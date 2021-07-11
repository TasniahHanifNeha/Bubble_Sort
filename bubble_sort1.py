# n = 5
# for i in range(0,n):
#     print("Loop 1: i-",i, " \n-----------------")
#     for j in range(0, n-i-1):
#         print("j - ",j)
print()


def bubble_sort(data_list):
    n = len(data_list)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if data_list[j] > data_list[j + 1]:
                # SWAP
                temp = data_list[j]
                data_list[j] = data_list[j+1]
                data_list[j+1] = temp

data_list = [-5, 45, 0, 15, -10]
bubble_sort(data_list)
print('Sorted list :',data_list)




print()















