#db Template

class Student:
    myStruct = ["isim text","ders text","puan int"]
    def __init__(self,tableName,isim,ders,puan):
        self.tableName = tableName
        self.isim = isim
        self.ders = ders
        self.puan = puan;
