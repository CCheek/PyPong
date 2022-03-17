import Two_Player_Pong
import AI_Pong
import init

print("Welcome to Pong!")
print("Would you like to play:")
print("A. Single Player")
print("Or...")
print("B. Two Players")
x = input("Please select you mode. Type A or B to choose: ")
init.init()

if x == "A":
    AI_Pong.mainloop()
elif x == "B":
    Two_Player_Pong.mainloop()