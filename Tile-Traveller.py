x = 1
y = 1


#Fastar fyrir strengi
TRAVEL_STR = "You can travel:"
DIRECTION_N = " (N)orth"
DIRECTION_S = " (S)outh"
DIRECTION_E = " (E)ast"
DIRECTION_W = " (W)est"
ERROR_DIR = "Not a valid direction!" #For when the user inputs an impossible direction.
OR_STR = " or"
DOT_STR = "."

#Breytur sem inniheldur strengina með áttunum.
tile_1_1_dir = (TRAVEL_STR + DIRECTION_N + DOT_STR)
tile_1_2_dir = (TRAVEL_STR + DIRECTION_N + OR_STR + DIRECTION_E + OR_STR + DIRECTION_S + DOT_STR)
tile_1_3_dir = (TRAVEL_STR + DIRECTION_E + OR_STR + DIRECTION_S + DOT_STR)
tile_2_1_dir = (TRAVEL_STR + DIRECTION_N + DOT_STR)
tile_2_2_dir = (TRAVEL_STR + DIRECTION_S + OR_STR + DIRECTION_W + DOT_STR)
tile_2_3_dir = (TRAVEL_STR + DIRECTION_E + OR_STR + DIRECTION_W + DOT_STR)
tile_3_3_dir = (TRAVEL_STR + DIRECTION_S + OR_STR + DIRECTION_W + DOT_STR)
tile_3_2_dir = (TRAVEL_STR + DIRECTION_N + OR_STR + DIRECTION_S + DOT_STR)
winning_tile_3_1 = "Victory!"


while x != 3 or y != 1:
    #Starting tile 1,1    
    if x == 1 and y == 1:
        print(tile_1_1_dir)
        dir_input = input("Direction: ")
        if dir_input == "n" or dir_input == "N":
            y += 1
        else:
            print(ERROR_DIR)

#When entering tile 1,2    
    if x == 1 and y == 2:
        print(tile_1_2_dir)
        dir_input = input("Direction: ")
        if dir_input == "n" or dir_input == "N":
            y += 1
        elif dir_input == "e" or dir_input == "E":
            x += 1 
        elif dir_input == "s" or dir_input == "S":
            y -= 1
        else:
            print(ERROR_DIR)

#When entering tile 1,3
    if x == 1 and y == 3:
        print(tile_1_3_dir)
        dir_input = input("Direction: ")
        if dir_input == "s" or dir_input == "S":
            y -= 1
        elif dir_input == "e" or dir_input == "E":
            x += 1
        else:
            print(ERROR_DIR)

#When entering tile 2,1
    if x == 2 and y == 1:
        print(tile_2_1_dir)
        dir_input = input("Direction: ")
        if dir_input == "n" or dir_input == "N":
            y += 1
        else:
            print(ERROR_DIR)

#When entering tile 2,2
    if x == 2 and y == 2:
        print(tile_2_2_dir)
        dir_input = input("Direction: ")
        if dir_input == "s" or dir_input == "S":
            y -= 1
        elif dir_input == "w" or dir_input == "S":
            x -= 1
        else:
            print(ERROR_DIR)

#When entering tile 2,3
    if x == 2 and y == 3:
        print(tile_2_3_dir)
        dir_input = input("Direction: ")
        if dir_input == "w" or dir_input == "W":
            x -= 1
        elif dir_input == "e" or dir_input == "E":
            x += 1
        else:
            print(ERROR_DIR)

#When entering tile 3,3
    if x == 3 and y == 3:
        print(tile_3_3_dir)
        dir_input = input("Direction: ")
        if dir_input == "w" or dir_input == "W":
            x -= 1
        elif dir_input == "s" or dir_input == "S":
            y -= 1
        else:
            print(ERROR_DIR)

#When entering tile 3,2
    if x == 3 and y == 2:
        print(tile_3_2_dir)
        dir_input = input("Direction: ")
        if dir_input == "n" or dir_input == "N":
            y += 1
        elif dir_input == "s" or dir_input == "S":
            y -= 1
        else:
            print(ERROR_DIR)

#When entering tile 3,1
    if x == 3 and y == 1:
        print(winning_tile_3_1) #Prints out the winning message, and goes to the top of the while loop
                                #and ends because the condition is no longer met. 






#def tile_1_1(direction):
    #x = 1 
    #y = 1
    #print(tile_1_1_dir + ".")
    #direction = input("Direction: ")
    #if direction == "n" or direction == "N":
        #y += 1
        #x += 0
    #else:
        #print(ERROR_DIR)
    #return direction

#print(tile_1_1("n"))

    