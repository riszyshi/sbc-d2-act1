from random import randint


print("THIS IS HUMPYANG GAME!")
Player_1 = int(input("Choose [0.FOLD OR 1.UNFOLD]: "))
if Player_1 == 0:
    Player_1 = "FOLD"
    print("Player_1: FOLD")
elif Player_1 == 1:
    Player_1 = "UNF0LD"
    print("Player_1: UNFOLD")

PC_2 = randint(0, 1)
if PC_2 == 0:
    PC_2 = "FOLD"
    print("Player_Comp2: FOLD")
elif PC_2 == 1:
    PC_2 = "UNF0LD"
    print("Player_Comp2: UNFOLD")


PC_3 = randint(0, 1)
if PC_3 == 0:
    PC_3 = "FOLD"
    print("Player_Comp3: FOLD")
elif PC_3 == 1:
    PC_3 = "UNF0LD"
    print("Player_Comp3: UNFOLD")



if Player_1 and PC_2 and PC_3 == 1 or Player_1 and PC_2 and PC_3 == 0:
    print("Draw!")
elif Player_1 == 1 and PC_2 == 0 and PC_3 == 0:
    print("You Won")
elif Player_1 == 0 and PC_2 == 1 and PC_3 == 0:
    print("Player Computer 2 Won")
elif Player_1 == 0 and PC_2 == 0 and PC_3 == 1:
    print("Player Computer 3 Won")