import random
n=random.randint(1,100)
a=-1
count=0
while a!=n:
    a=int(input("Enter your guess: "))
    if a==n:
        print("Bingo! You are correct")
        break
    elif a>n:
        print("Think lower!")
    else :
        print("Think higher!")
    
    count+=1

print(f"Number of guesses are: {count}")
