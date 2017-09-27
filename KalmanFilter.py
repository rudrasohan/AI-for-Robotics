

def update(mean1, var1, mean2, var2):
    new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = var1*var2/(var1+var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

for i in range(len(measurements)):
	list1 = update(mu,sig,measurements[i],measurement_sig)
	mu = list1[0]
	sig = list1[1]
	print "update:",[mu, sig]
	list1 = predict(mu,sig,motion[i],motion_sig)
	mu = list1[0]
	sig = list1[1]
	print "predict:",[mu, sig]
