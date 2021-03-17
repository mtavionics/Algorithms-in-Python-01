# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 12:00:11 2021
Project 1
@author: Mikhail Terentev

"""

import random

# initial value
n = 6           # number of creatures
quit = ''
skip = False

dict = {1: 'bear', 2: 'fish', 3: ''}

# Query of # of test
test_river = ''                  # test 1, 2, 3 or 4
test_river = input("Input # of test (1, 2, 3, 4 or 'r' for random): ")
    
# init river
river = []
if test_river == '1':
    # test 1 (a)
    river = [2,3,3,3,3,3]  # 1 - Bear, 2 - Fish, 3 - None
elif test_river == '2':
    # test 2 (b)
    river = [1,3,3,3,3,3]
elif test_river == '3':
    # test 3 (c)
    river = [1,1,2,2,2,2]
elif test_river == '4':
    # test 4 (mine)
    river = [1,3,1,1,2,3]
elif test_river == 'r':
    # random 
    river = [random.randint(1, 3) for _ in range(n)]

while not(quit == 'q'):
    orig_river = [dict[x] for x in river]
      
    # init moves
    if test_river == 'r' or '1' or '2' or '3' or '4':
        moves = [random.randint(-1, 1) for _ in range(n)]   # random moves
    else:   
        print ('Incorrect number. The simulation stoped')
        break

    for cell in range(n):
        
        # 1: current spot is empty, skip move to next or fish is killed and skip
        if river[cell] == 3 or skip == True:
            skip = False
            continue
        
        # 2: out the bound check or move is 0  - stay at same spot, no change
        elif cell + moves[cell] < 0 or cell + moves[cell] > n - 1 or moves[cell] == 0 : 
            continue

        # 3: same creature clash stay as is, then increase size by 1 at end of list with opposite creature
        elif river[cell] == river[cell + moves[cell]] and river[cell] != 3: 
            if dict[river[cell]] == 'bear':
                river.append(2)
            else:
                river.append(1)
            n += 1  # add to end of the list
            
        # 4: bear eat fish
        elif dict[river[cell]] == 'bear' and dict[river[cell + moves[cell]]] == 'fish':
            river[cell + moves[cell]] = river[cell]             # bear move to new spot
            river[cell] = 3                                     # bear ate fish
            if moves[cell] == 1:
                skip = True                                     # bear ate fish, skip next spot

        # 5: fish moved into bear's cell
        elif dict[river[cell]] == 'fish' and dict[river[cell + moves[cell]]] == 'bear':
            river[cell] = 3

        # 6: creature move into empty spot and set original spot as empty
        else:
            river[cell + moves[cell]] = river[cell]
            river[cell] = 3

    print('\n','The initial river list:', '\n', orig_river)
    print('\n','The random moves are: ', '\n', moves)
    new_river = [dict[x] for x in river]
    print('\n','The current river list:', '\n', new_river)
    
    # Query if quit or continue
    quit = input("Press any key to continue, or 'q' for stop simulation ")
    
print ('The simulation stoped')


'''
Output:
    
Input # of test (1, 2, 3, 4 or 'r' for random): 1

 The initial river list: 
 ['fish', '', '', '', '', '']

 The random moves are:  
 [1, 0, -1, 1, 1, 1]

 The current river list: 
 ['', 'fish', '', '', '', '']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['', 'fish', '', '', '', '']

 The random moves are:  
 [-1, 1, 0, 1, 0, 1]

 The current river list: 
 ['', '', 'fish', '', '', '']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['', '', 'fish', '', '', '']

 The random moves are:  
 [1, 1, -1, 0, 0, -1]

 The current river list: 
 ['', 'fish', '', '', '', '']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['', 'fish', '', '', '', '']

 The random moves are:  
 [0, -1, 1, -1, -1, 0]

 The current river list: 
 ['fish', '', '', '', '', '']

Press any key to continue, or 'q' for stop simulation q
The simulation stoped

-------

Input # of test (1, 2, 3, 4 or 'r' for random): 1

 The initial river list: 
 ['fish', '', '', '', '', '']

 The random moves are:  
 [1, 0, -1, 1, 1, 1]

 The current river list: 
 ['', 'fish', '', '', '', '']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['', 'fish', '', '', '', '']

 The random moves are:  
 [-1, 1, 0, 1, 0, 1]

 The current river list: 
 ['', '', 'fish', '', '', '']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['', '', 'fish', '', '', '']

 The random moves are:  
 [1, 1, -1, 0, 0, -1]

 The current river list: 
 ['', 'fish', '', '', '', '']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['', 'fish', '', '', '', '']

 The random moves are:  
 [0, -1, 1, -1, -1, 0]

 The current river list: 
 ['fish', '', '', '', '', '']

Press any key to continue, or 'q' for stop simulation q
The simulation stoped

-------------

Input # of test (1, 2, 3, 4 or 'r' for random): 3

 The initial river list: 
 ['bear', 'bear', 'fish', 'fish', 'fish', 'fish']

 The random moves are:  
 [1, 1, -1, -1, -1, 0]

 The current river list: 
 ['bear', '', 'bear', 'fish', '', 'fish', 'fish']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['bear', '', 'bear', 'fish', '', 'fish', 'fish']

 The random moves are:  
 [0, -1, 0, -1, 0, 1, -1]

 The current river list: 
 ['bear', '', 'bear', '', '', 'fish', 'fish', 'bear', 'bear']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['bear', '', 'bear', '', '', 'fish', 'fish', 'bear', 'bear']

 The random moves are:  
 [0, 0, -1, 0, 0, 1, 0, 0, 1]

 The current river list: 
 ['bear', 'bear', '', '', '', 'fish', 'fish', 'bear', 'bear', 'bear', 'fish']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['bear', 'bear', '', '', '', 'fish', 'fish', 'bear', 'bear', 'bear', 'fish']

 The random moves are:  
 [1, -1, 0, -1, 1, 1, 1, -1, -1, 0, -1]

 The current river list: 
 ['bear', 'bear', '', '', '', 'fish', 'bear', 'bear', '', 'bear', '', 'fish', 'fish', 'bear']

Press any key to continue, or 'q' for stop simulation q
The simulation stoped

-----------

Input # of test (1, 2, 3, 4 or 'r' for random): 4

 The initial river list: 
 ['bear', '', 'bear', 'bear', 'fish', '']

 The random moves are:  
 [-1, 1, 0, 1, 1, 0]

 The current river list: 
 ['bear', '', 'bear', '', 'bear', '']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['bear', '', 'bear', '', 'bear', '']

 The random moves are:  
 [-1, -1, 1, 1, 1, 1]

 The current river list: 
 ['bear', '', '', 'bear', '', '', 'bear']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['bear', '', '', 'bear', '', '', 'bear']

 The random moves are:  
 [-1, -1, 1, 0, -1, 0, 1]

 The current river list: 
 ['bear', '', '', 'bear', '', '', 'bear']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['bear', '', '', 'bear', '', '', 'bear']

 The random moves are:  
 [0, -1, 1, 1, -1, 0, 0]

 The current river list: 
 ['bear', '', '', 'bear', '', '', 'bear']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['bear', '', '', 'bear', '', '', 'bear']

 The random moves are:  
 [1, 1, -1, 1, 1, 0, 1]

 The current river list: 
 ['', 'bear', '', '', '', 'bear', 'bear']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['', 'bear', '', '', '', 'bear', 'bear']

 The random moves are:  
 [1, 0, 1, 0, 1, -1, 0]

 The current river list: 
 ['', 'bear', '', '', 'bear', '', 'bear']

Press any key to continue, or 'q' for stop simulation q
The simulation stoped

-----------

Input # of test (1, 2, 3, 4 or 'r' for random): r

 The initial river list: 
 ['fish', '', '', 'fish', '', '']

 The random moves are:  
 [-1, -1, -1, 1, -1, 0]

 The current river list: 
 ['fish', '', '', 'fish', '', '']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['fish', '', '', 'fish', '', '']

 The random moves are:  
 [-1, -1, 0, 0, 1, -1]

 The current river list: 
 ['fish', '', '', 'fish', '', '']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['fish', '', '', 'fish', '', '']

 The random moves are:  
 [0, -1, -1, 1, 0, 1]

 The current river list: 
 ['fish', '', '', '', 'fish', '']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['fish', '', '', '', 'fish', '']

 The random moves are:  
 [-1, 1, 1, 0, 0, -1]

 The current river list: 
 ['fish', '', '', '', 'fish', '']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['fish', '', '', '', 'fish', '']

 The random moves are:  
 [1, 0, 1, -1, -1, -1]

 The current river list: 
 ['', 'fish', '', 'fish', '', '']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['', 'fish', '', 'fish', '', '']

 The random moves are:  
 [-1, 0, -1, -1, -1, 0]

 The current river list: 
 ['', 'fish', 'fish', '', '', '']

Press any key to continue, or 'q' for stop simulation 
The simulation stoped

------------

Input # of test (1, 2, 3, 4 or 'r' for random): r

 The initial river list: 
 ['bear', '', 'fish', 'bear', '', '']

 The random moves are:  
 [0, 0, -1, 1, 1, -1]

 The current river list: 
 ['bear', 'fish', '', '', 'bear', '']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['bear', 'fish', '', '', 'bear', '']

 The random moves are:  
 [1, 0, 0, 1, 0, 0]

 The current river list: 
 ['', 'bear', '', '', 'bear', '']

Press any key to continue, or 'q' for stop simulation 

 The initial river list: 
 ['', 'bear', '', '', 'bear', '']

 The random moves are:  
 [-1, 0, 0, 1, -1, 0]

 The current river list: 
 ['', 'bear', '', 'bear', '', '']

Press any key to continue, or 'q' for stop simulation q
The simulation stoped


'''        