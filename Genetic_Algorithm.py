#遗传算法求最小值
import numpy as np
import matplotlib.pyplot as plt









def ga():
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
