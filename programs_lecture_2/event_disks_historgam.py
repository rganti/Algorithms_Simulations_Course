import math, pylab

def wall_time(pos_a, vel_a, sigma):
    if vel_a > 0.0:#Not sure why this condition is specified
        del_t = (1.0 - sigma - pos_a) / vel_a #1.0 - sigma(disk_radius) - pos_a(position_particle_a) ?
    elif vel_a < 0.0:
        del_t = (pos_a - sigma) / abs(vel_a)
    else:
        del_t = float('inf')
    return del_t

def pair_time(pos_a, vel_a, pos_b, vel_b, sigma):
    del_x = [pos_b[0] - pos_a[0], pos_b[1] - pos_a[1]] 
    del_x_sq = del_x[0] ** 2 + del_x[1] ** 2
    del_v = [vel_b[0] - vel_a[0], vel_b[1] - vel_a[1]]
    del_v_sq = del_v[0] ** 2 + del_v[1] ** 2
    scal = del_v[0] * del_x[0] + del_v[1] * del_x[1] # scal = dv_{x}dx + dv_{y}dy # del_v vector dotted with del_x vector
    Upsilon = scal ** 2 - del_v_sq * ( del_x_sq - 4.0 * sigma **2)
    if Upsilon > 0.0 and scal < 0.0:
        del_t = - (scal + math.sqrt(Upsilon)) / del_v_sq
    else:
        del_t = float('inf')
    return del_t

histo_data = []
pos = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]] #positions of hard disks
vel = [[0.21, 0.12], [0.71, 0.18], [-0.23, -0.79], [0.78, 0.1177]] #velocity of hard disks
singles = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1)] #has to do with wall collisions
pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)] #has to do with pair collisions
sigma = 0.1197 #radius of hard disk
t = 0.0 #time step
n_events = 1000000
for event in range(n_events):
    wall_times = [wall_time(pos[k][l], vel[k][l], sigma) for k, l  in singles] #searching for pos, vel according to singles
    pair_times = [pair_time(pos[k], vel[k], pos[l], vel[l], sigma) for k, l in pairs] #searching for pos, vel according to pairs
    next_event = min(pair_times + wall_times) # takes minimum of wall_times and pair_times to get next event
    t_previous = t
    for inter_times in range(int(t + 1), int(t + next_event + 1)):
        del_t = inter_times - t_previous
        for k, l in singles: pos[k][l] += vel[k][l] * del_t
        t_previous = inter_times
        for k in range(4): histo_data.append(pos[k][0])
    t += next_event
    for k, l in singles: pos[k][l] += vel[k][l] * (t - t_previous) #reconfiguring positions of disks
    if min(wall_times) < min(pair_times): # if disk hits wall first
        collision_disk, direction = singles[wall_times.index(next_event)] # if it hits the wall, single[event_time] will yield specific pair in singles(1st:specified collision disk, 2nd:x or y direction)
        vel[collision_disk][direction] *= -1.0 # velocity conserved but multiplied by -1 to change direction
    else: # if disk hits another disk first
        a, b = pairs[pair_times.index(next_event)]
        del_x = [pos[b][0] - pos[a][0], pos[b][1] - pos[a][1]]
        abs_x = math.sqrt(del_x[0] ** 2 + del_x[1] ** 2)
        e_perp = [c / abs_x for c in del_x] # normal vector
        del_v = [vel[b][0] - vel[a][0], vel[b][1] - vel[a][1]]
        scal = del_v[0] * e_perp[0] + del_v[1] * e_perp[1] #This is del_v vector dotted with normal vector, e_perp
        for k in range(2): 
            vel[a][k] += e_perp[k] * scal 
            vel[b][k] -= e_perp[k] * scal
    print 'event', event
    print 'time', t
    print 'pos', pos
    print 'vel', vel

pylab.hist(histo_data, bins=100, normed=True)
pylab.xlabel('x')
pylab.ylabel('frequency')
pylab.title('event disks regular intervals')
pylab.grid()
pylab.savefig('event_disks_histo_A331.png')
# pylab.show()
