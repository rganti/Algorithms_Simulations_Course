
import random, pylab

histo_data = []
L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
sigma = 0.1197
sigma_sq = sigma ** 2
delta = 0.1
n_steps = 2000000
for steps in range(n_steps):
    a = random.choice(L) # probably picks a random circle in L
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
    box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma #if this isn't satisfied, means circle touches or overlaps the wall
    if not (box_cond or min_dist < 4.0 * sigma ** 2):
        a[:] = b
    histo_data.append(a[0])

pylab.hist(histo_data, bins=100, normed=True)
pylab.xlabel('x')
pylab.ylabel('frequency')
pylab.title('frequency vs. x-coordinate of disks')
pylab.grid()
pylab.savefig('markov_disks_histo.png')
pylab.show()