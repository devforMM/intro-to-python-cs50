

def main():
 while True:
    fuel_level=input("Fraction: ")
    fraction=convert(fuel_level)
    resultat=gauge(fraction)
    print(resultat)
    break




def convert(fraction):
  try:
    fraction=fraction.split("/")
    x=int(fraction[0])
    y=int(fraction[1])
    z=int((x/y)*100)
    return z
  


def gauge(percentage):
    if percentage<1:
      return "E"
    elif percentage>=99:
      return "F"
    else:
      return f"{percentage}%"



if __name__ == "__main__":
    main()


