import numpy as np

def m_lambda_i(n, l):
    m = np.zeros((n, n))
    for i in range(n):
        m[i][i] = l

    return m

def m_mul(m1, m2):
    n_row = m1.shape[0]
    n_col = m2.shape[1]
    n_mid = m1.shape[1]
    m3 = np.zeros((n_row, n_col))
    for i in range(n_row):
        for j in range(n_col):
            sum = 0
            for k in range(n_mid):
                sum += m1[i][k]*m2[k][j]
            m3[i][j] = sum
    
    return m3

def m_add(m1, m2):
    n_row = m1.shape[0]
    n_col = m1.shape[1]
    m3 = np.zeros((n_row, n_col))
    for i in range(n_row):
        for j in range(n_col):
            m3[i][j] = m1[i][j] + m2[i][j]
    
    return m3

def m_invert(m):
    n = m.shape[0]
    m1 = m
    m2 = m_lambda_i(n, 1) #invert of m

    for i in range(n):
        t = m1[i][i]
        m1[i] /= t
        m2[i] /= t
        for j in range(n):
            if i != j:
                t = m1[j][i]
                m1[j] -= t * m1[i]
                m2[j] -= t * m2[i]
    
    return m2

def m_transpose(m):
    n_row, n_col = m.shape
    mt = np.zeros((n_col, n_row))
    for row in range(n_row):
        for col in range(n_col):
            mt[col][row] = m[row][col]

    return mt