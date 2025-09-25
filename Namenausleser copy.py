name = input("Was ist dein Name? -->> ")

user =	{
  "top": "12",
  "kek": "65",
  "lul": "25"
}

if name in user:
    alter=user[name]
    print("Der Name ist "+name+" und du bist "+alter)
else:
    print("Dich gibts nicht") 




#neuer code


name = input("Was ist dein Name? -->> ")

user =	{
    "top": "12",
    "kek": "65",
    "lul": "25"
    }

while name != "exit":

    if name in user:
       alter=user[name]
       print("Der Name ist "+name+" und du bist "+alter)
    else:
      #print("Dich gibts noch nicht")
      alter = input("Dich gibts noch nicht.Wie alt bist du? -->> ")
      user.update({name:alter})
    name = input("Was ist dein Name? -->> ")