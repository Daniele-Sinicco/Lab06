from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():
    def __init__(self):
        pass

    def get_anni_dao(self):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Connection error")
            return
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT DISTINCT YEAR(Date) AS Year FROM go_daily_sales"""
        cursor.execute(query)
        for row in cursor:
            result.append(row["Year"])
        cursor.close()
        cnx.close()
        return result

    def get_brand_dao(self):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Connection error")
            return
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT DISTINCT Product_brand AS Brand FROM go_products"""
        cursor.execute(query)
        for row in cursor:
            result.append(row["Brand"])
        cursor.close()
        cnx.close()
        return result

    def get_retailer_dao(self):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Connection error")
            return
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM go_retailers"""
        cursor.execute(query)
        for row in cursor:
            result.append(Retailer(row["Retailer_code"], row["Retailer_name"], row["Type"], row["Country"]))
        cursor.close()
        cnx.close()
        return result
