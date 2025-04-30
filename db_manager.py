# db_manager.py
import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',             # Change if your MySQL username is different
        password='', # Change this to your actual MySQL password
        database='lankatravelmate'
    )
    return connection# Database connection manager
