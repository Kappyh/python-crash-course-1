# 5.8 e 5.9
users = ['admin', 'lepolepo', 'mazo', 'falb', 'kappyh']
if users:
    for user in users:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for logging in again')
else:
    print('We need some users')