answer=input( " whats the answer of the great  quastion of life, the Universe , and Everything ?").lower().strip()
str="forty-two"
if answer.isdigit():
    if answer=="42" :
        print("yes")
    else:
       print("no")
else:
    if answer== str or answer==str.replace("-"," "):
     print("Yes")
    else:
       print("no")
