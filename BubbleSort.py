
##Code to do Bubble Sort###

def bubble_sort(list):
    sorted = True;
    step_counter = 0;
    for i in range(0, len(list)-1):
        for y in range(0,len(list)-1):
            step_counter+=1;
            if(list[y]>list[y+1]):
                list[y], list[y+1] = list[y+1], list[y];
                sorted = False;
        if(sorted):
            break;
    print("Sorted list is" + str(list));
    print("Steps needed for " + str(len(list)) + " elements : " + str(step_counter));

a = [70, 15 ,78, 2, 0];
bubble_sort(a);

