
def login():
    c = 3
    users = (
        ('Matheus', '1010'),
        ('Bruno', '1312'),
    )
    while c > 0:
        c -= 1
        u = input('User: ')
        p = input('Password: ')
        cont = 0
        isGranted = False

        for n, s in users:
            if u == n and p == s:
                isGranted = True
                break
            else:
                cont += 1
                continue

        if not isGranted:
            if cont != 1:
                if c == 0:
                    print('***Number of attempts exceeded!***')
                    print('Contact the IT department if you forgot your username/password.')
                    exit()
                else:
                    print(f'Invalid data! You have {c} attempts left.')
            continue
        print(f'Welcome, {n}!')
        break


