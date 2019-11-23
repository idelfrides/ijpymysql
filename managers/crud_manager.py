
from mysql_lib import MySQLDBLib
from utils import HelperModule


class CrudManager(MySQLDBLib, HelperModule):
    """
    ---------------------------------------------
       CRUD class(object) - contain all methods
       to build a CRUD features
    ---------------------------------------------
    """

    def __init__(self):
        self.mdbo = MySQLDBLib()
        self.hmo = HelperModule()
        self.hmo.module_crud_info()

    def insert(self, con, cur, mytb, data):     
        try:
            sql = "INSERT INTO " + mytb + "(name, company, salary, role, adress) VALUES (%s, %s, %s, %s, %s)"
            myvalues = (data[0], data[1], data[2], data[3], data[4])
            print("\n eu sou data: {}".format(data))
            print("\n eu sou val: {}".format(myvalues))
            cur.execute(sql, myvalues)
            con.commit()
            print(" {} Dev inserted. \n Dev ID: {}".format(cur.rowcount, cur.lastrowid))
        except Exception as erro:
            print('\n Error try to INSERT INTO the table: {}. \n Server reponse: {}'.format(mytb, erro))


    def insert_many(self, con, cur, mytb, list_data):
        try:
            i = 0
            j = 5
            loop = True
            mylist_values = list()
            n = list_data.__len__()
            while loop is True:
                data_dev = list_data[i:j]
                tuple_data_dev = tuple(data_dev)  # transforme the list data_dev to a tuple
                mylist_values.append(tuple_data_dev)
                i = j
                j = j + 5
                if i is n:
                    loop = False
                else:
                    pass

            sql = "INSERT INTO " + mytb + "(name, company, salary, role, adress) VALUES (%s, %s, %s, %s, %s)"
            cur.executemany(sql, mylist_values)
            con.commit()
            print(" {} Dev inserted.".format(cur.rowcount))
        except Exception as error:
            print('\n Error try to INSERT INTO the table: {}. \n Server reponse: {}'.format(mytb, error))


    def read_one(self, cur, mytb):        
        print('\n I AM GONNA READ ONE \n')
        try:
            sql = "SELECT * FROM " + mytb
            cur.execute(sql)
            myresult = cur.fetchone()
            print('\n The first row {}'.format(myresult))
        except Exception as error:
            print('\n Error try to SELECT FROM  table: {}. \n Server reponse: {}'.format(mytb, error))

    def read_all(self, cur, mytb):        
        # fetch -> buscar | fetches -> busca
        # fetchall() -> busca todas as linhas do conjunto de resultado de consulta sql
        # e retorna uma lista de tuplas. Caso o  result set for null,
        # fetchall/fetchone/fetchmany  retorna uma lista vazia
        # executemany(sql, val)

        try:
            sql = "SELECT * FROM " + mytb
            cur.execute(sql)
            results = cur.fetchall()
            for x in results:
                print('\n {}'.format(x))
        except Exception as error:
            print('\n Error try to SELECT FROM  table: {}. \n Server reponse: {}'.format(mytb, error))
    
    def read_one_filter(self, cur, mytb, dev_name):
        print('\n READ ONE: {} \n'.format(dev_name))
        try:
            sql = "SELECT * FROM " + mytb + " WHERE name = %s"
            atrib = (dev_name)
            cur.execute(sql, atrib)
            myresult = cur.fetchone()
            print('\n The first row {}'.format(myresult))
        except Exception as error:
            print('\n Error try to SELECT FROM  table: {}. \n Server reponse: {}'.format(mytb, error))

    def read_some_attr(self, cur, mytb, atr1, atr2):
        print('\n I AM GONNA READ SOME \n')
        try:
            sql = " SELECT " + atr1 + "," + atr2 + " FROM " + mytb
            cur.execute(sql)
            results = cur.fetchall()
            for x in results:
                print('\n {}'.format(x))
        except Exception as error:
            print('\n Error try to SELECT FROM table: {}. \n Server reponse: {}'.format(mytb, error))

    def read_some_dev(self, cur, mytb, num_dev):
        """
           ---------------------------------------------
            READ one record from the table.
            It SELECT all attributes for some developer.
            The table and number of records to be shown is
            informed by user.
           ---------------------------------------------
        """

        try:
            sql = "SELECT * FROM " + mytb
            cur.execute(sql)
            results = cur.fetchmany(size=num_dev)
            for x in results:
                print('\n {}'.format(x))
        except Exception as error:
            print('\n Error try to SELECT FROM table: {}'.format(mytb))
            print('\n Server reponse: {}'.format(error))

    def update(self, connec, cursor, tb, attr, new_value, id):

        try:
            sql = "UPDATE " + tb + " SET " + attr + " = %s  WHERE id = %s"
            val = (new_value, id)
            cursor.execute(sql, val)
            connec.commit()
            print('\n Lines affected {}'.format(cursor.rowcount))
        except Exception as error:
            print('\n Error try to UPDATE table: {}'.format(tb))
            print('\n Server reponse: {}'.format(error))

    def delete(self,  con, cur, mytb, dev_name):
        try:
            sql = " DELETE FROM " + mytb + " WHERE name = %s"
            val = (dev_name)
            cur.execute(sql, val)
            con.commit()
            print('\n Record deleted: {}'.format(cur.rowcount))
            self.restart_pk(con, cur, mytb)   # restar the pk
        except Exception as error:
            print('\n Error try to DELETE FROM  table: {}.'
                  '\n Server reponse: {}'.format(mytb, error)
            )

    def custom_query(self, con, cur, query):
        """
           --------------------------------------------------
            This method lets you/user free to make a custom query
            to your DB. Yo by yourself write a SQL string
            command completely  and inform it to this method,
            to parameter 'query'(the last one).
            The method shows via run terminal the result.
           --------------------------------------------------
        """

        try:
            cur.execute(query)
            con.comit()
            print('\n\n QUERY SUCCESSFULL \n\n')
        except Exception as error:
            print('\n Error by executing YOUR QUERY. '
                  '\n Server said: {}'.format(error)
            )

    def restart_pk(self, connec, cursor, mytb):
        try:
            # sql = ' ALTER TABLE ' + mytb + 'AUTO_INCREMENT = 1'
            sql = ' ALTER TABLE ' + mytb + ' AUTO_INCREMENT = %s'
            start = 1
            cursor.execute(sql, start)
            connec.comit()
            print('\n Primary key restarted SUCCESSFULY for table {}'
                .format(mytb)
            )
        except Exception as error:
            print('\n Error by try restarting the primary key of {}.'
                  '\n\n Server said: {}'.format(mytb, error)
            )

