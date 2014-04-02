import random, math

N = 4
sigma = 0.2
condition = False
while condition == False:
    L = [(random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))] # Generates random x,y coordinate
    for k in range(1, N):
        a = (random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))
        min_dist = min(math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) for b in L) # Loops through L to check dist for e/ hard disk
        if min_dist < 2.0 * sigma: #if there's overlap of disks
            condition = False
            break # start from beginning of while loop due to overlap
        else:
            L.append(a) # adds the new circle coordinates to L
            condition = True
print L
