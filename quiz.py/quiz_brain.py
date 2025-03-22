co=0
n=0
def remarque(co):
    if co==10:
        print(f"you got {co} exelent")
    elif 5<co<10:
        print(f"you got {co} good")
    elif co==5:
        print(f"you got {co} average")
    elif 0<co<5:
        print(f"you got {co} bad")
    else:
        print(f"you got {co} you are a donkey")


