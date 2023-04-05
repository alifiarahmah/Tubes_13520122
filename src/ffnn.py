import json
import os
import numpy as np
import helper

filename = str(input("Masukkan nama file model: "))
f = open('./test/'+filename)

data = json.load(f)

# create array of bias
bias = []

# create matrix of weight
mat_weight = []

# get bias and weight from weight
arr_weight = data["case"]["weights"]
for i in arr_weight:
    bias.append(i[0])
    mat_weight.append(i[1:])

# get layers from json
arr_layer = data["case"]["model"]["layers"]

# create array of activation function
arr_activation = []

for i in range(len(arr_layer)):
    arr_activation.append(arr_layer[i]["activation_function"])

# get input data
arr_input = data["case"]["input"]

# predict
# get count layer
cnt_layer = len(data["case"]["model"]["layers"])

# create array of output
output = []

# loop for every input
for i in range(len(arr_input)):
    current_data = [arr_input[i]]

    # loop for every layer
    for j in range(cnt_layer):
        hj = np.dot(current_data, mat_weight[j]) + bias[j]
        current_data = hj

        # loop for every neuron
        for k in range(len(current_data[0])):
            print("neuron", (current_data[0][k]))

            # TO DO: Refactoring error of change value in numpy
            # if (arr_activation[j] == "linear"):
            #     current_data[0][k] = helper.linear(current_data)
            # if (arr_activation[j] == "relu"):
            #     current_data[0][k] = helper.relu(current_data)

    output.append(current_data)

print(output)
f.close()
