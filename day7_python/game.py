import random as rd

num=rd.randint(1,100)
chances=10
while chances>0:
    choice=int(input("Guess The Number:"))
    if choice<num:
        print(f'you guessed too low!! , You have only{chances} available')
    elif choice>num:
        print(f'you guessed too high !! , You have only{chances} available')
    else:
        print("congratulations bro , you have EVM!!!")
        break
    chances-=1