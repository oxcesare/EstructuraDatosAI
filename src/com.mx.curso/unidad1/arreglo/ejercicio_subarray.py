#contar los subarray a partir un arreglo
array = [1, -2, 4, -5, 1]

contador = 0

# The outer loop determines the starting element of the subarray
for i in range(len(array)):
    sub_sum = 0  # 1. Initialize a new sum for each new subarray
    # The inner loop extends the subarray one element at a time
    for j in range(i, len(array)):
        sub_sum += array[j]  # 2. Add the current element to the subarray's sum
        if sub_sum < 0:
            contador += 1  # 3. Increment the counter if the sum is negative

print(contador)