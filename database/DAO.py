from database.DB_connect import DBConnect
from model.retailer import Retailer
from model.vendite import Vendite


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

    def get_top_vendite_dao(self, anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select * from go_daily_sales where year (Date) = coalesce(%s, year(Date)) and 
        Retailer_code = coalesce(%s, Retailer_code) and
         Product_number in (select Product_number from go_products where Product_brand = coalesce(%s, Product_brand))"""
        cursor.execute(query, (anno, retailer, brand))
        vendite = []
        result = []
        for row in cursor:
            vendite.append(Vendite(row['Date'], (row['Quantity']*row['Unit_sale_price']), row['Retailer_code'], row['Product_number']))
        vendite.sort(reverse=True)
        if len(vendite) >= 5:
            result = vendite[:5]
        else:
            result = vendite[:len(vendite)]
        cursor.close()
        cnx.close()
        return result


