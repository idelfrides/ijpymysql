
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


class MySQLDBLib(object):    
    """
        This class is the my library for python
        appications working with MySQL DB.
        The class will create all methods needed to
        manage a db app and more other methods.
    """ 
    
    def __init__(self):
        self.appdb = 'py_app_db'                
        self.dev_table = 'developer'            
        # manager_table = 'manager'       
        # supervisor_table = 'supervisor' 
        
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
            host = 'localhost',
            user = 'root',
            password = '',
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
            host='localhost',
            user='root',
            password='',
            database = self.appdb,
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor
        )
        cursor = conection.cursor()
        return conection, cursor

    def verification(self, cursor, entity):
        """
            This method verify if the entity(db or table)
            is realy exists in the local server.
            It return 1 if the entity exists or
            0 if it not exists.

            :param cursor: object of mySQL connection
            :type cursor: object of mysql to make queries
            :param entity: type of entity to be verifyed. db or tb
            :type entity: caracter
            :rtype: None
        """ 
        ans = 0
        if entity is 'db':
            try:
                cursor.execute("SHOW DATABASES")
                for db in cursor:
                    dict_dbs = db.values()     # get dict of dbs
                    list_db = list(dict_dbs)   # convert the dict to list of dbs
                    host_db = list_db[0]
                    if host_db == self.appdb:
                        ans = 1
                        break
                    else:
                        ans = 0
                return ans
            except Exception as error:
                print('Error by try to show all DB. \n Server said: {}'.format(error))
        
        if entity is 'tb':
            try:
                cursor.execute("SHOW TABLES")
                for tb in cursor:
                    dict_tbs = tb.values()    # get a dict of a table
                    list_tb = list(dict_tbs)  # convert the dict to a list of table
                    host_tb = list_tb[0]
                    if host_tb == self.dev_table:
                        ans = 1
                        break
                    else:
                        ans = 0
                return ans
            except Exception as error:
                print('Error by try to show all tables. \n Server said: {}'.format(error))
        else:
            pass

    def create_db(self, cursor, db):
        """
            This method create a DB to be used on
            this package. The db is define by you/user as
            an attribute of this module(see on the to).
           
           :param cursor: cursor of mySQL connection
           :type cursor: object of mysql to make queries
           :param db: database name to be created
           :type db: string
           :rtype: None
        """
        try:
            sql = "CREATE DATABASE IF NOT EXISTS" + db
            cursor.execute(sql)
            print("\n Database {} created successfully. \n ".format(db))
        except Exception as erro:
            print('Error by try to CREATE DB: {}'.format(
                self.appdb)
            )
            print('\n Server reponse: {}'.format(
                erro)
            )

    def activate_db(self, cursor, db=None):
        """
            This method activate the DB to be used to test
            this package.
            
            :param cursor: cursor of MySQL connection
            :type cursor: onject of MySQL to make queries
            :param db: database name to be created
            :type db: string
            :rtype: None
        """

        if db is not None:  # database passed
            try:
                sql_use = " USE " + db
                cursor.execute(sql_use)
                print('\n Database {} activated successfuly'.format(
                    self.appdb)
                )
                return
            except Exception as erro:
                print('\n Error try to activate DB {}'.format(self.appdb))
                print('\n Server said: {}'.format(erro))
                
                
        if db is None: # No database passed  
            try:
                sql_use = " USE " + self.appdb
                cursor.execute(sql_use)
                print('\n Default database {} activated successfuly'.format(
                    self.appdb)
                )
                return
            except Exception as erro:
                print('\n Error try to activate DB {}'.format(self.appdb))
                print('\n Server said: {}'.format(erro))

    def create_table(self, cursor, mytb):
        """
            This method create a table on the DB 
            created befored or another one used 
            on this package. All tables is defined by
            you/user like  an attribute of this
            module(see on the to).

            :param cursor: cursor of MySQL connection
            :type cursor: onject of MySQL to make queries
            :param mytb: tabla name where to be  created
            :type mytb: string
            :rtype: None
        """

        sql_tb = "CREATE TABLE IF NOT EXISTS " + mytb
        tb_fields = "(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), gender ENUM('M', 'F'), company VARCHAR(255), age INT(3), salary FLOAT(7, 2))"
        sql = sql_tb +  tb_fields
        try:
            cursor.execute(sql)
            print("\n Table {} created successfully. \n ".format(mytb))
        except Exception as erro:
            print('\n Error by try to create the table: {}'.format(mytb))
            print('\n Server reponse: {}'.format(erro))

    def alter_table(self, cursor, mytb, operation, attrib):
        """
            This method alter a table present on a DB.
            The method provide 3 operations: add, drop
            and modify. The tables and operation are
            defined by you/user like an attribute(tables)
            of this module(see on the to).
           
            :param cursor: object of MySQL connection
            :type cursor: object of MySQL able to execute                 queries
            :param mytb: table name to be altered
            :type mytb: string
            :param operation: the operation to be perform                      over the  attribute 'attrib'
            :type operation: character
            :param attrib: attibute will be altered
            :type attrib: string
            :rtype: None
        """
        
        if operation is 'add':
            sql_add = " ALTER TABLE " + mytb
            new_attrib = " ADD COLUMN " + attrib + " VARCHAR(255)"
            sql = sql_add + new_attrib
            try:
                cursor.execute(sql)
                print("\n Table {} altered successfully. \n ".format(mytb))
                return
            except Exception as error:
                print('\n Error by try to alter the table: {}'.format(mytb))
                print('\n Server reponse: {}'.format(error))
        
        if operation is 'drop':
            sql_drop = "ALTER TABLE " + mytb
            drop_attrib = " DROP COLUMN " + attrib
            sql = sql_drop + drop_attrib
            try:
                cursor.execute(sql)
                print("\n Table {} altered successfully. \n ".format(mytb))
                return
            except Exception as error:
                print('\n Error by try to alter the table: {}'.format(mytb))
                print('\n Server reponse: {}'.format(error))
         
        if operation is 'mod':
            sql_mod = "ALTER TABLE " + mytb
            mod_attri = " MODIFY COLUMN " + attrib + " VARCHAR(255)"
            sql = sql_mod + mod_attri
            try:
                cursor.execute(sql)
                print("\n Table {} altered successfully. \n ".format(mytb))
            except Exception as error:
                print('\n Error by try to alter the table: {}'.format(mytb))
                print('\n Server reponse: {}'.format(error))
   
    def drop_struct(self, con, cur, code, entity):
        """        
           --------------------------------------------------
            This method DROP a db/table exists.
            The method has 3 parameters: cursor of conection,
            code of struct and the name(entity) of the same.
           --------------------------------------------------
           
           :type con: connection with MySQL DB
           :type cur: cursor of MySQL connection
           :type code: code of struct. Can be database (db) or table (tb)
           :type entity: name of the structure defined by code parameter. 
           :rtype: None
        """
        
        # cur = self.set_conec_with_db()
        op = self.hmo.info_danger(code, entity)
        if code is 'db':
            if op == 1:
                sql = " DROP DATABASE IF EXISTS " + entity
                try:
                    cur.execute(sql)
                    print("\n Database {}  was droped  successfully. \n ".format(entity))
                    con.comit()
                except Exception as erro:
                    print('\n Error try to DROP the Database: {}. \n Server reponse: {}'.format(entity, erro))
            elif op == 0:
                print('\n YOU CHOSE TO QUIT \n INTELIGENT DECISION.')
        elif code is 'tb':
            if op == 1:
                sql = " DROP TABLE IF EXISTS " + entity
                try:
                    cur.execute(sql)
                    print("\n Table {} was droped successfully. \n ".format(entity))
                    con.comit()
                except Exception as erro:
                    print('\n Error try to DROP the table: {}. \n Server reponse: {}'.format(entity, erro))
            elif op == 0:
                print('\n YOU CHOSE TO QUIT \n INTELIGENT DECISION.')
            else:
                pass
        else:
            pass

    def truncate(self, con, cur, mytb):
        """        
           --------------------------------------------------
             This method TRUNCATE a table presents on DB.
             The method has 3 parameters: connection, cursor
             and the table that going to be truncated.
           --------------------------------------------------          
           
           :type con: connection with MySQL DB
           :type cur: cursor of MySQL connection
           :type mydb: database name, witch contain the
                       table that the attibute gonna be truncated
           :rtype; None
        """
        try:
            sql = " TRUNCATE TABLE " + mytb
            cur.execute(sql)
            con.comit()
            print("\n Table {} TRUNCATED successfully. \n ".format(mytb))
        except Exception as error:
            print('\n Error by try to TRUNCATE the table: {}. \n Server reponse: {}'.format(mytb, error))
       
    def entity_verify(self, cur, entity):
        """
            -----------------------------------------------------
              This method make a verification of a struct: db
              or table presents on DB.
              The method show(via run terminal) all db existis
              on the localhost or all tables on a specific db.
            ------------------------------------------------------
            
            :type cur: cursor of MySQL connection
            :type entity: name of the structure: db or tb. 
            :rtype: None
         """
        
        if entity is 'db':
            print('\n VERIFY DB')
            try:
                cur.execute("SHOW DATABASES")
                for db in cur:
                    print('\n tipo: ', type(db))
                    print(' {}'.format(db))
            except Exception as error:
                print('Error by try to show all DB. \n Server said: {}'.format(error))
        elif entity is 'tb':
            print('\n VERIFY TB')
            try:
                cur.execute("SHOW TABLES")
                for tb in cur:
                    print('\n tipo: ', type(tb))
                    print(' {}'.format(tb))
            except Exception as error:
                print('Error by try to show all tables. \n Server said: {}'.format(error))
        else:
            pass

    def unique_constraint(self, cur, table, oper, attr):
        """
           ------------------------------------------------------
             This method alter a table present on DB to make
             an attr as UNIQUE. It provide 2 operations: Add | Drop
             The table, operation and attribute
             are defined by you/user as arguments of method.
           ------------------------------------------------------
           
           :type cur: cursor of MySQL connection
           :type attr: attibute to make unique 
           :type table: the table that contain the attribute
           :type oper: the operations to be perform
           :rtype: None
        """
        
        unique_const_name = table + '_' + attr + '_' + 'key'
        if oper is 'add':
            print('\n ADDING ATTR %s AS UNIQUE IN TABLE  %s',attr, table)
            try:
                sql_1 = " ALTER TABLE " + table
                sql_2 = 'ADD CONSTRAINT ' + unique_const_name + ' UNIQUE(attr)'
                sql = sql_1 + sql_2
                cur.execute(sql)
                print('\n Operation done SUCCESSFULY')
            except Exception as error:
                print('Error by tring to MAKE {} as UNIQUE. \n\n Server said: {}'.format(attr, error))
        elif oper is 'drop':
            print('\n DROPPING UNIQUE CONSTRAINT FROM ATTR {} IN TABLE {}'.format(attr, table))
            try:
                sql_1 = " ALTER TABLE " + table
                sql_2 = ' DROP CONSTRAINT ' + unique_const_name
                sql = sql_1 + sql_2
                cur.execute(sql)
                print('\n Operation done SUCCESSFULY')
            except Exception as error:
                print('Error by tring to REMOVE {} as UNIQUE. \n\n Server said: {}'.format(attr, error))
        else:
            pass

    def close_mysqlcon(self, con, cur):
        """
           ---------------------------------------------------
             This method close the connection with MySQL
             server. The con only or cursor only or both them
           ---------------------------------------------------
           
           :type con: connection with MySQL DB
           :type cur: cursor of MySQL connection
           :rtype: None
        """
        
        try:
            cur.close()
            con.close()
            print('\n MySQL Connection is closed successfuly \n')
        except Exception as error:
            print('Error by tring to CLOSE the connection with MySQL server %s ', con)
            print('\n\n Server said: {}'.format(error))
