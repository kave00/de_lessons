l1 = [7, 6, 5, 4, 3, 2, 1]
def bubble_sort (my_array):
    n = len(my_array)
    count = 0
    for i in range(n - 1):
        for j in range (n - 1):
            if my_array[j] > my_array[j+1]:
                tmp = my_array[j]
                my_array[j] = my_array[j+1]
                my_array[j+1] = tmp
                count += 1
    print(count)
    return my_array



print(bubble_sort(l1))