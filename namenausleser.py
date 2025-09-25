name = input("Was ist dein Name? -->> ")

import json

#öffnet userdata und schreibt es in ein dictionary
with open("userdata.json", "r") as tabelle:
   user = json.load(tabelle)

#loopt die Eingabe bis man exit eingibt
while name != "exit":

    if name in user:
       alter=user[name]
       print("Der Name ist "+name+" und du bist "+alter)
    else:
      alter = input("Dich gibts noch nicht.Wie alt bist du? -->> ")
      user.update({name:alter})

      #öffnet userdata zum reinschreiben
      with open("userdata.json", "w") as tabelle:
         json.dump(user, tabelle, indent=4, ensure_ascii=False)

    name = input("Was ist dein Name? -->> ")