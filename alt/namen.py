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