#Python examples with strings

#1 format string
name = "Gabriela"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)

#2 string methods modifying strings
name_2 = "Kira"
print(f"{name_2.lower()}\n{name_2.upper()}\n{name_2.title()}")

#3 String Quotes
message_3 = 'Sir Isac Newton once said, "If I have ever made any valuable discoveries, it has been ' \
            'due more to patient attention, than to any other talent."\n'
print(message_3)

#4 String Quotes with format string
famous_author= "Sir Isac Newton"
message_4 = f'{famous_author} once said,"If I have ever made any valuable discoveries, it has been ' \
            'due more to patient attention, than to any other talent."'
print(message_4)

# Striping whitespaces

person_name = "\n Gabriela Mendes\t"
print(f"hi{person_name.strip()}oi")
print(f"hi{person_name.lstrip()}oi")
print(f"hi{person_name.strip()}oi")
