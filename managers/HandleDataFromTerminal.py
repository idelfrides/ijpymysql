
class HandleDataFromTerminal(object):
    """
       -------------------------------------------------------
        This module (class) going to help you to entry data
        to general app by from Run Terminal. It is accept
        to entry one or many records to the table at the
        same time.
       -------------------------------------------------------
    """

    def __init__(self):
        """
           ---------------------------------------------------
             the thunder init method inicialize and show
             the module information to user via terminal by
             calling method 'module_info()'
           ---------------------------------------------------
        """
        self.module_info()

    
    def data_terminal(self):
        """
           ---------------------------------------------------
            This method able user to enter data via terminal.
            It accept just one record by time. Then create
            a list and add all values to it and then return
            the list filled up. This method is called on your
            test a   p module as many times as you want.
           ---------------------------------------------------
        """
        
        print(' ---------------------------'
              '\n\t ENTRY DATA FOR ONE DEV '
              '\n ---------------------------\n')
        name = input('\n Entry a name:  ')
        company = input('\n Entry a company:  ')
        salary = float(input('\n Entry a salary:  '))
        role = input('\n Entry a funcao:  ')
        adress = input('\n Entry a adress:  ')

        data = list()  # create a list called data

        # add all attributes to the list data
        data.append(name)
        data.append(company)
        data.append(salary)
        data.append(role)
        data.append(adress)

        #        name, company, salary, role, adress
        # return name, company, salary, adress, funcao
        return data


    def data_terminal_many(self):
        """
           ---------------------------------------------------
            This method is similar to method 'data_terminal()',
            the only diference from it is about accept many
            records at the same time, the same loop. Is call
            is the    ame like 'data_terminal()' method.
            It call define_n() method to get number of records
            the user going to make.
          ---------------------------------------------------
        """
        
        print(' ---------------------------'
              '\n ENTRY DATA FOR MANY DEV '
              '\n ---------------------------')
        n = self.define_n() # call define_n() method
        dev_data = list()
        for ind in range(n):
            print('\n--------------------------------')
            print('\t DATA FOR DEV {}'.format(ind+1))
            print('--------------------------------\n')
            name = input('\n Entry the name:  ')
            company = input('\n Entry the company:  ')
            salary = float(input('\n Entry the salary:  '))
            role = input('\n Entry the role:  ')
            adress = input('\n Entry the adress:  ')

            # add attributes to the list data
            dev_data.append(name)
            dev_data.append(company)
            dev_data.append(salary)
            dev_data.append(role)    # função = role
            dev_data.append(adress)
            
        return dev_data

    
    def define_n(self):
        """
           ---------------------------------------------------
             This method ask the user to inform the quantity
             o  tuples(records) user goint to enter
             This method is called by 'data_terminal_many()'
              method.
           ---------------------------------------------------
        """
        
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


    def module_info(self):
        """
           --------------------------------------------------
            This method shows the propose of this module.
            That is his information.
            This method is only called by 'thunder init'
            method of this module/class.
           ---------------------------------------------------
        """
        
        # info variable has information of this module
        info = 'This module going to help you to entry data to \n this app' \
               'from terminal. It is accept to entry one or many \n developers at the same time.'

        print('\n ------------------------------------------------'
              '\n MODULE INFORMATION -> HANDLE DATA VIA TERMINAL'
              '\n ------------------------------------------------'
              '\n {}'.format(info))
        print('\n ------------------------------------------------\n')

