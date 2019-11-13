
"""
 ---------------------------------------------
   ====  MODULE INFORMATION  ====
 ---------------------------------------------
 This module proccess form. Recover values of
 form process them and insert on the table
-----------------------------------------------
"""


# ---------------------------------------------
# import python modules
# ---------------------------------------------
from mysql_lib import MySQLDBLib
from  .crud_manager import CrudManager
import cgi          # common geteway interface support


# ---------------------------------------------
#  create an object of cgi to get data form
# ---------------------------------------------
myform = cgi.FieldStorage()


# --------------------------------------------
# tratamento de dados vindos do formulário
# --------------------------------------------
name = myform.getvalue("n_uname")
company = myform.getvalue("n_comp")
salary = myform.getvalue("n_salary")
role = myform.getvalue('n_role')
adress = myform.getvalue('n_adress')

#  REGULAR EXPRESSION PYTHONS

# ---------------------------------------------
#  show data individualy
# ---------------------------------------------
print('\n {}\n {}\n {}\n {} \n {}'.format(name, company, salary, role, adress))

# ---------------------------------------------
# create a list called data o store data on it
# ---------------------------------------------
data = list()  #


# ---------------------------------------------
# add values recovered from form to data list
# ---------------------------------------------
data.append(name)
data.append(company)
data.append(salary)
data.append(role)
data.append(adress)


# ---------------------------------------------
#  Create objects from  modules of 
# ijpymysql library
# ---------------------------------------------

dblib = MySQLDBLib()
cmo = CrudManager()


# ---------------------------------------------
#  set conection to local server
# ---------------------------------------------
con, cur = MySQLDBLib().set_conec_with_db()


# ---------------------------------------------
#  get table name
# ---------------------------------------------
devtb = dblib.dev_table


# ---------------------------------------------
#  create an  record on the table
# ---------------------------------------------
cmo.insert(con, cur, devtb, data)
