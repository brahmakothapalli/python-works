import mysql.connector


def get_db_connection():
    db_connector = mysql.connector.connect(host="localhost", user="root", passwd="root", database="qababudb")
    return db_connector

# db_cursor.execute("create database qababudb")

# db_cursor.execute("show databases")


# db_cursor.execute("create database school")

# db_cursor.execute("Use school")

# db_cursor.execute("create table employee(Name varchar(50), Role varchar(20), Id int(20), Salary int(20))")
