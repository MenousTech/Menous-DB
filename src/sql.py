import sqlite3
import os
import sys
import json
import random

if sys.platform == "darwin":
    if not os.path.exists("/Library/Caches/.menousdb"):
        os.mkdir("/Library/Caches/.menousdb")
    if not os.path.exists("/Library/Caches/.menousdb/data"):
        os.mkdir("/Library/Caches/.menousdb/data")
    if not os.path.exists("/Library/Caches/.menousdb/authdata"):
        os.mkdir("/Library/Caches/.menousdb/data")
    if not os.path.exists("/Library/Caches/.menousdb/config.json"):
        with open("/Library/Caches/.menousdb/config.json", "w") as file:
            json.dump({
                "mode":"json",
                "port":5555
            }, file)
    path = "/Library/Caches/.menousdb/data"

elif sys.platform == "win32":
    if not os.path.exists(os.getenv("APPDATA")+"\\MenoudDb"):
        os.mkdir(os.getenv("APPDATA")+"\\MenoudDb")
    if not os.path.exists(os.getenv("APPDATA")+"\\MenoudDb"+"\\data"):
        os.mkdir(os.getenv("APPDATA")+"\\MenoudDb/data")
    if not os.path.exists(os.getenv("APPDATA")+"\\MenoudDb"+"\\authdata"):
        os.mkdir(os.getenv("APPDATA")+"\\MenoudDb\\authdata")
    if not os.path.exists(os.getenv("APPDATA")+"\\MenoudDb"+"\\config.json"):
        with open(os.getenv("APPDATA")+"\\MenoudDb"+"\\config.json", "w") as file:
            json.dump({
                "mode":"json",
                "port":5555
            } ,file)
    path = os.getenv("APPDATA")+"\\MenoudDb"+"\\data"

else:
    if not os.path.exists("/usr/local/bin/menousdb"):
        os.mkdir("/usr/local/bin/menousdb")
    if not os.path.exists("/usr/local/bin/menousdb/data"):
        os.mkdir("/usr/local/bin/menousdb/data")
    if not os.path.exists("/usr/local/bin/menousdb/authdata"):
        os.mkdir("/usr/local/bin/menousdb/authdata")
    if not os.path.exists("/usr/local/bin/menousdb/config.json"):
        with open("/usr/local/bin/menousdb/config.json", "w") as file:
            json.dump({
                "mode":"json",
                "port":5555
            }, file)

    path="/usr/local/bin/menousdb/data"

class dataBase:

    def __init__(self,name):
        self.name = name


    def read_db(self):
        d = sqlite3.connect(os.path.join(path, self.name))
        db = d.cursor()
        data = {}
        db.execute("SELECT name FROM sqlite_master WHERE type='table'")
        for i in db.fetchall():
            table = i[0]
            cc = db.execute(f"SELECT * FROM {table}")
            atts = [d[0] for d in cc.description]
            data[table] = {"attributes": atts}
            for i in db.fetchall():
                dic = {}
                for j in atts:
                    dic[j] = i[atts.index(j)] 
                data[table][str(random.randint(100, 100000))] = dic
        return data
    

    def create_database(self):
        # CREATE DATABASE name
        if os.path.exists(path + f"/{self.name}.db"):
            raise Exception("Database already exists")
        else:
            with open(path + f"/{self.name}.db", 'w') as file:
                json.dump({}, file, indent=True)


    def check_database_exists(self):
        if os.path.exists(path + f"/{self.name}.db"):
            return True
        else:
            return False


    def delete_database(self):
        if self.check_database_exists():
            os.remove(path + f'/{self.name}.db')
        else:
            raise Exception("Database files not found")
        
    
    def check_table_exists(self, table: str):
        data = self.read_db()
        if table not in data.keys():
            return False
        else:
            return True
        

    def create_table(self,table, attributes):
        if not self.check_database_exists():
            raise Exception("Database files not found")
        if self.check_table_exists(table):
            raise Exception("Table already exists")
        d = sqlite3.connect(os.path.join(path, self.name))
        db = d.cursor()
        q = f"CREATE TABLE IF NOT EXISTS {table}("
        for i in attributes:
            q += str(i)
            if attributes.index(i) == len(attributes) - 1:
                q += ")"
            else:
                q += ","
        db.execute(q)
        d.commit()

    def get_table(self, table):
        if self.check_database_exists() and self.check_table_exists(table):
            return self.read_db()[table]
        else:
            raise Exception("Table does not exist or Database does not exist")
        
    def add_value_to_table(self,table, values):
        if self.check_database_exists() == False:
            raise Exception("Database does not exist")
        elif self.check_table_exists(table) == False:
            raise Exception("Table does not exist")
        vAtts = []
        data = self.read_db()

        if table not in data:
            raise Exception("table not found")
        
        for i in values:
            vAtts.append(i)

        atts = data[table]["attributes"]
        
        d = sqlite3.connect(os.path.join(path, self.name))
        db = d.cursor()
        q = f"INSERT INTO {table}("

        count = 0
        for i in atts:
            if count == len(atts)-1:
                q += i + ")"
            else:
                q += i + ","

            count += 1

        q += " VALUES("

        vals = []
        for i in values:
            vals.append(values[i])
        for i in values:
            vals[atts.index(i)] = values[i]
        
        count = 0
        for i in vals:
            if count == len(vals)-1:
                q += "'"+str(i)+"'"+")"
            else:
                q += "'"+str(i)+"'"+","
            count += 1

        db.execute(q)
        d.commit()

    # represents SELECT * FROM table WHERE condition
    def select_where(self, table: str, conditions: dict):
        if self.check_database_exists() == False:
            raise Exception("Database does not exist")
        elif self.check_table_exists(table) == False:
            raise Exception("Table does not exist")
        else:
            answers=[]

            q = f"SELECT * FROM {table} WHERE "
            for i in conditions:
                q += str(i) + "="+"'"+str(conditions[i])+"'"+" AND "
            q = q[:-5]
            d = sqlite3.connect(os.path.join(path, self.name))
            db = d.cursor()
            db.execute(q)
            result = db.fetchall()
            cc = db.execute(f"SELECT * FROM {table}")
            atts = [d[0] for d in cc.description]
        
            for i in result:
                temp = {}
                for j in atts:
                    temp[j] = i[atts.index(j)]
                answers.append(temp)
            return answers

            # represets SELECT cloumns FROM table
    def select_columns(self, table: str, columns: list):
        if self.check_database_exists() == False:
            raise Exception("Database does not exist")
        elif self.check_table_exists(table) == False:
            raise Exception("Table does not exist")
        else:
            ans = {}
            q = "SELECT "
            for i in columns:
                q += i + ","
            q = q[:-1] + f" FROM {table}"

            d = sqlite3.connect(os.path.join(path, self.name))
            db = d.cursor()
            db.execute(q)
            temp = db.fetchall()

            ans = {

            }
            length = len(columns)
            for i in range(0, length):
                ans[columns[i]] = []
                for j in temp:
                    ans[columns[i]].append(j[i])


            return ans
    

    def select_columns_where(self, table: str, columns: list, conditions: dict):
        if self.check_database_exists() == False:
            raise Exception("Database does not exist")
        elif self.check_table_exists(table) == False:
            raise Exception("Table does not exist")
        else:
            # Start forming the SQL query
            query = "SELECT "
            query += ", ".join(columns) + f" FROM {table}"
            
            # Add WHERE conditions
            if conditions:
                condition_statements = []
                for column, value in conditions.items():
                    if isinstance(value, str):
                        condition_statements.append(f"{column} = '{value}'")
                    else:
                        condition_statements.append(f"{column} = {value}")
                query += " WHERE " + " AND ".join(condition_statements)
            
            # Execute the query
            conn = sqlite3.connect(os.path.join(path, self.name))
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            
            # Map the results to columns
            result = {col: [] for col in columns}
            for row in rows:
                for col, value in zip(columns, row):
                    result[col].append(value)
            
            conn.close()
            return result
        
    def delete_where(self,table,conditions):
        q = f"DELETE FROM {table} WHERE "
        for i in conditions:
            q += str(i)+"="+"'"+str(conditions[i])+"'"+" AND "
        q = q[:-5]

        d = sqlite3.connect(os.path.join(path, self.name))
        db = d.cursor()

        db.execute(q)
        d.commit()
        
    def delete_table(self, table) -> None:
        if self.check_database_exists() == True:
            q = f"DROP TABLE {table}"
            d = sqlite3.connect(os.path.join(path, self.name))
            db = d.cursor()

            db.execute(q)
            d.commit()
        elif self.check_database_exists() == False:
            raise Exception('Database does not exist')
        else:
            raise Exception('Table does not exist')
        
    def update_table(self,table, conditions,values):
        q = f"UPDATE {table} SET "
        x = 1
        for i in values:
            if x == len(values):
                q+= str(i) + "="+"'"+str(values[i])+"'"+" "
            else:
                q+= str(i) + "="+"'"+str(values[i])+"'"+", "
            x += 1
        q += " WHERE "
        x = 1
        for i in conditions:
            if x == len(conditions):
                q += str(i)+"="+"'"+str(conditions[i])+"'"+" "
            else:
                q += str(i)+"="+"'"+str(conditions[i])+"'"+" AND "
            x += 1
        print(q)
        d = sqlite3.connect(os.path.join(path, self.name))
        db = d.cursor()

        db.execute(q)
        d.commit()


def get_databases():
    
    databases = []
    for i in os.listdir(path):
        if ".db" in i:
            databases.append(i.replace(".db", ""))
    return databases
