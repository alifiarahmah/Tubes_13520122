f = open("demofile.txt", "r")

cnt_layer = int(f.readline().strip('\n'))

print(cnt_layer)

input_activator_weight = []

# tinjau setiap layer
for i in range(int(cnt_layer - 1)):
    neuron_and_activator = f.readline().strip('\n')
    neuron_and_activator_split = neuron_and_activator.split(' ')

    cnt_neuron = int(neuron_and_activator_split[0])

    activator_type = " "
    if(i > 0):
        activator_type = neuron_and_activator_split[1]

    bobot_j = []
    for j in range(cnt_neuron + 1):
        bobot_read = f.readline().strip('\n')
        arr_bobot = bobot_read.split(' ')
        bobot_k = []
        for k in arr_bobot:
            bobot_k.append(int(k))
        bobot_j.append(bobot_k)

    input_activator_weight.append([cnt_neuron, activator_type, bobot_j])

output_layer = f.readline().strip('\n')
output_and_activator_split = output_layer.split(' ')
input_activator_weight.append(
    [int(output_and_activator_split[0]), output_and_activator_split[1]])
print(input_activator_weight)
