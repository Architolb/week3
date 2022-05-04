numbers = [4, 11, 68, 22, 44, 7, 11, 8]
more_nums = [2, 3, 5, 1, 7, 9, 1, 12]


doubled = list(map(lambda x,y: (((x * 2) - 1),((y * 2) - 1)) if x > 0 and y > 0 else (x,y), numbers, more_nums))
print(doubled)



list1=range(1,11)
print(list(map(lambda x: x*2-1,list1)))
