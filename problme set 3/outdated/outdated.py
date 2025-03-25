import string

liste=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

specialchars=string.punctuation.replace("/","")

while True:
 try:
  date=input("Date: ")
  for char in specialchars:
    if char in date:
     date =date.replace(char,"")
  if "/" in date:
   date=date.split("/")
  else:
   date=date.split(" ")





  mois=date[0]

  jour=date[1]

  annee=date[2]
 except IndexError:
   continue



 if not mois.isdigit():
   for num,month in enumerate(liste) :
    if mois==month:
      mois=num+1
 mois=int(mois)
 try:
  jour=int(jour)
 except ValueError:
  continue
 annee=int(annee)


 if 1<=jour<=31 and 1<=mois<=12:
   break


formated_date=f"{annee}-{mois:02}-{jour:02}"
print(formated_date)


