import random, numpy, math, pylab

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
    for i in [float(j) / 10 for j in range(1,50,1)]:
        acc_list = []
        for run in range(n_runs):
            (n_hits,n_acc) = markov_pi(n_trials, i)
            # print 4.0 * n_hits / float(n_trials)
            acc_list.append(n_acc / float(n_trials))
        y_vec.append(round(numpy.mean(acc_list),2))
        x_vec.append(i)
    return (x_vec,y_vec)

def rms_error():
    n_runs = 500
    n_trials = 1000
    sigma_vec = []
    delta_vec = []
    pi_vec = []
    avg_pi = []
    sigma = 0.0
    for i in [float(j) / 10 for j in range(1,50,1)]:
        for run in range(n_runs):
            (n_hits,n_acc) = markov_pi(n_trials, i)
            pi_est = 4.0 * n_hits / float(n_trials)
            sigma += (pi_est - math.pi) ** 2
            pi_vec.append(pi_est)
        avg_pi.append(round(numpy.mean(pi_vec),5))
        sigma_vec.append(round(math.sqrt(sigma/(n_runs)),2))
        delta_vec.append(i)
    return (delta_vec,sigma_vec,avg_pi)

(delta_vec,sigma_vec,avg_pi) = rms_error()

print avg_pi, sigma_vec
print 'Pi = ', math.pi

x_vec = []
y_vec = []

(x_vec,y_vec) = acceptance(x_vec, y_vec)

print x_vec, y_vec

pylab.plot(delta_vec, sigma_vec, 'o')
# pylab.gca().set_xscale('log')
# pylab.gca().set_yscale('log')
pylab.xlabel('$\delta$')
pylab.ylabel('$\sigma$')
pylab.title('$\sigma$ as a function of $\delta$')
pylab.savefig('rms_errorfcnofdelta.png')

# Acceptance ratio of 1/2 between Delta = 1.1 and 1.2