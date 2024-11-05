room_descritions =[
       ["A", "B", "C", "D", "E"],
       ["F", "G", "H", "I", "J"],
       ["K", "L", "M", "N", "O"],
       ["P", "Q", "R", "S", "T"],
       ["U", "V", "W", "X", "Y"]
]

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

room_exits =[

    [(False, False, True, False), (False, True, False, False), (False, True, True, True), (False, True, True, True), (False, False, True, True)],
    [(True, False, True, False), (False, True, True, False), (True, True, True, True), (True, False, False, True), (True, False, True, False)],
    [(True, False, True, False), (True, False, False, False), (True, False, True, False), (False, True, False, False), (True, False, True, True)],
    [(True, False, True, False), (False,True, True, False), (True, True, False, True), (False, True, False, False), (True, False, True, False)],
    [(True, True, False, False), (True, False, False, True), (False, False, False, False), (True, False, False, False), (False, False, True, False)]


]





position =(2,2)


x, y = position
description=room_descritions[y][x]
print(position, ":", description)



while(True):

 

    print("What now?")
    command = input()

   
    if command == "north":
        if(room_exits[y][x][NORTH]):
            print("You move north....")
            y = y -1
        else:
            print("Cant move north!")
    elif command == "south":
        if(room_exits[y][x][SOUTH]):
            print("You move south....")
            y= y + 1
        else:
            print("Cant move south!")
    elif command == "east":
        if(room_exits[y][x][EAST]):
            print("You move east....")
            x= x + 1
        else:
            print("Cant move east!")
    elif command == "west":
        if(room_exits[y][x][WEST]):
            print("You move west....")
            x= x - 1
        else:
            print("Cant move west!")
    elif command == "Goodbyes":
        break

    else:
        print("I dont understand" + command)
position=(x,y)