# imports 
import copy # for creating copies instead of refrence 
import math

def check_perfect_square(number):
    square_root = number**0.5
    return ((square_root - math.floor(square_root) )== 0)


def heat_wall(wall_matrix,size):
    n_of_c =0
    for i in range(size):
        for j in range(size):
            if wall_matrix[i][j]== 'D':
              pass
            else : 
                n_of_c += 1
    if check_perfect_square(n_of_c):
        return n_of_c
    else:
        """
        i used the below code block only . using the link given as attribution 
        attribution : 
        https://www.geeksforgeeks.org/find-the-next-perfect-square-greater-than-a-given-number/
        """
        return  math.floor(math.sqrt(n_of_c)) + 1



#taking input
try:
    wall_size = int(input())
    if wall_size >= 1 and wall_size <=100:
        wall_structure = [input().split() for i in range(wall_size)]
        print(heat_wall(copy.deepcopy(wall_structure), wall_size))


except : 
    pass


# print(wall_structure) 
# print(rotate_wall(copy.deepcopy(wall_structure),wall_size))














