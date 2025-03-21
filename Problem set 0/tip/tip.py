
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    final=float(d.replace("$",""))
    return final


def percent_to_float(p):
   avant=p.replace("%","")
   final=float("0."+avant)
   return final


main()

