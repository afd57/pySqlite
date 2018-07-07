#Db class
import sqlite3

    
class MySqlite:
    def __init__(self,dbName):
        self.dbName = dbName
        
    def addInstancetoDB(self,model):
        self.createDB(model)
        
        conn = sqlite3.connect(self.dbName)
        c = conn.cursor()
        
        values = []
        for i in range(len(model.myStruct)):
            values.append(getattr(model,model.myStruct[i].split(' ')[0]))
        
        sqlString = "insert into "+model.tableName+" values ("+str(values).strip("[]")+")"
        print(sqlString)
        c.execute(sqlString)
        conn.commit()
        conn.close()
        
    def createDB(self,model):
        conn = sqlite3.connect(self.dbName)
        c = conn.cursor()
        modelStruct = self.createQuery(model)
        sqlString = "CREATE TABLE IF NOT EXISTS "+model.tableName+" ("+modelStruct+")";
        print(sqlString)
        c.execute(sqlString)
        conn.commit()
        conn.close()

    def createQuery(self,model):
        sqlQuery = "";
        for dbPropertie in model.myStruct:
            sqlQuery = sqlQuery + dbPropertie +','
        if sqlQuery[-1] == ',':
            return sqlQuery[:-1]
        else:
            return sqlQuerys
    
