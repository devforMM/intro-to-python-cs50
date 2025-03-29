import inflect
inflect_obj=inflect.engine()
noms=[]
message="Adieu, adieu, to "
while True:
  try:
    nom=input("Name: ")
    noms.append(nom.title())
  except EOFError:
    break

if len(noms)==1:
  message+=noms[0]
  print(message)
else:
  reste=inflect_obj.join(noms)
  message+=reste
  print(message)
