# 5.10
current_users = ['admin', 'kappyh', 'john', 'marie', 'donald']
new_users = ['kappyh', 'john', 'tom', 'jerry', 'eleven']

for new_user in new_users:
    if new_user.lower() in current_users:
        print('This user already exists, create a new one')
    else:
        print(f"New user create for {new_user}")

# 5.11

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ordinal_list = []
for number_list in numbers_list:
    if number_list == 1:
        ordinal_list.append(f'{number_list}st')
    elif number_list == 2:
        ordinal_list.append(f'{number_list}nd')
    elif number_list == 3:
        ordinal_list.append(f'{number_list}rd')
    else:
        ordinal_list.append(f'{number_list}th')

print(f"{ordinal_list}")