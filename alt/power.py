name="kek"
age="23"
country="Deutschland"
result=None

result="Hallo, mein Name ist "+name+", ich bin "+age+" Jahre alt und komme aus "+country #Variable überschrieben
print(result)

result1="Hallo, mein Name ist "+name+", ich bin "+age+" Jahre alt und komme aus "+country #in Variable geschrieben
print(result1)

result2=f"Hallo, mein Name ist {name}, ich bin {age} Jahre alt und komme aus {country}" #in string Variable geschrieben
print(result2)

print("Hallo, mein Name ist "+name+", ich bin "+age+" Jahre alt und komme aus "+country) #direkt geprintet