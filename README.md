
# ijpymysql Library


## Project Information

This is an python library  created to work with MySQL DB in Python 3. It's a Python package available to be used on Python projects that need to handle data from a MySQL database.

The package  use **OOP** and  **Microserce Architecture** and organized like you can see on tab **<> Code** (in the top left menu) with four packages. All them, except templates, has one or more modules, each one olds a Class. The classes contain many methods used to build this library, exept from_data_manager.py.


## Execution information
 Package name: ijpymysql
 
 Description: This project is mine one of monst important project. It'is a package to handle data on MySQL DB with python.

 @utor: Engineer Idelfrides Jorge
 
 Date started: jul. 25th, 2019
 
 Date finished: jul. 29th, 2019
 
 License: provide one.
 

## Technical Information
 Python Interpreter:
 
   --> Python 3.7.3 by ENV

 Python driver for MySQL database:
 
   --> PyMySQL v0.9.3
   
 -- Coding: UTF-8 --
 
 content-type: script/python; utf-8
 
## HOW TO USE: Steps to use this package
 Follow next steps to use this package in your python project or to make a simple test and learn more.
 
 ### Step 1:
Install **ijpymysql** from pip 
like: pip install ijpymysql

 ### Step 2:
Read the file README fully, or for other way, you can do it here on github repository or on the PyPi.
After that, take a look to understand project structure, to understand mostly, the fields of the table.
So, in this point, you may make some changes on it or create your own table to use [I recomend you the second option].

 ### Step 3:
Then, you may use it like I am goint to tell you next.
Create a python file in root of your project, to be a main one. Then, create a method inside that file, that mrthod is goint to be, therefore the main method of your python project. So, after that follow next steps. 

 ### Step 4:
Import modules inside **ijpymysql** and python time module you gonna use in your project like this.
* Do this: from ijpymysql import MySQLDBLib, DBLib, TableLib
* Do this: import time.

 ### Step 5:
Inside the main method you have to create an object of module you goint to need imediatily or for all modules(I recomend the first way). Take a look a real example.
* Example: mylibo = ModuleMySQLdb()


 ### Step 6:
  Call the method to set up a conection to local server
    * Example: 
      connec, cursor = mylibo.set_connection() [1] or
      connec, cursor = mylibo.set_connec_with_db() [2].

      WARNING: Do not execute option [2], do the first one [1].
      Do this [2] only if you sure that database already exists.

     # -----------------------------------------------
     #  set_connection()
     # --------
     # This method set a conection to the locol server,
     # with no 'database' created yet.
     # This method is only called on your main module,
     # the same used to test the 'ijpymysql' package.
     # Return  'connection' with db and 'cursor' 
     # to execute quereis.
     # -----------------------------------------------
    

  If you really sure about a database existence, do this. This is a particular case.

    # -------------------------------------------------
    #  set_connec_with_db()
    # --------
    # This method set up aconection to the localhost 
    # (local server), with an database already 
    # created. This argument is required. 
    # This method is only called on your main module/file,
    # the same used to test the 'ijpymysql' package.
    # Return 'connection' with db and 'cursor'
    # to execute queries.
    # -------------------------------------------------


 ### Step 7:
  Considering that you connected to server without a databse, now you need verify with database are in your local server. For that, call method  show_all_db(cursor) from DBLib class.
  
  From here, you can jump to **Step 8 (activate a database)**
  or 
  You can create a new database as you want.
  To do that, call method  create_db(self, cursor, db) like next.
    dblibo = DBLib()
    * Example: dblibo.create_db(cursor, mylibo.appdb)
   
    # ----------------------------------------------
    #  create_db(cursor, mdbo.appdb)
    # ---------
    # This method create a DB to be used on
    # your module. The db is define by you/user as
    # an attribute of ModuleMySQLdb module 
    # (see the module in package).
    # ----------------------------------------------
  
  Make sure that your db was successfuly created.For that, call method  db_verification(cursor, db).
     * Example: resp = dblibo.db_verification(cursor, 'db_name')
   
   
     # ----------------------------------------------
     # db_verification(cursor, db)
     # -------
     # This method verify if the db is realy
     # exists in the local server.
     # It return 1 if the db exists or
     # 0 if not exists.
     # ----------------------------------------------
  
  
 ### Step 8:
   Activate a db to be used in your project. For that, call  method  mdbo.activate_db(cursor, db).
   * Example: dblibo.activate_db(cursor, 'db_name').
      
    # ----------------------------------------------
    #  activate_db(cursor, db)
    # --------
    # This method activate the DB to be used to in your
    # project.
    # ----------------------------------------------
    
    
 ### Step 9:
   Now, call the show_all_tb method to make sure that some tables exists in your database actived.
   tblibo = TableLib()
   * Example: resp = tblibo.show_all_tb(cursor)
  
 
 ### Step 10:
   Finaly, you must alter the default table to drop two  attributes then add two others. To make this right call method alter_table(self, cur, tb, oper, atrib).
   * Example: tblibo.alter_table(cursor, mdbo.dev_table, 'drop', 'age')
   
  
    # ------------------------------------------------------
    #  alter_table(self, cur, tb, oper, atrib)
    # ---------
    # This method alter a table present on DB.
    # The method provide 3 operations: add, drop
    # and modify. The table, opration and attribute are defined by you/user.
    # ------------------------------------------------------
   
   Run alter table method to alter two attributes: age and gender as follow:
   
    # ----------------------------------
    # drop: age | gender
    # ----------------------------------
    mdbo.alter_table(cursor, mylibo.apptable, 'drop', 'age')
    mdbo.alter_table(cursor, mylibo.apptable, 'drop', 'gender')

    # ----------------------------------
    # add: role | adress
    # ----------------------------------
    mdbo.alter_table(cursor, mylibo.apptable, 'add', 'role')
    mdbo.alter_table(cursor, mylibo.apptable, 'add', 'adress')

 After these  steps, you are now free to play with the package like you want.
 
 ### Contributions
 
Maybe WE (me and you) can build the best **Python package for handle data on MySQL DB**  to help other pythpn developers emprove their job. So, feel free to start a chat or send pull requests.
 

  ----

 @uthor: IDELFRIDES JORGE | Mail me by idelfridesjorgepapai@gmail.com

 FOLLOW ME ON MEDIAS:

   GITHUB: [Idelfrides Jorge](https://github.com/idelfrides/)

   Linkedin: [Idelfrides Jorge](https://www.linkedin.com/in/idelfrides-jorge-089939107/)

   


