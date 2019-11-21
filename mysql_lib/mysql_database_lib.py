
#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class DBLib(object):    
    """ Database lib object"""

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
        except Exception as error:
            print('Error by try to CREATE DB: {}'.format(db))
            print('\n Server reponse: {}'.format(error))

    def db_verification(self, cursor, db):
        """
            This method verify if the db
            is realy exists in the local server.
            It return 1 if the db exists or
            0 if it do not exists.

            :param cursor: object of mySQL connection
            :type cursor: object of mysql to make queries
            :param db: database to be verifyed.
            :type db: string
            :rtype: 1 = Yes or 0 = No
        """ 

        ans = 0
        try:
            cursor.execute("SHOW DATABASES")
            for db in cursor:
                dict_dbs = db.values()     # get dict of dbs
                list_db = list(dict_dbs)   # convert the dict to list of dbs
                host_db = list_db[0]
                if host_db == db:
                    ans = 1
                    break            
                if host_db != db:
                    ans = 0
            return ans
        except Exception as error:
            print('Error by try to show all DB. \n Server said: {}'.format(
                error)
            )
        
    def activate_db(self, cursor, db):
        """
            This method activate the DB to be used 
            to test this package.
            
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
                print('\n Database {} activated successfuly'.format(db))
                return
            except Exception as error:
                print('\n Error try to activate DB {}'.format(db))
                print('\n Server said: {}'.format(error))


    def drop_database(self):
        pass
            

