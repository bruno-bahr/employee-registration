from employees import Employee
import login


login.login()


print("---EMPLOYEES' REGISTRATION MODULE---")
print('')
print('Choose an option below to continue:')
print('1 - List of registered employees')
print('2 - Register new employee')
print('3 - Remove employee')
print('4 - Update registration')
print('5 - Finish program')

option = int(input('Enter your option: '))

while option != 5:
    if option == 1:
        Employee.listar()
    if option == 2:
        Employee.cadastrar(cls=Employee)
    if option == 3:
        Employee.excluir()
    if option == 4:
        Employee.alterar()
    print('')
    print('1 - List of employees   2 - Register   3 - Remove   4 - Update   5 - Finish section')
    option = int(input('Enter your option: '))
    print('')

if option == 5:
    print('PROGRAM FINISHED!')
    exit()
