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






#MAIN Test Cases
def main():
    my_list = [1, 3, 5, 7, 9]
    print(binary_search(my_list,3))
    list = [5, 3, 6, 2, 10]
    print(selection_sort(list))

if __name__ == "__main__":
    main()
