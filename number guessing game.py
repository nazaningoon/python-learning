secret=19
attempts=0
print("Number Guessing Game")
print("Im thinking of a Number between 1 and 100 !")

while True:
    guess=int(input("guess a number : "))
    attempts+=1
    if guess==secret:
        print(f"correct! you got it in {attempts} attempts. ")
        break
    if guess <secret:
        print("guess higher !: ")
        
    else:
        print("guess lower!: ")
        
