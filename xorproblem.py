import numpy as np
def sigmoid(x): return 1/(1+np.exp(-x))
def sigmoid_d(x): return x *(1-x)

#XOR problem - a simple neural net test
x=np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

np.random.seed(42)
W1=np.random.randn(2,4)* 0.5#input hidden weights
W2=np.random.randn(4,1)*0.5 #hidden output weights

lr=0.5
losses=[]
for epoch in range(10000):
    #forward pass
    h=sigmoid(x @ W1)
    o=sigmoid(h @ W2)

 #loss (mean squared error)
    loss=np.mean((y-o)**2)
    losses.append(loss)

#backward pass-comute gradient
    d_o=(o-y)*sigmoid_d(o)
    d_h=(d_o@ W2.T)*sigmoid_d(h)

#update wieghts
    W2-=lr *h.T@ d_o
    W1-=lr*x.T @ d_h

import matplotlib.pyplot as plt
plt.plot(losses);plt.title('loss decreasing durng training')
plt.xlabel('epoch');plt.ylabel('loss');plt.show()

print('final predictiond(should decreasing during training)')
print(np.round(0,2))