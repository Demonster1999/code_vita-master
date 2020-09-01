Corona Virus
Problem Description
A city is represented as two-dimensional rectangular matrix. The outer wall of the given matrix denotes the boundaries of the city. Citizens are dispersed in the city at different locations. They are either depicted by {a, c}. Corona Virus has already infected the city.

The Corona Virus enters the city from coordinate (0, 0) and traverses along a diagonal path until it encounters a human. If it encounters a human, designated as a , its trajectory rotates anti clockwise (right to left) by 90 degrees. Similarly, if it encounters a human, designated as c , its trajectory rotates clockwise (left to right) by 90 degrees. After infecting the person, the virus continues to move along its diagonal path.

During its traversal if it hits the boundary of the city for the first time, it rotates 90 degrees to reenter the city. However if it hits any of the boundary wall, the second time, the virus gets destroyed.

You have to calculate the trajectory taken by the virus, print the city map where infected citizens can be found and finally report the number of safe and infected citizens. com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@720bf02:image1.gif

Input
An input matrix of 9 rows and 20 columns comprising of {*, a, c, . } characters where

* denotes an element on the boundaries of the city

a denotes citizen after encountering whom the virus trajectory changes by 90 degrees (anti clockwise direction)

c denotes citizen after encountering whom the virus trajectory changes by 90 degrees (clockwise direction)

. (dot) denotes empty location within the city

Output
Random number of lines each denoting the coordinates of the trajectory of the virus.

From next line an output matrix of 9 rows and 20 columns comprising of {*, a, c, ., - } characters where

* denotes an element on the boundaries of the city

a denotes citizen after encountering whom the virus trajectory changes by 90 degrees (anti clockwise direction)

c denotes citizen after encountering whom the virus trajectory changes by 90 degrees (clockwise direction)

. (dot) denotes empty location within the city

- denotes the location of the infected citizen

And the next two lines print the number of safe and infected citizens in the city

Refer Examples section for better understanding.

Constraints
0 <= x <= 20

0 <= y <= 8

The virus cannot hit the three corners (20, 8) (20, 0) (0, 8)

Time Limit
1


Examples
Example 1

Input

********************

*....c.............*

*...c..............*

*c.................*

*.............a....*

*c.c...............*

*.a................*

*...........c......*

********************

Output

0 0

1 1

2 2

1 3

2 4

3 5

4 6

5 5

6 4

7 3

8 2

9 1

10 0

11 1

12 2

13 3

14 4

13 5

12 6

11 7

10 8

********************

*....c.............*

*...-..............*

*c.................*

*.............-....*

*-.c...............*

*.-................*

*...........c......*

********************

safe=4

infected=4

Explanation

The virus trajectory starts from (0,0) and crosses (1,1) (2,2). At (2,2) we have a citizen of type a causing the virus trajectory to be rotated by 90 degrees anti clockwise. It moves until the next citizen in its path is encountered at (1, 3) of type c causing the virus trajectory to be rotated by 90 degree clockwise. It continues on its path till it reaches the next human in its path at (4,6) of type c Virus trajectory is again rotated by 90 degrees clockwise until it hits the boundary at (10,0). Since this is the first time that the virus hits the boundary, it rotates by 90 degrees anticlockwise to reenter the city. The trajectory then continues towards (11,1) (12,2) (13,3) and finally a citizen at (14,4) of type a rotating the trajectory to 90 degree anticlockwise. From there it continues its trajectory and hits the boundary at (10,8).

Since this is the second time the virus hits the boundary, the virus is destroyed.

So, along its trajectory starting from (0,0) it has infected 4 citizens at location (2,2) (1,3) (4,6) (14,4). The other 4 citizens who did not come in the virus trajectory are deemed to be safe.

Example 2

Input

********************

*..................*

*..c...............*

*....c.............*

*.........a........*

*..................*

*.......a......c...*

*..................*

********************

Output

0 0

1 1

2 2

3 3

4 4

5 5

6 4

7 3

8 2

9 3

10 4

9 5

8 6

7 7

6 8

5 7

4 6

3 5

2 4

1 3

0 2

********************

*..................*

*..c...............*

*....-.............*

*.........-........*

*..................*

*.......-......c...*

*..................*

********************

safe=2

infected=3

Explanation

The virus trajectory starts from (0,0) and crosses (1,1) (2,2) (5,5). At (5,5) we have a citizen of type c causing the virus trajectory to be rotated by 90 degrees clockwise. It moves until the next citizen in its path is encountered at (8,2) of type a causing the virus trajectory to be rotated by 90 degree anti clockwise. It continues on its path till it reaches the next human in its path at (10,4) of type a Virus trajectory is again rotated by 90 degrees clockwise until it hits the boundary at (6,8). Since this is the first time that the virus hits the boundary, it rotates by 90 degrees anticlockwise to reenter the city. The trajectory then continues towards (9,5) (8,6) (7,7) (6,8) and renters the city by rotating the trajectory by 90 degrees anti clockwise to follow the trajectory (5,7) (4,6) (3,5) (2,4) (1,3) (0,2).

At (0,2) it again hits the boundary and since this is the second time the virus hits the boundary, the virus is destroyed. So along its trajectory starting from (0,0) it has infected 3 citizens at location (5,5) (10,4) (8,2). The other 2 citizens who did not come in the virus trajectory are deemed to be safe.