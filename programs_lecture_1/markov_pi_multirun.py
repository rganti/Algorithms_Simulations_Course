import random, numpy

def markov_pi(N, delta): 
    x, y = 1.0, 1.0
    n_hits = 0
    n_acc = 0
    for i in range(N):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
            n_acc += 1
        if x**2 + y**2 < 1.0: n_hits += 1
    return (n_hits,n_acc)

def acceptance(x_vec, y_vec):
    n_runs = 500
    n_trials = 1000
    delta = numpy.arange(0.1,1.0,0.1)
    for i in numpy.nditer(delta):
        acc_list = []
        for run in range(n_runs):
            (n_hits,n_acc) = markov_pi(n_trials, i)
            # print 4.0 * n_hits / float(n_trials)
            acc_list.append(n_acc / float(n_trials))
        x_vec.append(numpy.mean(acc_list))
        y_vec.append(i)
    return (x_vec,y_vec)

x_vec = []
y_vec = []

print acceptance(x_vec, y_vec)