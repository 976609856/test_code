#遗传算法求最小值
import numpy as np
import matplotlib.pyplot as plt
from numpy import random

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





 ga():
	"""变异操作"""
	c=0.3
	m=0.05
	best_finess=[]
	best_xy=[]
	best_num=[]
	iter_num=[]
	x0=np.random.randint(0,2,(50,40)) #0,1矩阵
	for i in range(iter_num):
		X1=decode_X(X0)
		fitness =fitness_func(X1)
