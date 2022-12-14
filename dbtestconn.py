from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 4444
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'gp41_db'
 
mysql = MySQL(app)

#Creating a cursor object using the cursor() method
with app.app_context():
    cursor = mysql.connection.cursor()  
    print("connection estabilished")
    username = "pppp"
    mail="gggg@gmail.com"
    phone="08033445566"


    # Preparing SQL query to INSERT a record into the database.
    sql = """INSERT INTO user_table(
    user_name,user_mailaddress,user_phone)
    VALUES ("""+username+""","""+mail+""","""+phone+""")"""
    print("executing query")
    print(sql)
    try:
        # Executing the SQL command
        cursor.execute(sql)

        # Commit your changes in the database
        mysql.connection.commit()

        print("success")

    except:

        print("error")
