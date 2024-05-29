from database.DAO import DAO
class Model:
    def __init__(self):
        self.DAO = DAO()

    def get_anni(self):
        return self.DAO.get_anni_dao()

    def get_brand(self):
        return self.DAO.get_brand_dao()

    def get_retailer(self):
        return self.DAO.get_retailer_dao()

    def get_top_vendite(self, anno, brand, retailer):
        return self.DAO.get_top_vendite_dao(anno, brand, retailer)
