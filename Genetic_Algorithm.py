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
	X2=np.zeros(X.shape[0],2)
	for i in range(X.shape[0]):
		x[i]=decode(X[i,:20],-5,5)
		y[i]=decode(X[i,20:],-5,5)
		X2[i,:]=np.array(x[i],y[i])
	return X2

def select(X,fitness):   #根据概率得到X的不同行
	fitness=1/fitness
	fitnesss=fitness/fitness.sum()
	idx=np.array(list(range(X.shape[0])))
	X2_inx=np.random.choice(idx,X.shape[0],p=fitness)
	X2=X[X2_inx,:]
	return X2

def 





 ga():
	"""变异操作"""
	c=0.3
	m=0.05
	best_finess=[]
	best_xy=[]
	best_num=[]
	iter_num=[]
	X0=np.random.randint(0,2,(50,40)) #0,1矩阵
	for i in range(iter_num):
		X1=decode_X(X0)
		fitness =fitness_func(X1)
		X2=select(X0,fitness)