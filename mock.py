users = (
    ('Matheus', 1010),
    ('Bruno', 1312),
)

u = input('User: ')
p = int(input('Password: '))

for n, s in users:
    print(u, n)
    print(p, s)
    if u == n and p == s:
        print("Ok")
    else:
        print("Data don't match")

