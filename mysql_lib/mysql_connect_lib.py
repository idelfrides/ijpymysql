
#!/usr/bin/env python
# -*- encoding: utf-8 -*-


"""
 ------------------------------------------------------
   ====  PACKAGE INFORMATION  ====
 Package name: ijpymysql
 Version: 1.0.0
 Description: module to handle data from MySQL
              DB with python 3.6
 @utor: Idelfrides Jorge
        Computer Engineer and software Developer.
 Date started: jul. 25th, 2019
 Date finished: jul. 29th, 2019
 License: on the README.md file
 Email: idelfridesjorgepapai@gmail.com
 GitHub: @idelfrides(https://github.com/idelfrides/)
 ------------------------------------------------------
   ====  TECHNICAL INFORMATION  ====
 Python Interpreter:
    --> Python 3.7.3 by ENV
 Python driver for MySQL database:
    --> PyMySQL v0.9.3
 -*- Coding: UTF-8 -*-
     content-type: script/python; utf-8
 ------------------------------------------------------
"""

from utils import HelperModule
import pymysql


class MySQLDBLib(HelperModule):    
    """
        This class is the library for python
        appications working with MySQL DB.
        The class will create all methods needed to
        manage a db app and more other methods.
    """ 

    def __init__(self):
        self.appdb = 'ijpymysqlDB'
        self.apptable = 'developer'
        self.hmo = HelperModule()
        self.hmo.app_information()

    def set_connection(self):
        """
            This method set a conection to the local server,
            with no 'database' created yet.
            This method is only called on your main module,
            the same used to test the 'ijpymyql' package.
            Return  'connection' with db and 'cursor' 
            to execute quereis.
            
            :param self: auto reference parameter

            :type self: python reserved word

            :rtype: connection with MySQL and cursor of that connection
        """

        conection = pymysql.Connect(
            host = 'localhost',     # 127.0.0.1
            user = 'root',
            password = '',   # 'mydbwm19',
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor
        )
        cursor = conection.cursor()
        self.db_con = conection
        return conection, cursor

    def set_connec_with_db(self):
        """
            This method set conection to the local server,
            with a 'database' already exists. It need to set a DB.
            It is only called on your main module,
            the same used to test the 'ijpymyql' package.
            Return 'conection' with db and 'cursor'
            to make quireis.
        """      
        
        conection = pymysql.Connect(
            host='localhost',    # 127.0.0.1
            user='root',
            password= '',  # 'mydbwm19',
            database = self.appdb,
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor
        )
        cursor = conection.cursor()
        return conection, cursor

    def close_mysql_connec(self, connec, cursor):
        """
            This method close the connection with MySQL
            server. The con only or cursor only or both them
                     
            :type connec: connection with MySQL DB

            :type cursor: cursor of MySQL connection to make queries
            
            :rtype: None
        """
        
        try:
            cursor.close()
            connec.close()
            print('\n MySQL Connection is closed successfuly \n')
        except Exception as error:
            print('Error by tring to CLOSE the connection with MySQL server %s ', connec)
            print('\n\n Server said: {}'.format(error))
    
