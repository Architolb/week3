# Move Zeros
# Given an array nums, write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.
# Example:
input_list = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example Input: [0,0,11,2,3,4]
# Example Output: [11,2,3,4,0,0]


def new_order(moveitems):
    counter = 0
    #every time we remove a 0 increase 1
    #for i in moveitems
    while 0 in moveitems:
        moveitems.remove(0)
        counter += 1
    print(counter)
    for i in range(counter):
        moveitems.append(0)
    return moveitems
print(new_order(input_list))







