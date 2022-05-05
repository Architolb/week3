# Find Middle Number
# Given a number (n) and an array of numbers (num_list) as input to a function, 
# return True if the number is greater than the middle number of the array. 
# Return False if the number is less than the middle number of the array.
# If the array has an even amout of indexes you must decide how to handle that.

# Example Input: n = 4, array = [3,5,8, 10]
# Example Output: False
# Example Input: n = 105, array = [10,30,44,22,100]
# Example Output: True

def middle_number(n, num_list):
    return n > num_list[len(num_list)//2]



def determine_middle_n(n_list, n):
    my_odd = True
    if len(n_list) % 2 == 0:
        length_list = len(n_list) - 1
        my_odd = False
    else:
        length_list = len(n_list)
    if my_odd == False:
        middle_index = length_list // 2
        x = n_list[middle_index]
        y = n_list[middle_index + 1]
        new_middle_index = (x + y) / 2
    if my_odd == True:
        middle_index = length_list // 2
        new_middle_index = n_list[middle_index]
    return n > new_middle_index
print(determine_middle_n(array, n))


# OOP - Create your own object. Make at least two additional methods for it.



