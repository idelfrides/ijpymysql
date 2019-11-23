#! /usr/bin/env python
# -*- encoding: utf-8 -*-
 
""" Test module """

from ijpymysql import *


class UseMysqlLib(object):
    """ Testing the library module  """

    def __init__(self):
        self.mysql_lib = MySQLDBLib()
        self.db_lib = DBLib()
        self.tb_lib = TableLib()
    
    def run_lib(self):
        connec, cursor = self.mysql_lib.set_connection()

        self.db_lib.create_db(cursor, self.mysql_lib.appdb)

        self.db_lib.activate_db(cursor, self.mysql_lib.appdb )

        print(connec)

        print('\n\n I AM RUN LIB \n\n')


def main():
    mysql_obj = UseMysqlLib()
    mysql_obj.run_lib()


if __name__ == "__main__":
    main()