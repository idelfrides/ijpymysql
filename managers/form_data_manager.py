
"""
 ----------------------------------------------
   ====  MODULE INFORMATION  ====
 ----------------------------------------------
 This module proccess form. Recover values of
 form process them and insert on the table
-----------------------------------------------
"""

from mysql_lib import MySQLDBLib
from  .crud_manager import CrudManager
import cgi


def handle_data_from():

    myform = cgi.FieldStorage()

    name = myform.getvalue("n_uname")

    # or
    # name = myform['n_uname']
    company = myform.getvalue("n_comp")

    # do mnot have fields in the form -> index.html
    salary = myform.getvalue("n_salary")
    role = myform.getvalue('n_role')
    adress = myform.getvalue('n_adress')

    #  REGULAR EXPRESSION PYTHON

    data = list()  

    data.append(name)
    data.append(company)
    data.append(salary)
    data.append(role)
    data.append(adress)

    dblib = MySQLDBLib()
    cmo = CrudManager()
    con, cur = dblib.set_connec_with_db() 

    cmo.insert(con, cur, dblib.apptable, data)

