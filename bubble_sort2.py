
print()

def bubbleSort(data_list):
    
  # loop for each element of list
  for i in range(len(data_list)):

    swapped = False
    
    # compare list elements
    for j in range(0, len(data_list) - i - 1):
      if data_list[j] > data_list[j + 1]:

        # SWAP 
        temp = data_list[j]
        data_list[j] = data_list[j+1]
        data_list[j+1] = temp

        swapped = True
          
    # list is already sort so no need for further comparisoned

    if not swapped:
      break

data_list = [-2, 45, 0, 11, -9]

bubbleSort(data_list)

print('Sorted Array in Ascending Order:', data_list)

print()















