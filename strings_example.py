first_name = "Gabriela"
last_name = "Mendes"
full_name = f"{first_name} {last_name}"
print(full_name.upper())


# Formato antigo do format strings(abaixo da versao 3.6)
dog_1 = "Kirica"
dog_2 = "Dollyca"
dogs_names= "{} {}".format(dog_1, dog_2)
print(dogs_names)

#Whitespaces and newlines

print("\nPython3")
print("Languages:\nPython\nC\nJavascript")
print("Languages:\n\tPython\n\tC\n\tJavascript")

# Removing extra spaces
favorite_language="Python "
favorite_language = favorite_language.rstrip()
print(favorite_language)
