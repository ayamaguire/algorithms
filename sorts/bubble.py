import time_it


def bubble(inlist):
    is_sorted = False
    the_list = inlist[:]
    n = len(the_list)
    last = the_list[:]
    while not is_sorted:
        for i in range(n-1):
            if the_list[i] <= the_list[i+1]:
                pass
            else:
                the_list[i], the_list[i+1] = the_list[i+1], the_list[i]
        if last == the_list:
            is_sorted = True
        last = the_list[:]


time_it.time_that_shit(func=bubble)
