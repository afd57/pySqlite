#denemeFramework
import model
import sqlitedbClass
import model2


if __name__ == "__main__":
    print("Borning new entity framework :D")
    
    #item1 = model.Item("Users","01/08","Frenka2")
    
    item1 = model2.Student("student","Frenka","English",90)
    item2 = model2.Student("student","Frenka","Turkish",80)
    item3 = model2.Student("student","Frenka","Math",100)
    
    tst1 = sqlitedbClass.MySqlite("deneme2.db")
    tst1.addInstancetoDB(item1);
    tst1.addInstancetoDB(item2);
    tst1.addInstancetoDB(item3);