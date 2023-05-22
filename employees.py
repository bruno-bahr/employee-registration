
class Employee:
    list = []
    id_f = 0

    def __init__(self, id_f, nome, sobrenome, cpf, dpto):
        self.id_f = id_f
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.dpto = dpto

    @classmethod
    def listar(cls):
        if (len(cls.list)) == 0:
            return print('List of employees is empty!')
        print('')
        print('***LIST OF REGISTERED EMPLOYEES ***')
        for i in range(len(cls.list)):
            f = cls.list[i]
            print(f'Id: {f.id_f} | Name: {f.nome} {f.sobrenome} | CPF: {f.cpf} | Departament: {f.dpto}')
        print('')

    @classmethod
    def cadastrar(self, cls):
        self.id_f += 1
        self.nome = input('Name: ')
        self.sobrenome = input('Last name: ')
        self.cpf = input('CPF: ')
        self.dpto = input('Departament: ')

        func = Employee(self.id_f, self.nome, self.sobrenome, self.cpf, self.dpto)
        if len(cls.list) == 0:
            cls.list.append(func)
        else:
            for i in range(len(cls.list)):
                f = cls.list[i]
                if self.cpf != f.cpf:
                    cls.list.append(func)
                else:
                    print('CPF already taken!')
                return cls.list

    @classmethod
    def excluir(cls):
        if len(cls.list) != 0:
            id_f = int(input('Enter the id of the employee you want to delete: '))
            for i in range(len(cls.list)):
                f = cls.list[i]
                if id_f == f.id_f:
                    conf = input(f'Confirm the exclusion of employee {f.nome.upper()}? Y|N: ')
                    if conf in 'Yy':
                        print(f'Employee {f.nome} {f.sobrenome} was removed from the database.')
                        cls.list.remove(cls.list[i])
                        return cls.list
                    else:
                        print('Invalid option!')
                        break
            else:
                print('ID not found!')
        elif len(cls.list) == 0:
            print('List of employees is empty!')


    @classmethod
    def alterar(cls):
        if len(cls.list) != 0:
            id = int(input('Enter the employee id to continue: '))
            for i in range(len(cls.list)):
                f = cls.list[i]
                if id == f.id_f:
                    print(f'Employee selected: {f.nome} {f.sobrenome}')
                    print('---Choose one of the options below---')
                    print('1 - Update name')
                    print('2 - Update last name')
                    print('3 - Update CPF')
                    print('4 - Update departament')
                    print('5 - Main menu')
                    option = int(input('Enter your option: '))
                    if option == 1:
                        nome = input('Update name to: ')
                        f.nome = nome
                        print(f'Name updated with success!')
                    if option == 2:
                        sobrenome = input('Update last name to: ')
                        f.sobrenome = sobrenome
                        print('Last name updated with success!')
                    if option == 3:
                        cpf = input('Update CPF to: ')
                        f.cpf = cpf
                        print('CPF updated with success!')
                    if option == 4:
                        dep = input('Update department to: ')
                        f.dpto = dep
                        print('Departament updated with success!')
                    if option == 5:
                        print('Returning to main menu')
                        break
                    return cls.list
            else:
                print('No employees identified with this id. ')
        else:
            print('List of employees is empty!')