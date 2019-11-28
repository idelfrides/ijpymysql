
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
        self.sleep = 7            # seconds
        self.module_information()

    def data_from_terminal(self):
        print(dedent("""
            ---------------------------------
               INFORMING DATA FOR ONE DEV
            ---------------------------------

            """)
        )
        
        ind = 0
        dev_data = list()
        attr_type = [
            'alpha',
            'alpha',
            'numeric',
            'alpha',
            'alphanum'
        ]
        
        for attr in ['name', 'company', 'salary', 'role', 'adress']:
            try:
                attr_value = input('\n Enter the %s:  ',attr)
            except KeyboardInterrupt as kbi_exc:
                print('\n Program interrupted by user \n {}'
                    .format(kbi_exc)
                )
                exit(0)
            else:
                if not self.attrib_validation(attr_value, attr_type[ind]):
                    self.show_warning(attr)
                    self.data_from_terminal()

            dev_data.append(attr_value)
            ind += 1
        
        #        name, company, salary, role, adress
        # return name, company, salary, funcao, adress
        return dev_data

    def data_from_terminal_many(self):
        print(dedent("""
            ------------------------------------
                INFORMING DATA FOR MANY DEV
            ------------------------------------

            """)
        )
        
        records = self.define_records_number() 

        all_dev_data = list()
        
        for ind in range(records):
            print(dedent("""
                --------------------------------
                        DATA FOR DEV {}
                --------------------------------
                
                """.format(ind+1))
            )
            
            one_dev_data = self.data_from_terminal()
            all_dev_data.append(one_dev_data)

        return all_dev_data

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
        info = '''
            This module going to help you to
            entry data to this app from terminal.
            It is accept to entry one or many
            developers at the same time.
        '''

        print('\n ------------------------------------------------'
              '\n MODULE INFORMATION -> HANDLE DATA VIA TERMINAL'
              '\n ------------------------------------------------'
              '\n {}'.format(info))
        print('\n ------------------------------------------------\n')

    def attrib_validation(self, attribute, code):
        """ Return True or False """

        yes_attr = False

        if code == 'alpha':
            if re.match('[a-z]', attribute):
                yes_attr = True

        if code == 'numeric':
            if attribute.isnumeric():
                yes_attr = True
            
        if code == 'alphanum':
            if re.match(r'\w+', attribute):
                yes_attr = True
        
        return yes_attr

    def show_warning(self, attribute):
        print('*'*60)
        print(dedent("""
            ======= WARNING ========
            
            Invalid value to {0}!!!
            You need to inform other value 
            for attribute {0}.
            
            """.format(attribute))
        )  
        print('*'*60)
        time.sleep(self.sleep)
