
##Code to do Bubble Sort###

# Keep left part of the array sorted
# Big O : O(N*N)

#global step_counter;
step_counter = 0;

def selection_sort(list):
    global step_counter;

    for j in range(0,len(list)-1):
        step_counter += 1;
        index = find_smallest ( list[j:len(list)] ) + j;
        if (index != j):
            list[index], list[j] = list[j], list[index];

    print("The sorted list is :" + str(list))
    print("Steps needed to sort :" + str(step_counter));


def find_smallest(list):
    global step_counter;

    smallest_num = list[0];
    smallest_num_index = 0;

    for i in range(0, len(list)-1):
        step_counter += 1;
        if(smallest_num > list[i+1]):
            smallest_num = list[i+1];
            smallest_num_index = (i+1);
    return smallest_num_index;


a = [0, 11, 2, -7, 200];
selection_sort(a);


