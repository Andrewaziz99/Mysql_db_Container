# <h1>Mysql_db_With_Python</h1>

<p>Simple docker Project, Allow to access mysql database from python.
     Can Insert values, show table's data and also can create new databases and tables.
     In this project I used docker image <b>'Mysql'</b> and python library <b>'mysql.connector.python'</b>
     It is not a volatile project, it will store data in your local machine.
</p>

<hr>

# <h2>How to run this project</h2>

<pre>
1. Clone this project
2. Open terminal and go to project directory
3. Pull Docker image by running command <b>'docker pull mysql'</b>
4. Run command <b>'docker run -v $PWD:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw  -p 4444:3306 -d mysql'</b>  --> This command will run mysql docker image on port 4444 and in the cuurent directory in the background.
5. Open another terminal and go to project directory
6. Run command <b>'python3 main.py'</b>
</pre>

<hr>

# <h2>How to create database and table</h2>

<pre>
1. Open <b>main.py</b> file with any text editor (recommended vscode)
2. After line 16 you can execute sql queries
3. Edit this line : mycursor.execute("CREATE DATABASE mydatabase") --> Change <b>'mydatabase'</b> to your database name
4. Edit this line : mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))") --> Change <b>'customers'</b> to your table name
5. Save the file and run command <b>'python3 main.py'</b> in terminal
</pre>
