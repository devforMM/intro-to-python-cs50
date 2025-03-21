def main():
    time=input("what time is it ? ").strip()
    if convert("7:00")<=convert(time)<=convert("8:00"):
       print("breakfast time")
    elif convert("12:00")<=convert(time)<=convert("13:00"):
       print("lunch time")
    elif convert("18:00")<=convert(time)<=convert("19:00"):
       print("dinner time ")


def convert(time):
 hour,minute=time.split(":")
 hour=float(hour)
 minute=float(minute)
 if minute==0:
    converted_time=hour
    return converted_time
 else:
    minutes=minute/60
    converted_time=hour+minutes
    return converted_time
if __name__ == "__main__":
    main()
