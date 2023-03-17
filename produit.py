class Produit(): 
    def __init__(self,name_,descri_,price_,quantity_,categ_):
        self.name = name_
        self.descri = descri_
        self.price = price_
        self.quantity = quantity_
        self.categ = categ_
    
    def addProduct(self,cursor):
        query = f"INSERT INTO produit (nom,description,prix,quantité,id_categorie) VALUES ('{self.name}','{self.descri}',{self.price},{self.quantity},{self.categ});"
        cursor.execute(query)

    def changeProduct(self,cursor,id):
        query =  query = f"UPDATE produit SET nom = '{self.name}', description = '{self.descri}',prix = {self.price}, quantité = {self.quantity},id_categorie = {self.categ} WHERE id = {id};"
        cursor.execute(query)
        