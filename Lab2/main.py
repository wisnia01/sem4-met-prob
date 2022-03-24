import math
from operator import xor
from bitarray.util import ba2int
from bitarray import bitarray
A = 69069
X_0 = 15
C = 1
N = 100000
M = pow(2, 31) - 1
prob_bucket = [0] * 10


def generate(prev_val):
    return (A * prev_val + C) % M


# 2.2
value = X_0
for _ in range(N):
    value = generate(value)
    bucket_index = math.floor(10 * value / M)
    prob_bucket[bucket_index] += 1

print(prob_bucket)

# 2.6
prob_bucket = [0] * 10
P = 7
Q = 3
bit_array = [0] * 24
bit_start = [1, 0, 1, 1, 0, 1, 0]
bit_array += bit_start
print(bit_array)
for _ in range(N):
    for index in range(31-7):
        bit_array[index] = xor(bit_array[index+P], bit_array[index+Q])
    ba = bitarray(bit_array)
    value = ba2int(ba)
    # print(value)
    bucket_index = math.floor(10 * value / M)
    # print(bucket_index, "test")
    prob_bucket[bucket_index] += 1
    for i in range(31-25):
        bit_array[i+25] = bit_array[i]
print(prob_bucket)




