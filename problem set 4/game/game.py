import random
while True:
    level=input("Level")
    if level.isdigit():
        level=int(level)
        if level>0:
            break
    else:
        continue

random_intger=random.randint(1,level)

while True:
  guess=input("Guess: ")
  if guess.isdigit:
    guess=int(guess)
    if guess==random_intger:
        print("Just right!")
        break
    elif guess<random_intger:
        print("Too small!")
    else:
        print("Too large!")
  else:
      continue
