#! /usr/bin/env python
# -*- encoding: utf-8 -*-
 
""" Test module """

from ijpymysql import *


class UseMysqlLib(object):
    """ Testing the library module  """

    def __init__(self):
        self.mylibo = MySQLDBLib()
        self.dblibo = DBLib()
        self.tblibo = TableLib()
        self.cmo = CrudManager()
    

    def run_lib(self):
        connec, cursor = self.mylibo.set_connection()

        self.dblibo.create_db(cursor, self.mylibo.appdb)
        
        if not self.dblibo.db_verification(cursor, self.mylibo.appdb):
            exit(0)

        self.dblibo.activate_db(cursor, self.mylibo.appdb )

        self.tblibo.alter_table(cursor, self.mylibo.apptable,
            'drop',
            'age'
        )

        self.tblibo.alter_table(cursor, self.mylibo.apptable,
            'drop',
            'gender'
        )

        self.tblibo.alter_table(cursor, self.mylibo.apptable,
            'add',
            'role'
        )

        self.tblibo.alter_table(cursor, self.mylibo.apptable,
            'add',
            'adress'
        )

        # ---------- CRUD OPERARION ----------- 

        self.cmo.read_all(cursor, self.mylibo.apptable)

        self.mylibo.close_mysql_connec(connec, cursor)
        

        print('\n\n I AM RUN LIB \n\n')
        


def main():
    mysql_obj = UseMysqlLib()
    mysql_obj.run_lib()


if __name__ == "__main__":
    main()
