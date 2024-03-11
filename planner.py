# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:51:15 2024

@author: 15834
"""

import numpy as np
from scipy.linalg import block_diag
from scipy.optimize import minimize 

def cum_prod(S, x_0):
    N = S.shape[2]
    m = x_0.shape[0]
    P = np.eye(m)
    for i in range(N):
        P = np.dot(P, S[:, :, i])
    return P

def MPCplanner(x0,v0,y0,fi0,x1, x_des,v1, y_des, step,N,w1,w2,w3, w4,w5):
    '''
    x0:初始位置   v0:初始速度  y0:初始纵向距离 fi0:初始航向角 x1 前车位置 v_des:期望速度 y_des: 期望车道  v1:前车速度    step:步长   N:预测时域
    w1,w2,w3,w4:分别是速度、加速度、纵向距离、航向角权重
    '''
    #定义初始状态和时间步长
    x_0 = np.array([x0, v0, y0, fi0]).reshape(-1, 1)
    X_des=np.array([x1+x_des, v1, y_des, 0],dtype=object).reshape(-1, 1)
    #定义系统动态方程 x(k+1) = A*x(k) + B*u(k)
    A = np.array([[1, step, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 1, v0*step],
                  [0, 0, 0, 1]])        
    B = np.array([[0.5 * step ** 2, 0],
                  [step, 0],
                  [0, 0],
                  [0, step * v0/4]])
    #定义目标状态和控制输入的权重矩阵 Q 和 R
    Q = np.diag([w1, w2, w4, w5])
    R =np.diag([w3, 0])
    #转化为用控制量ut表示的，关于状态量的推导方程的矩阵
    M=np.eye(4)
    C=np.zeros((4,2*N))
    C = np.concatenate((C, np.kron(np.diag(np.ones(N)), B)), axis=0)
    Qt = np.kron(np.diag(np.concatenate((np.ones(N), np.array([0])))), Q)
    Rt = np.kron(np.diag(np.ones(N)), R)
    
    for i in range(1, N+1):
        M = np.vstack((M, np.linalg.matrix_power(A, i)))
        if i == 1:
            pass  # 与Matlab中的 '1;' 相对应，这里什么都不做
        else:
            for j in range(1, i):
                C[4*i:4*i+4, 2*j-2:2*j] = np.dot(np.linalg.matrix_power(A, i-j), B)
    # 更新X_des
        X_des = np.vstack((X_des, np.array([x1 + i*step*v1 + x_des, v1, y_des, 0],dtype=object).reshape(-1, 1)))
    
    u_max = np.array([3, 0.7]).reshape(-1,1)
    u_min = np.array([-5, -0.7]).reshape(-1,1)
    U_max = np.tile(u_max, (N, 1))
    U_min = np.tile(u_min, (N, 1))
    H = C.T @ Qt @ C + Rt
    f = 2 * (x_0.T @ M.T - X_des.T) @ Qt @ C
    obj_func = lambda x: 0.5 * x.T @ H @ x + f @ x
    bounds = [(low, high) for low, high in zip(U_min.flatten(), U_max.flatten())]
    x0 = np.zeros(20)
    result = minimize(obj_func, x0, method='SLSQP', bounds=bounds, options={'maxiter': 100000})
    sol = result.x
    acc = sol[0]
    angle = sol[1]
    return acc,angle