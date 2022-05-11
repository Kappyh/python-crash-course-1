# 3.4 Guest list
wanted_people_guest_list = ['Lidia', 'Warley', 'Lucas']
print(f'{wanted_people_guest_list[0]} will be nice if you could have dinner here\n')
print(f'{wanted_people_guest_list[-1]} will be nice if you could have dinner here\n')
print(f'{wanted_people_guest_list[1]}'
      f' I wish you to be alive to have dinner with mom and me')

# 3.5 changing the guest list
print(f'{wanted_people_guest_list[1]} cant come to dinner')
wanted_people_guest_list.remove('Warley')
wanted_people_guest_list.insert(1,'Sky')
print(f'{wanted_people_guest_list[0]} you are invited for dinner tonight')
print(f'{wanted_people_guest_list[1]} you are invited for dinner tonight')
print(f'{wanted_people_guest_list[-1]} you are invited for dinner tonight\n')

# 3.6 More guests
print(f'{wanted_people_guest_list[0]} I found a bigger dinner table')
print(f'{wanted_people_guest_list[1]} I found a bigger dinner table')
print(f'{wanted_people_guest_list[-1]} I found a bigger dinner table\n')

wanted_people_guest_list.insert(0, 'Rodolpho')
wanted_people_guest_list.insert(3, 'Lella')
wanted_people_guest_list.append('Kira')

print(wanted_people_guest_list)

print(f'{wanted_people_guest_list[0]} you are invited for dinner tonight in a biggest table')
print(f'{wanted_people_guest_list[1]} you are invited for dinner tonight in a biggest table')
print(f'{wanted_people_guest_list[2]} you are invited for dinner tonight in a biggest table')
print(f'{wanted_people_guest_list[3]} you are invited for dinner tonight in a biggest table')
print(f'{wanted_people_guest_list[4]} you are invited for dinner tonight in a biggest table')
print(f'{wanted_people_guest_list[-1]} you are invited for dinner tonight in a biggest \n')

# 3.7 Shrinking the guest list
print('Sorry guys, the table is not ready yet. So I only can invite 2 people')
deleted_guest_1 = wanted_people_guest_list.pop(1)
print(f'So sorry, you not come for the dinner tonigh {deleted_guest_1}')
deleted_guest_2 = wanted_people_guest_list.pop(-1)
print(f'So sorry, you not come for the dinner tonigh {deleted_guest_2}')
deleted_guest_3 = wanted_people_guest_list.pop(-1)
print(f'So sorry, you not come for the dinner tonigh {deleted_guest_3}')
deleted_guest_4 = wanted_people_guest_list.pop(1)
print(f'So sorry, you not come for the dinner tonigh {deleted_guest_4}\n')
print(f'{wanted_people_guest_list[0]} still have dinner with me tonight')
print(f'{wanted_people_guest_list[1]} still have dinner with me tonight')

del wanted_people_guest_list[0]
del wanted_people_guest_list[0]
print(wanted_people_guest_list)
