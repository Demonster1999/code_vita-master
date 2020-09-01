"""
Problem Description
A company manufactures walls which can be directly implanted at the site. The company uses small square bricks of material C and material D which have similar looks but have huge difference in quality. The company manufactures walls of square shapes only to optimize their costs.

A novice employee created a square wall using bricks of material C and D. However, the client had asked the wall to be made of only high-quality material - material C.

To solve this problem, they will place the wall in a special furnace and heat it such that the material D melts and only material C remains. Material C brick will move down due to gravity if a material D brick below it melts. The new empty space created will be filled by new material C square walls. They also want to use biggest possible C square wall while building the final wall. For this they will position the wall in the furnace in an optimal way i.e. rotate by 90-degrees any number of times, if required, such that the biggest space possible for new material C wall is created. No rotations are possible when the furnace starts heating.

Given the structure of the original wall created by the novice employee, you need to find out the size of the new C square wall which can be fitted in the final wall which will be delivered to the client.

Constraints
1 < N < 100

Input
First Line will provide the size of the original wall N.

Next N lines will provide the type of material (C and D) used for each brick by the novice employee.

Output
Size of the biggest possible C square wall which can be fitted in the final wall.

Time Limit
1


Examples
Example 1

Input

4

C D C D

C C D C

D D D D

C D D D

Output

3

Explanation

If the wall is placed with its left side at the bottom, space for a new C wall of size 2x2 can be created. This can be visualized as follows

D C D D

C D D D

D C D D

C C D C

The melted bricks can be visualized as follows

- - - -

- C - -

C C - -

C C - C

Hence, the maximum wall size that can be replaced is 2x2.

If the wall is placed as it is with its original bottom side at the bottom, space for a new C wall of size 3x3 can be created. Post melting, this can be visualized as follows.

- - - -

C - - -

C - - -

C C C C

Hence, the maximum wall size that can be replaced is 3x3 in this approach.

Since no rotations followed by heating is going to a yield a space greater than 3x3, the output is 3.

Example 2

Input

7

C D D C D D D

C D D C D D D

D D D D D D C

D C D C D D D

D D D C D C D

C D D C D C C

C D C D C C C

Output

5

Explanation

If the wall is placed with its left side at the bottom, a space for new C wall of size 5x5 can be created. This can be visualized as follows

D D C D D C C

D D D D C C C

D D D D D D C

C C D C C C D

D D D D D D C

D D D C D D D

C C D D D C C

When this orientation of the wall is heated, a space for new C wall of size 5x5 is created after the D bricks melt

_ _ _ _ _ _ _

_ _ _ _ _ _ _

_ _ _ _ _ _C

_ _ _ _ _ _ C

_ _ _ _ _ C C

C C _ C C C C

C C C C C C C

Whereas, if the rotation was not done, the wall formed after the D bricks melt will be as follows

_ _ _ _ _ _ _

_ _ _ _ _ _ _

_ _ _ C _ _ _

C _ _ C _ _ _

C _ _ C _ _ C

C _ _ C _ C C

C C C C C C C

When this orientation of the wall is heated, a space for new C wall of size 3x3 only is created after the D bricks melt

Hence rotation is important and correct answer is 5x5

Since no rotations followed by heating is going to a yield a space greater than 5x5, the output is 5.

"""
# imports 
import copy # for creating copies instead of refrence 
import math
list_observations = []



# def rotate_wall(wall_matrix , size):

#     """
#     this function is used to rotate the wall and check the possiblity of the current rotation.
#     this function is built on the top of the below link:
#     https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/
#     """
#     for x in range(0, size//2):
        
#         for y in range(x, size-x-1):
#             # it takes the  current values from the matrix
#             temp = wall_matrix[x][y]
#             wall_matrix[x][y] = wall_matrix[y][size-1-x]
#             wall_matrix[y][size-1-x] = wall_matrix[size-1-x][size-1-y]
#             wall_matrix[size-1-x][size-1-y] = wall_matrix[size-1-y][x]
#             wall_matrix[size-1-y][x] = temp
#     return wall_matrix


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

wall_size = int(input())
if wall_size == 1 and wall_size <=100:
wall_structure = [input().split() for i in range(wall_size)]
print(heat_wall(copy.deepcopy(wall_structure), wall_size))

else:
    pass

# print(wall_structure) 
# print(rotate_wall(copy.deepcopy(wall_structure),wall_size))














