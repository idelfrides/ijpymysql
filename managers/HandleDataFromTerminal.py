
from textwrap import dedent
import time, re


class DataFromTerminal(object):
    """
        This object (class) going to help you to entry data
        to general app from Run Terminal. It is accept
        to entry one or many records to the table at the
        same time.
    """

    def __init__(self):
        self.sleep = 7
        self.module_information()

    def data_from_terminal(self):
        print(' ------------------------------'
              '\n\t INFORMING DATA FOR ONE DEV '
              '\n ------------------------------\n')
        try:
            name = input('\n Enter a name:  ')
        except KeyboardInterrupt as kbi_exc:
            print('\n Program interrupted by user\n {}'
                .format(kbi_exc)
            )
            exit(0)
        else:
            if not self.attrib_validation(name, 'alpha'):
                self.show_warning('name')
                self.data_from_terminal()           

        try:
            company = input('\n Enter a company:  ')
        except KeyboardInterrupt as kbi_exc:
            print('\n Program interrupted by user \n {}'
                .format(kbi_exc)
            )
            exit(0)
        else:
            if not self.attrib_validation(company, 'alpha'):
                self.show_warning('company')
                self.data_from_terminal()  

        try:
            salary = float(input('\n Entry a salary:  '))
        except KeyboardInterrupt as kbi_exc:
            print('\n Program interrupted by user \n {}'
                .format(kbi_exc)
            )
            exit(0)
        else:
            if not self.attrib_validation(salary, 'numeric'):
                self.show_warning('salary')
                self.data_from_terminal()

        try:
            role = input('\n Enter a role:  ')
        except KeyboardInterrupt as kbi_exc:
            print('\n Program interrupted by user \n {}'
                .format(kbi_exc)
            )
            exit(0)
        else:
            if not self.attrib_validation(role, 'alpha'):
                self.show_warning('rola')
                self.data_from_terminal()

        try:
            adress = input('\n Enter a adress:  ')
        except KeyboardInterrupt as kbi_exc:
            print('\n Program interrupted by user \n {}'
                .format(kbi_exc)
            )
            exit(0)
        else:
            if not self.attrib_validation(adress, 'alphanum'):
                self.show_warning('adress')
                self.data_from_terminal()

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
        print(' ------------------------------'
              '\n INFORMING DATA FOR MANY DEV '
              '\n ------------------------------')
        records = self.define_records_number() 
        dev_data = list()
        for ind in range(records):
            print('\n--------------------------------')
            print('\t DATA FOR DEV {}'.format(ind+1))
            print('--------------------------------\n')
            
            try:
                name = input('\n Enter a name:  ')
            except KeyboardInterrupt as kbi_exc:
                print('\n Program interrupted by user\n {}'
                    .format(kbi_exc)
                )
                exit(0)
            else:
                if not self.attrib_validation(name, 'alpha'):
                    self.show_warning('name')
                    self.data_from_terminal_many() 
             
            try:
                company = input('\n Entry the company:  ')
            except KeyboardInterrupt as kbi_exc:
                print('\n Program interrupted by user\n {}'
                    .format(kbi_exc)
                )
                exit(0)
            else:
                if not self.attrib_validation(company, 'alpha'):
                    self.show_warning('company')
                    self.data_from_terminal_many() 
           
            try:
                salary = float(input('\n Entry the salary:  '))
            except KeyboardInterrupt as kbi_exc:
                print('\n Program interrupted by user\n {}'
                    .format(kbi_exc)
                )
                exit(0)
            else:
                if not self.attrib_validation(salary, 'numeric'):
                    self.show_warning('salary')
                    self.data_from_terminal_many() 

           
            try:
                role = input('\n Entry the role:  ')
            except KeyboardInterrupt as kbi_exc:
                print('\n Program interrupted by user\n {}'
                    .format(kbi_exc)
                )
                exit(0)
            else:
                if not self.attrib_validation(role, 'alpha'):
                    self.show_warning('role')
                    self.data_from_terminal_many() 

            
            try:
                adress = input('\n Entry the adress:  ')
            except KeyboardInterrupt as kbi_exc:
                print('\n Program interrupted by user\n {}'
                    .format(kbi_exc)
                )
                exit(0)
            else:
                if not self.attrib_validation(adress, 'alphanum'):
                    self.show_warning('adress')
                    self.data_from_terminal_many() 
            
            dev_data.append(name)
            dev_data.append(company)
            dev_data.append(salary)
            dev_data.append(role)
            dev_data.append(adress)
            
        return dev_data

    def define_records_number(self):
        max_amount = 100        
        yes_n = False
        while yes_n is False:
            input('\n Amount of dev be bnetween 2 <= n <= %d', max_amount)
            try:
                devs = int(input('\n Enter amount of dev:   '))
            except KeyboardInterrupt as kbi_exc:
                print('\n Program interrupted by user {}'
                    .format(kbi_exc)
                )
                time.sleep(self.sleep)
                exit(0)
            except Exception as excep:
                print('*'*60)
                print(dedent("""
                    ======= WARNING ========
                    
                    Invalid value!!!
                    You entered a caracter --> {}
                    
                    server said: {}                
                      
                    """.format(devs, excep))
                )                
                print('*'*60)
                time.sleep(7)
            else:
                if devs >= 2:
                    yes_n = True
                    break
                if devs < 2:
                    print(dedent("""
                            WARNING:
                        Amount is INVALID.
                        It is out of bound!
                    """))
                    yes_n = False
                if devs > max_amount:
                    print(dedent("""
                            WARNING:
                        Amount is INVALID.
                        It is out of bound!
                    """))
                    yes_n = False
        return devs

    def module_information(self):
        info = 'This module going to help you to entry data to \n this app' \
               'from terminal. It is accept to entry one or many \n developers at the same time.'

        print('\n ------------------------------------------------'
              '\n MODULE INFORMATION -> HANDLE DATA VIA TERMINAL'
              '\n ------------------------------------------------'
              '\n {}'.format(info))
        print('\n ------------------------------------------------\n')

    # TODO: finish this method
    def attrib_validation(self, attribute, code):
        yes_attr = False

        if code == 'alpha':
            x = re.match('[a-zA-Z]', attribute)
            if x: 
                yes_attr = True          
        if code == 'numeric':
            x= re.match('\rd', attribute)
            if x:
                yes_attr = True
        if code == 'alphanum':
            x = re.match('[a-zA-Z]+\rd', attribute)
            if x:
                yes_attr = True
        
        return yes_attr

    def show_warning(self, attribute):
        print('*'*60)
        print(dedent("""
            ======= WARNING ========
            
            Invalid value to {}!!!
            You need to inform other value 
            for attribute {}.
            
            """.format(attribute, attribute))
        )  
        print('*'*60)
        time.sleep(self.sleep)
