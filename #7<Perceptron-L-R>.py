def predict(row, weights):
    activation = weights[0]
    for i in range(len(row)-1):
        activation += weights[i + 1] * row[i]
        return 1.0 if activation >= 0.0 else 0.0
 
# Estimate Perceptron weights using stochastic gradient descent
def train_weights(train, l_rate, n_epoch):
	weights = [0.0 for i in range(len(train[0]))]
	for epoch in range(n_epoch):
		sum_error = 0.0
		for row in train: 
			prediction = predict(row, weights)
			error = row[-1] - prediction
			sum_error += error**2
			weights[0] = weights[0] + l_rate * error
			for i in range(len(row)-1):
				weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
	return weights
 
# Calculate weights
X1=[0.5,-1.1,0.24,-0.22,-1.8]
X2=[0.15,-1.4,0.11,-0.28,-0.3]
X3=[0.1,-1.4,0.11,0.6,-1.11] 
W=[0.1, 0.17,0.2,-1.1, -0.4]
dataset = []

dataset.append(X1)
dataset.append(X2)
dataset.append(X3)

l_rate = 2.5
n_epoch = 10
weights = train_weights(dataset, l_rate, n_epoch)


//final output
//>epoch=9, lrate=2.500, error=4.562
