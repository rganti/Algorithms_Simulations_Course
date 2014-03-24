import random, pylab, math

def markov_pi_all_data(N, delta):
    x, y = 1.0, 1.0
    data = []
    for i in range(N):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
        if x ** 2 + y ** 2 < 1.0:
            data.append(4.0) # Adds 4 to array when a hit happens (point inside the circle)
        else:
            data.append(0.0) # Adds 0 to array if a hit doesn't happen
    return data

poweroftwo = 14
n_trials = 2 ** poweroftwo
delta = 0.1
data = markov_pi_all_data(n_trials, delta)
errors  = []
bunches = []
for i in range(poweroftwo):
    new_data = [] #Should be add data calculated from algorithm
    mean = 0.0
    mean_sq = 0.0
    N = len(data)
    while data != []:
        x = data.pop() #Removes latest data value in array
        y = data.pop() #Removes next latest data value: thus create pair
        mean += x + y # Adding the pair together for mean calculation <x>
        mean_sq += x ** 2 + y ** 2 # Squaring e/ in pair and adding: for <x^2>
        new_data.append((x + y) / 2.0 )
    errors.append(math.sqrt(mean_sq / N - (mean / N) ** 2) / math.sqrt(N))
    bunches.append(i)
    data = new_data[:] # Not sure what this part is doing.
pylab.plot(bunches, errors, 'o')
pylab.xlabel('iteration')
pylab.ylabel('naive error')
pylab.title('Bunching: naive error vs iteration number')
pylab.savefig('apparent_error_bunching.png', format='PNG')
pylab.show()