#db Template

class Item:
    myStruct = ["tarih text","name text"]
    def __init__(self,tableName,tarih,name):
        self.tableName = tableName
        self.tarih = tarih
        self.name = name
