
#!/usr/bin/env python
# -*- encoding: utf-8 -*-



from utils import HelperModule
import pymysql


class TableLib(HelperModule):    
    """ Table lib object """ 

    def __init__(self):
        self.hmo = HelperModule()
    
    def tb_verification(self, cursor, tb):
        """
            This method verify if the table
            is realy exists in the local server.
            It return 1 if the tb exists or
            0 if it not exists.

            :param cursor: object of mySQL connection
            :type cursor: object of mysql to make queries
            :param tb: table to be verifyed
            :type tb: string
            :rtype: 1 = Yes or 0 = No
        """ 
        ans = 0

        try:
            cursor.execute("SHOW TABLES")
            for tb in cursor:
                dict_tbs = tb.values()    # get a dict of a table
                list_tb = list(dict_tbs)  # convert the dict to a list of table
                host_tb = list_tb[0]
                if host_tb == tb:
                    ans = 1
                    break
            
            return ans
        except Exception as error:
            print('Error by try to show all tables. \n Server said: {}'.format(
                error)
            )
        
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
   
    def drop_table(self, connec, cursor, table):
        """        
            This method DROP a table exists.

           :param connec: connection with MySQL DB
           :type connec: object of MySQL 
           :param cursor: cursor of MySQL connection
           :type cursor: object of MySQL connection
           :param table: the name of table will be droped
           :type table: string
           :rtype: None
        """
        
        # cur = self.set_conec_with_db()
        option = self.hmo.info_danger('tb', table)
        
        if option == 1:
            sql = " DROP TABLE IF EXISTS " + table
            try:
                cursor.execute(sql)
                print("\n Table {} was droped successfully. \n ".format(table))
                connec.comit()
            except Exception as erro:
                print('\n Error try to DROP the table: {}'.format(table))
                print('\n Server reponse: {}'.format(erro))
        
        if option == 0:
            print('\n YOU CHOSE TO QUIT \n INTELIGENT DECISION.')

    def truncate(self, connec, cursor, table):
        """        
            This method TRUNCATE a table presents on DB.
            The method has 3 parameters: connection, cursor
            and the table that going to be truncated.  
           
            :param connec: connection with MySQL DB
            :type connec: object of MySQL 
            :param cursor: cursor of MySQL connection
            :type cursor: object of MySQL connection
            :param table: the name of table will be truncated
            :type table: string
            :rtype: None
        """
        try:
            sql = " TRUNCATE TABLE " + table
            cursor.execute(sql)
            connec.comit()
            print("\n Table {} TRUNCATED successfully. \n ".format(table))
        except Exception as error:
            print('\n Error by try to TRUNCATE the table: {}'.format(table))
            print('\n Server reponse: {}'.format(error))

    def unique_constraint(self, cur, table, oper, attr):
        """
            This method alter a table present on DB to make
            an attr as UNIQUE. It provide 2 operations: 
                --> Add | Drop
            The table, oper and attr 
            are defined by you/user as arguments of method.
           
            :param cur: connection with MySQL DB
            :type cur: cursor of MySQL connection
            :param table: the table that contain the attribute
            :type table: string
            :param oper: the operations to be perform
            :type oper: string
            :param attr: attibute to make unique 
            :type attr: string  
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
                return
            except Exception as error:
                print('Error by tring to MAKE {} as UNIQUE. \n\n Server said: {}'.format(attr, error))
        
        if oper is 'drop':
            print('\n DROPPING UNIQUE CONSTRAINT FROM ATTR {}'.format(attr))
            print(' IN TABLE {}'.format(table))
            
            try:
                sql_1 = " ALTER TABLE " + table
                sql_2 = ' DROP CONSTRAINT ' + unique_const_name
                sql = sql_1 + sql_2
                cur.execute(sql)
                print('\n Operation done SUCCESSFULY')
            except Exception as error:
                print('Error by tring to REMOVE {} as UNIQUE. \n\n Server said: {}'.format(attr, error))
       

