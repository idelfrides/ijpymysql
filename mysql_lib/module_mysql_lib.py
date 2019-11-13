
#!/usr/bin/env python
# -*- encoding: utf-8 -*-


"""
 ------------------------------------------------------
   ====  PACKAGE INFORMATION  ====
 App name: ijpymysql
 Version: 1.0.0
 Description: module to handle data from MySQL
              DB with python 3.6
 @utor: Engineer Idelfrides Jorge
 Date started: jul. 25th, 2019
 Date finished: jul. 29th, 2019
 License: on the README.md file
 Email: idelfridesjorgepapai@gmail.com
 GitHub: @idelfrides(https:\\github.com/idelfrides/)
 ------------------------------------------------------
   ====  TECHNICAL INFORMATION  ====
 Python Interpreter:
 --> Python 3.6.2
 Python driver for MySQL database:
   --> PyMySQL v0.9.3
   --> PyMySQLDB v0.0.2 (doesn't used)
 -*- Coding: UTF-8 -*-
 content-type: script/python; utf-8
 ------------------------------------------------------
"""

from utils import HelperModule
import pymysql          # mysql db driver


class MySQLDBLib(object):    
    """
       ---------------------------------------------------
          ====  OPERATIONAL INFORMATION  =====
         This module will be my library for python
         appications working with MysSQL DB.
         The module will create all method needed to
         manage a db app and more other methods.
       ---------------------------------------------------
    """ 
    

    appdb = 'py_app_db'         # define db name
    dev_table = 'developer'     # define table name
    # man_table = 'manager'     # define manager table
    # sup_table = 'supervisor'  # define supervisor table

    def __init__(self):
        """
           -------------------------------------------------
            The thunder init method inicialize and show
            the module information to user via terminal by
            calling method 'app_info()'
           -------------------------------------------------
           
           :type self: auto reference parameter
           :rtype: None
        """
        self.hmo = HelperModule()
        self.hmo.app_info()

    
    def set_conection(self):
        """
           --------------------------------------------------
             This method set conection to the local server,
             with no 'database' created yet.
             This method is only called on your main module,
             the same used to test the 'ijpymyql' package.
             Return  'connection' with db and 'cursor'
                     to execute quereis.
           --------------------------------------------------           
           
           :type self: auto reference parameter
           :rtype: connection with MySQL | cursor of that connection
        """

        conec = pymysql.Connect(
            host = 'localhost',
            user = 'root',
            password = '',
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor
        )
        cursor_conec = conec.cursor()
        self.db_con = conec
        return conec, cursor_conec

    
    def set_conec_with_db(self):
        """
           ----------------------------------------------------------
             This method set conection to the local server,
             with a 'database' already exists. It need to set a DB.
             It is only called on your main module,
             the same used to test the 'ijpymyql' package.
             Return 'conection' with db and 'cursor'
             to execute quireis
           -----------------------------------------------------------
        """      
        
        # print("\n I AM A CONNECTION WITH A MySQL DB\n")
        db_conection = pymysql.Connect(
            host='localhost',
            user='root',
            password='',
            database = self.appdb,
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor
        )
        cursor = db_conection.cursor()
        return db_conection, cursor

    
    def verification(self, cur, entity):
        """
           -------------------------------------------------
             This method verify if the entity(db or table)
             is realy exists in the local server.
             It return 1 if the entity exists or
             0 if it not exists.
           -------------------------------------------------
        """      
        ans = 0
        if entity is 'db':
            try:
                cur.execute("SHOW DATABASES")
                for db in cur:
                    val = db.values()     # get dict of dbs
                    list_db = list(val)   # convert  the dict to list of dbs
                    host_db = list_db[0]
                    app_db = self.appdb
                    if host_db == app_db:
                        ans = 1
                        break
                    else:
                        ans = 0
                return ans
            except Exception as error:
                print('Error by try to show all DB. \n Server said: {}'.format(error))
        elif entity is 'tb':
            try:
                cur.execute("SHOW TABLES")
                for tb in cur:
                    val = tb.values()    # get a dict of a table
                    list_tb = list(val)  # convert the dict to a list of table
                    host_tb = list_tb[0]
                    app_tb = self.dev_table
                    if host_tb == app_tb:
                        ans = 1
                        break
                    else:
                        ans = 0
                return ans
            except Exception as error:
                print('Error by try to show all tables. \n Server said: {}'.format(error))
        else:
            pass


    def create_db(self, cur_con, db):
        """
           -------------------------------------------------
             This method create a DB to be used on
             this package. The db is define by you/user as
             an attribute of this module(see on the to).
           -------------------------------------------------
           
           :type cur_con: cursor of mySQL connection
           :type db: database name to be created
           :rtype: None
        """
        try:
            sql = "CREATE DATABASE IF NOT EXISTS" + db
            cur_con.execute(sql)
            print("\n Database {} created successfully. \n ".format(db))
        except Exception as erro:
            print('Error by try to CREATE DB: {}. \n Server reponse: {}'.format(self.appdb, erro))

 
    def activate_db(self, cur_con, db=None):
        """
           -------------------------------------------------
            This method activate the DB to be used to test
            this package.
           -------------------------------------------------
           
           :type cur_con: cursor of MySQL connection
           :type db: data base name to be created
           :rtype: None
        """
        if db is not None:  # database passed
            try:
                sql_use = " USE " + db
                cur_con.execute(sql_use)
                print('\n Database {} activated successfuly'.format(self.appdb))
                return
            except Exception as erro:
                print('\n Error try to activate DB {}. \n Server said: {}'.format(self.appdb, erro))
                
                
        if db is None:      
            try:
                sql_use = " USE " + self.appdb
                cur_con.execute(sql_use)
                print('\n Database {} activated successfuly'.format(self.appdb))
                return
            except Exception as erro:
                print('\n Error try to activate DB {}. \n Server said: {}'.format(self.appdb, erro))

 
    def create_table(self, cur, mytb):
        """
           --------------------------------------------------
            This method create a table to the DB and be
            used on this package. Al tables is defined by
            you/user like  an attribute of this
            module(see on the to).
           --------------------------------------------------
           
           :type cur: cursor of MySQL connection
           :type mydb: database name where a table will be created
           :rtype: None
        """
        
        # cursor_conec = self.set_conec_with_db()

        sql_1 = "CREATE TABLE IF NOT EXISTS " + mytb
        myfields = "(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), gender ENUM('M', 'F'), company VARCHAR(255), age INT(3), salary FLOAT(7, 2))"
        sql = sql_1 +  myfields
        try:
            cur.execute(sql)
            print("\n Table {} created successfully. \n ".format(mytb))
        except Exception as erro:
            print('\n Error by try to create the table: {}. \n Server reponse: {}'.format(mytb, erro))


    def alter_table(self, cur, mytb, oper, atrib):
        """
           -------------------------------------------------
             This method alter a table present on DB.
             The method provide 3 operations: add, drop
             and modify. The tables and operation are
             defined by you/user like an attribute(tables)
             of this module(see on the to).
           -------------------------------------------------
           
           :type cur: cursor of MySQL connection
           :type mydb: database name, witch contain the
                       table that the attibute gonna be altered
           :type oper: the operation to be perform over the attribute atrib
           :type atrib: attibute will be altered
           :rtype: None
        """
        
        # cur = self.set_conec_with_db()
        if oper is 'add':
            sql_1 = " ALTER TABLE " + mytb
            newattri = " ADD COLUMN " + atrib + " VARCHAR(255)"
            sql = sql_1 + newattri
            print(sql)
            try:
                cur.execute(sql)
                print("\n Table {} altered successfully. \n ".format(mytb))
            except Exception as erro:
                print('\n Error by try to alter the table: {}. \n Server reponse: {}'.format(mytb, erro))
        elif oper is 'drop':
            sql_1 = "ALTER TABLE " + mytb
            drop_attri = " DROP COLUMN " + atrib
            sql = sql_1 + drop_attri
            try:
                cur.execute(sql)
                print("\n Table {} altered successfully. \n ".format(mytb))
            except Exception as erro:
                print('\n Error by try to alter the table: {}. \n Server reponse: {}'.format(mytb, erro))
        elif oper is 'mod':
            sql_1 = "ALTER TABLE " + mytb
            mod_attri = " MODIFY COLUMN " + atrib + " VARCHAR(255)"
            sql = sql_1 + mod_attri
            try:
                cur.execute(sql)
                print("\n Table {} altered successfully. \n ".format(mytb))
            except Exception as erro:
                print('\n Error by try to alter the table: {}. \n Server reponse: {}'.format(mytb, erro))
        else:
            pass
 

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
