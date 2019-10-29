
def main():
    the_array = [15, 22, 84, 14, 88, 23]
    max_num = 0
    min_num = 999
    
    for i in the_array:
        if max_num < i:
            max_num = i
        elif min_num > i:
            min_num = i

    return max_num - min_num

def alternate():
    the_array = [15, 22, 84, 14, 88, 23]
    return max(the_array) - min(the_array)

# print(main())
