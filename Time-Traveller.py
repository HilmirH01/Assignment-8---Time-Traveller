def x(x):
    return x+1
def ussilon(y):
    return y+1

TRAVEL_STR = "You can travel: "
DIRECTION_N = "(N)orth"
DIRECTION_S = "(S)outh"
DIRECTION_E = "(E)ast"
DIRECTION_W = "(W)est"

def n(y):
    return ussilon(y)


tile_1_1_dir = (TRAVEL_STR + DIRECTION_N)
tile_1_2_dir = (TRAVEL_STR + DIRECTION_N + " or " + DIRECTION_E + " or " + DIRECTION_S)
destination_e = (TRAVEL_STR + DIRECTION_E)
destination_w = (TRAVEL_STR + DIRECTION_W)
dir_input = input("Direction: ")

while x != 3 or y != 1:
    if x == 1 and y == 1:
        print(tile_1_1_dir + ".")
        dir_input
        if dir_input == "n" or dir_input == "N":
            n(1)
            print(x,n)
            dir_input = input("Direction: ")
        else:
            print("Not a valid direction!")
    elif x == 1 and y == 2:
        print(tile_1_2_dir)
        dir_input
        if dir_input == "n" or dir_input == "N":
            n(1)
            print(x,y)
        elif dir_input == "e" or dir_input == "N":
            y -= 1