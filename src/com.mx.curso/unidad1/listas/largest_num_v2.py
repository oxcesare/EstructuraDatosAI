my_List = [30,12, 45, 67, 89, 23, 3, 78, 90, 111, 56, 34]
largest = my_List[-1] 
my_List.sort()

print(largest)

my_List.append(100)  # Añadir un nuevo elemento para probar
for i in range(len(my_List)):
    if my_List[i] > largest:
        largest = my_List[i]
print(largest)        