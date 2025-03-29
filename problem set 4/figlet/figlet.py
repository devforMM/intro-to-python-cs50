from pyfiglet import Figlet
import random
import sys


figlet=Figlet()


if len(sys.argv)<2:
 user=input("Input:")
 fonts=figlet.getFonts()
 r_font=random.choice(fonts)
 font=figlet.setFont(font=r_font)
 print(f"Output:{figlet.renderText(user)}")
elif 2<len(sys.argv)<4:

 if sys.argv[1]=="-f" or sys.argv[1]=="--font":
  font=sys.argv[2]
  if font not in figlet.getFonts():
   sys.exit
  else:
   user=input("Input:")
   font=figlet.setFont(font=font)
   print(f"Output:{figlet.renderText(user)}")
else:
 sys.exit
