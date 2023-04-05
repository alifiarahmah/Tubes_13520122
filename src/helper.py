# Helper function
from math import exp

# net -> persamaan linear (ax+b+...)


def linear(net):
    return net


def relu(net):
    return max(0, net)


def sigmoid(net):
    return float(1/(1 + exp(net * -1)))


def softmax(net_i, arr_net):
    net_sum = 0
    for i in arr_net:
        net_sum += i
    return (exp(net_i))/net_sum


def multiplyMatrix(m1, m2):
    m3 = []
    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m2[0])):
            m3[i].append(0.0)
            for k in range(len(m1[0])):
                m3[i][j] += float(m1[i][k] * m2[k][j])

    return m3


def addMatrix(m1, m2):
    m3 = []
    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m2)):
            m3[i].append(0)
            m3[i][j] = m1[i][j] + m2[i][j]

    return m3
