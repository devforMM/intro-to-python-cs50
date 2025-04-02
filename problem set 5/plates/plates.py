import string

def is_valid(plaque):
    longeur_plaque = len(plaque)

    alphabets = string.ascii_uppercase
    numeros = string.digits
    co1 = 0
    co2 = 0


    for char in plaque:
        if char not in alphabets and char not in numeros:
            co1 += 1


    if not (2 <= longeur_plaque <= 6):
        return False


    for char in plaque[:2]:
        if char not in alphabets:
            return False


    for i in range(longeur_plaque):
        if plaque[i] in numeros and 1 <= i < longeur_plaque - 1:
            if plaque[i+1] in alphabets and plaque[i-1] in alphabets:
                co2 += 1
            if plaque[i] == "0" and plaque[i-1] in alphabets:
                return False

    compteur_final = co2 + co1

    if compteur_final == 0:
        return True
    else:
        return False

def main():
    s = input("Plate: ")
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")

main()
