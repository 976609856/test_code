#遗传算法求最小值
import numpy as np
import matplotlib.pyplot as plt
from numpy import random
from numpy.lib.function_base import select

def fitness_func(X):
	a=10
	pi=np.pi
	x=X[:,0]
	y=X[:,1]
	return 2*a+x**2+y**2-a*np.cos(2*pi*x)-a*np.cos(2*pi*y)

def decode(x,a,b):
	xt=0
	for i in range(len(x)):
		xt=xt+x[i]*np.power(2,i)
	return a+xt*(b-a)/(np.power(2,len(x))-1)

def decode_X(X:np.array):
	X2=np.zeros((X.shape[0],2))
	for i in range(X.shape[0]):
		xi=decode(X[i,:20],-5,5)
		yi=decode(X[i,20:],-5,5)
		X2[i,:]=np.array(xi,yi)
	return X2

def select(X,fitness):   #根据概率得到X的不同行
	fitness=1/fitness
	fitness=fitness/fitness.sum()
	idx=np.array(list(range(X.shape[0])))
	X2_inx=np.random.choice(idx,X.shape[0],p=fitness)
	X2=X[X2_inx,:]
	return X2

def crossover(X,c):
	"""按顺序选择2个个体与概率c进行交叉操作"""
	for i in range(0,X.shape[0],2):
		xa=X[i,:]
		xb=X[i+1,:]
		for j in range(X.shape[1]):
			if np.random.rand() <= c :
				xa[j],xb[j]=xb[j],xa[j]
		X[i,:]=xa
		X[i+1,:]=xb
	return X

def mutation(X,m):
	for i in range(X.shape[0]):
		for j in range(X.shape[1]):
			if np.random.rand() <= m:
				X[i,j]=(X[i,j]+1)%2
	return X

def ga():
	"""变异操作"""
	c=0.3
	m=0.05
	best_fitness=[]
	best_xy=[]
	best_num=[]
	iter_num=100
	X0=np.random.randint(0,2,(50,40)) #0,1矩阵
	for i in range(iter_num):
		X1=decode_X(X0)
		fitness =fitness_func(X1)
		X2=select(X0,fitness)
		X3=crossover(X2,c)
		X4=mutation(X3,m)

		X5=decode_X(X4)
		fitness=fitness_func(X5)
		best_fitness.append(fitness.min())
		x,y=X5[fitness.argmin()]
		best_xy.append((x,y))
		X0=X4
	
	print("最优解是：%.5f" % best_fitness[-1])
	print("最优解是：x=%.5f,y=%.5f" % best_xy[-1])
	plt.plot(best_fitness,color='r')
	plt.show()

ga()