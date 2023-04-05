import json
import os
import numpy as np

filename = str(input("Masukkan nama file model: "))
f = open('./test/'+filename)

data = json.load(f)

# create array of bias
bias = []

# create matrix of weight
mat_weight = []

# get bias and weight from weight
arr_weight = data["case"]["weights"]
# print(arr_weight)
for i in arr_weight:
    bias.append(i[0])
    mat_weight.append(i[1:])

print(mat_weight)
print(bias)

# get layers from json
arr_layer = data["case"]["model"]["layers"]

# create array of activation function
arr_activation = []

for i in range(len(arr_layer)):
    arr_activation.append(arr_layer[i]["activation_function"])

print(arr_activation)

# get input data
arr_input = data["case"]["input"]
for i in arr_input:
    print(i)
# print(arr_input)

# predict
# get count layer
cnt_layer = data["case"]["model"]["input_size"]
print(cnt_layer)

current_data = [arr_input[2]]
print(current_data)

for i in range(cnt_layer):
    current_data = np.dot(current_data, mat_weight[i]) + bias[i]

print("result", current_data)
f.close()
