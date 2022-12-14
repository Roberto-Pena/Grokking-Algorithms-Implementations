#BINARY SEARCH
def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:

        mid = (low+high)//2
        current = list[mid]

        if current == item:
            return mid
        elif current > item:
            high = mid-1
        elif current < item:
            low = mid+1

    return None

#SELECTION SORT
def find_smallest(list):
    smallest = list[0]
    smallest_index = 0

    for i in range(1,len(list)-1):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i
    return smallest_index

def selection_sort(list):
    new_list = []
    for i in range(len(list)):
        index = find_smallest(list)
        new_list.append(list[index])
        list.pop(index)
    return new_list

#Recursive Algorithms
def factorial(x):
    if x == 1:
        return 1
    elif x > 1:
        return x * factorial(x-1)

#Divide and Conquer
    #Recursive Algorithm For Array Sum 

    #Define a Base Case
    #Reduce the size of your problem until matching the base case

    # Sum of Arrays, Base case is to have an array with 0 or 1 element, 
    # that way the sum is either 0 or the element itself
    # Reduce the size of the problem by removing one element at the time and calling the function recursively

# Recursive functin to sum of the items in a list
def sum_array(list):
    if list == []:
        return 0
    else:
        return list[0] + sum_array(list[1:])

# Recursive function finding the number of items in a list
def number_items(list):
    if list == []:
        return 0
    else:
        return 1 + number_items(list[1:])

# Recursive function to find the max value of a list
def find_max(list):
    if list == []:
        return 0
    else:
        max_number = 0
        compare = find_max(list[1:])
        if list[0] > compare:
            max_number = list[0]
        else:
            max_number = compare
        return max_number

# Recursive Binary Search

#def recursive_binary_search(list, target):
    mid = (0+len(list))//2
    if list[mid] == target:
        return mid
    else:
        if mid > target:
            return recursive_binary_search(list[0:mid-1], target)
        elif mid < target:
            return recursive_binary_search(list[mid+1:], target)


def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less_pivot = []
        more_pivot = []
        for i in range(1,len(list)-1):
            if list[i] > pivot:
                more_pivot.append(list[i])
            else:
                less_pivot.append(list[i])
        return quicksort(less_pivot) + [pivot] + quicksort(more_pivot) 

#MAIN Test Cases
def main():
    my_list = [1, 3, 5, 7, 9]
    print(binary_search(my_list,3))
    list = [5, 3, 6, 2, 10]
    print(selection_sort(list))
    print(factorial(3))
    print(sum_array(my_list))
    print(number_items(my_list))
    print(find_max(my_list))
    #print(recursive_binary_search(my_list,3))
    print(quicksort(list))


if __name__ == "__main__":
    main()
