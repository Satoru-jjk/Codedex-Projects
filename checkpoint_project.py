import random 
system=random.randint(1,3)


print("Rock Paper Scisor Game")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
choice=int(input("Choose a number:"))

if choice==1 and system==1:
    print("Playe choice:✊")
    print("CPU choice:✊")
    print("It's Tie!!")
elif choice==1 and system==2:
    print("Player choice:✊")
    print("CPU choice:✋")
    print("CPU won")
elif choice==1 and system==3:
    print("Player choice:✊")
    print("CPU choice:✌️")
    print("Player won!!")
elif choice==2 and system==1:
    print("Player choice:✋")
    print("CPU choice:✊")
    print("Player won!!")
elif choice==2 and system==2:
    print("Player choice:✋")
    print("CPU choice:✋")
    print("It's a Tie!!!")
elif choice==2 and system==3:
    print("Player choice:✋")
    print("CPU choice:✌️")
    print("CPU win!!")
elif choice==3 and system==1:
    print("Player choice:✌️")
    print("CPU choice:✊")
    print("CPU wins!!")
elif choice==3 and system==2:
    print("Player choice:✌️")
    print("CPU choice:✋")
    print("Player won!!")
elif choice==3 and system==3:
    print("Player choice:✌️")
    print("CPU choice:✌️")
    print("It's a Tie!!")
else:
    print("Please Enter a valid option")