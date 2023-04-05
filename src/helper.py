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
        net_sum += exp(i)
    return (exp(net_i))/net_sum
