
""" Helper module """

import winsound


class HelperModule(object):
    """
       --------------------------------------------------
        This contain some auxiliar methods, witch used 
        to help user understanding what is going on.
       --------------------------------------------------
    """

    def app_info(self):
        """
            ---------------------------------------------------
             This method shows the propose of this application
              by resume. That is his information.
              This method is only called by 'thunder init'
              method of ModuleMySQLdb module/class.
            ---------------------------------------------------
        """
        
        info = ''' 
        ----------------------------------------------
             ====  BUILDING INFORMATION  ====
            App name: ijpymysql
            Description: module to handle data from MySQL 
            DB with python 3.6
            @utor: Engineer Idelfrides Jorge
            Date started: jul. 25th, 2019
            Date finished: jul. 29th, 2019
            License: 
            Email: idelfridesjorgepapai@gmail.com
            GitHub: @idelfrides(https://github.com/idelfrides/)
            -------------------------------------------------
                ====  OPERATIONAL INFORMATION  =====
            This module will be my library for python
            applications working with MysSQL DB.
            The module will create all method needed to
            manage a db app and more other methods.
            -------------------------------------------------
                 ====  TECHNICAL INFORMATION  ====
            -*- Coding: UTF-8 -*-
             content-type: script/python; utf-8
        -------------------------------------------------'''

        print('{}'.format(info))

   
    def beep_alert(self):
        """
            ---------------------------------------------------
              This method sounds an alert sound to warn about a
              danger actions - DROP DATABASE/TABLE
              This method is only called by 'info_danger'
              method of this module/class.
            ---------------------------------------------------
        """
        frequency = 2500  # Set Frequency To 2500H Hertz
        duration = 1000    # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)


    def info_danger(self, code, entity):
        """
            ---------------------------------------------------
              This method shows a message alert to warn about a
              danger actions - DROP DATABASE/TABLE
              This method is only called by 'drop_struct'
              method of ModuleMySQLdb module/class.
              It return [1] to drop or [0] to quit
            ---------------------------------------------------
        """
        
        self.beep_alert()
        yes_drop = 0
        if code == 'db':
            infor = '''
               **************************************************
                        WARNING: VERY DANGER ACTION
               **************************************************
               You are trying to DROP a DATABASE, that a too 
               DANGER action. If you do that, you will LOSE 
               every single TABLES on it and data definitely.
               So, we recomend you to ABORT/ABANDON/QUIT 
               that operation.            
               '''
            print('\n {}'.format(infor))
            print('\n You tring to DROP DATABASE {}'.format(entity))

            valid_ans = False
            while valid_ans is False:
                print('\n Press Y/y to continue or N/n to Abort/quit')
                resp = input('\n Enter your choice[y/n]:  ')
                if resp.isalpha() and resp == 'Y' or resp == 'y':
                    valid_ans = True     # a caracter informed Y or y
                    yes_drop = 1
                elif resp.isalpha() and resp == 'N' or resp == 'n':
                    valid_ans = True     # a caracter informed N or n
                    yes_drop = 0
                elif resp.isnumeric():
                    valid_ans = False    # a number informed
                else:
                    pass
            return yes_drop

        elif code == 'tb':
            infor = '''
               **************************************************
                        WARNING: VERY DANGER ACTION
               **************************************************
                  You are trying to DROP a TABLE, that a too 
                  DANGER action. If you do that, you will LOSE 
                  all data/records on it definitely.
                  So, we recomend you to ABORT/QUIT 
                  that operation. In worse case, we recomend
                  TRUNCATE instead DROP operation.    
               '''
            print('\n {}'.format(infor))
            print('\n You tring to DROP TABLE {}'.format(entity))

            valid_ans = False
            while valid_ans is False:
                print('\n Press Y/y to continue or N/n to Abort/quit')
                resp = input('\n Enter your choice[y/n]:  ')
                if resp.isalpha() and resp == 'Y' or resp == 'y':
                    valid_ans = True  # a caracter informed Y or y
                    yes_drop = 1
                elif resp.isalpha() and resp == 'N' or resp == 'n':
                    valid_ans = True  # a caracter informed N or n
                    yes_drop = 0
                elif resp.isnumeric():
                    valid_ans = False  # a number informed
                else:
                    pass
            return yes_drop
        else:
            pass


    def module_crud_info(self):
        """
            ---------------------------------------------------
             This method shows the propose of the Crud_build class.
             That is his information.
             This method is only called by 'thunder init'
             method of Crud_build module.
            ---------------------------------------------------
        """
        
        info = 'This module going to help you to handling data of DB MySQL\n' \
                'from FORM or TERMINAL RUN app. It contain all methods \n' \
                ' to build a CRUD features .'

        print('\n ------------------------------------------------'
              '\n\t\t\t MODULE INFORMATION -> CRUD MODULE'
              '\n ------------------------------------------------'
              '\n {}'.format(info))
        print('\n ------------------------------------------------\n')
