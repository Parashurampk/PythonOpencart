import mysql.connector


class DBConnection:

    @staticmethod
    def get_connection():

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="opencart"
        )

        return conn