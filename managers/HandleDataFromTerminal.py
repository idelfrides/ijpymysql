
class HandleDataFromTerminal(object):
    """
        This object (class) going to help you to entry data
        to general app from Run Terminal. It is accept
        to entry one or many records to the table at the
        same time.
    """

    def __init__(self):
        self.module_information()

    
    def data_from_terminal(self):        
        print(' ---------------------------'
              '\n\t INFORM DATA FOR ONE DEV '
              '\n ---------------------------\n')
        name = input('\n Enter a name:  ')
        company = input('\n Enter a company:  ')
        salary = float(input('\n Entry a salary:  '))
        role = input('\n Enter a funcao:  ')
        adress = input('\n Enter a adress:  ')

        data = list()

        data.append(name)
        data.append(company)
        data.append(salary)
        data.append(role)
        data.append(adress)

        #        name, company, salary, role, adress
        # return name, company, salary, funcao, adress
        return data


    def data_from_terminal_many(self):        
        print(' ---------------------------'
              '\n INFORM DATA FOR MANY DEV '
              '\n ---------------------------')
        records = self.define_records_number() 
        dev_data = list()
        for ind in range(records):
            print('\n--------------------------------')
            print('\t DATA FOR DEV {}'.format(ind+1))
            print('--------------------------------\n')
            
            name = input('\n Entry the name:  ')
            company = input('\n Entry the company:  ')
            salary = float(input('\n Entry the salary:  '))
            role = input('\n Entry the role:  ')
            adress = input('\n Entry the adress:  ')

            dev_data.append(name)
            dev_data.append(company)
            dev_data.append(salary)
            dev_data.append(role)    # função = role
            dev_data.append(adress)
            
        return dev_data

    
    def define_records_number(self):        
        yes_n = False
        while yes_n is False:
            n = int(input('\n Entry a amount of dev (n > 1):  '))
            if n >= 2:
                yes_n = True
            elif n < 2:
                print("\n WARNING: \n Amount is INVALID!")
                yes_n = False
            else:
                pass

        return n


    def module_information(self):
        info = 'This module going to help you to entry data to \n this app' \
               'from terminal. It is accept to entry one or many \n developers at the same time.'

        print('\n ------------------------------------------------'
              '\n MODULE INFORMATION -> HANDLE DATA VIA TERMINAL'
              '\n ------------------------------------------------'
              '\n {}'.format(info))
        print('\n ------------------------------------------------\n')
    

