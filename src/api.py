# Author : Snehashish Laskar
# Date   : 1st November 2022
# Version : 0.1.0
# Copyright (C) Snehashish Laskar 2023
# LICENSE: MIT OPen Source Software License

# Importing necessary modules
from flask import Flask, request, jsonify, abort
from auth import *

if sys.platform == "darwin":
    if not os.path.exists("/Library/Caches/.menousdb/config.json"):
        with open("/Library/Caches/.menousdb/config.json", "w") as file:
            json.dump({
                "mode":"json",
                "port":5555
            }, file)
    with open("/Library/Caches/.menousdb/config.json", "r") as file:
        settings = json.load(file)
elif sys.platform == "win32":
    if not os.path.exists(os.getenv("APPDATA")+"\\MenoudDb"+"\\config.json"):
        with open(os.getenv("APPDATA")+"\\MenoudDb"+"\\config.json", "w") as file:
            json.dump({
                "mode":"json",
                "port":5555
            } ,file)
    with open(os.getenv("APPDATA")+"\\MenoudDb"+"\\config.json", "r") as file:
        settings = json.load(file)
else:
    if not os.path.exists("/usr/local/bin/menousdb/config.json"):
        with open("/usr/local/bin/menousdb/config.json", "w") as file:
            json.dump({
                "mode":"json",
                "port":5555
            }, file)
    with open("/usr/local/bin/menousdb/config.json", "r") as file:
        settings = json.load(file)

"""
methods included:
 
1: read-db GET 
2: create-db POST
3: check-db-exists GET
4: del-database DELETE
5: check-table-exists GET
6 : get-table GET
7: create-table POST
8: insert-into-table POST
9: select-where GET
10: select-columns GET
11: select-columns-where GET
12: delete-where DELETE
13: delete-table DELETE
14: update-table POST

"""


mode = settings["mode"]
port = settings["port"]

if mode == "json":
    from models import *
elif mode=="sql":
    from sql import *
app = Flask(__name__)

@app.route('/read-db', methods=['GET'])
def index():

    if request.method == 'GET':
        try:
            key = request.headers['key']
            db  = request.headers.get('database')

            if check_key(key):
                database = dataBase(db)
                if database.check_database_exists():
                    data = database.read_db()
                    return jsonify(data)
                else:
                    return 'Database does not exist'
            else:
                abort(403)
        except Exception as ex:
            return str(ex)
    else:
        abort(403)

@app.route('/create-db',methods = ['POST'])
def createDb():
    try:
        key= request.headers['key']
        db = request.headers['database']

        if check_key(key):
            database = dataBase(db)
            if database.check_database_exists():
                return 'Error: database already exists'
            else:
                database.create_database()
                return 'Successfully created database'

        else:
            abort(403)
    except Exception as ex:
        return str(ex)

@app.route('/check-db-exists', methods = ['GET'])
def checkDbExists():
    try:
        key = request.headers['key']
        db  = request.headers['database']

        if check_key(key):
            database = dataBase(db)
            if database.check_database_exists():
                return 'True'
            else:
                return 'False'
        else:
            abort(403)
    except Exception as ex:
        return str(ex)

@app.route('/del-database', methods = ['DELETE'])
def delDatabase():
    try:
        key = request.headers['key']
        db = request.headers['database']

        if check_key(key):
            database = dataBase(db)
            database.delete_database()
            abort(200)
        else:
            abort(403)
    except Exception as ex:
        return str(ex)

@app.route('/check-table-exists', methods=['GET'])
def checkTableExists():
    try:
        key = request.headers['key']
        database = request.headers['database']
        table = request.headers['table']

        if check_key(key):
            db = dataBase(database)
            if db.check_table_exists(table):
                return 'True'
            else:
                return 'False'
        else:
            abort(403)

    except Exception as ex:
        return str(ex)

@app.route("/get-table", methods=["GET"])
def getTable():
    try:
        key = request.headers['key']
        database = request.headers['database']
        table = request.headers['table']
        if check_key(key):
            db = dataBase(database)
            return jsonify(db.get_table(table))
        else:
            abort(403)
    except Exception as ex:
        return str(ex)

@app.route('/create-table', methods=['POST'])
def createTable():
    try:
        key = request.headers['key']
        database = request.headers['database']
        table = request.headers['table']
        print(key,database,table)
        attributes = request.json['attributes']
        if check_key(key):
            db = dataBase(database)
            db.create_table(table, attributes)
            abort(200)
        else:
            abort(403)
    except Exception as ex:
        return str(ex)

@app.route('/insert-into-table', methods = ['POST'])
def insertInto():
    try:
        key = request.headers['key']
        database  = request.headers['database']
        table = request.headers['table']
        values = request.json['values']

        if check_key(key):
            db = dataBase(database)
            db.add_value_to_table(table, values)
            abort(200)
        else:
            abort(403)
    except Exception as ex:
        return str(ex)


@app.route('/select-where', methods=['GET'])
def selectWhere():
    try:
        key = request.headers['key']
        database = request.headers['database']
        table = request.headers['table']
        conditions = request.json['conditions']

        if check_key(key):
            db = dataBase(database)
            ans = db.select_where(table, conditions)
            return jsonify(ans)
        else:
            abort(403)
    except Exception as ex:
        return str(ex)


@app.route('/select-columns', methods=['GET'])
def select_columns():
    try:
        key = request.headers['key']
        database = request.headers['database']
        table = request.headers['table']
        columns = request.json['columns']

        if check_key(key):
            db = dataBase(database)
            ans = db.select_columns(table, columns)
            return jsonify(ans)
        else:
            abort(403)
    except Exception as ex:
        return str(ex)


@app.route('/select-columns-where', methods=['GET'])
def select_columns_where():
    try:
        key = request.headers['key']
        database = request.headers['database']
        table = request.headers['table']
        columns = request.json['columns']
        conditions = request.json['conditions']

        if check_key(key):
            db = dataBase(database)
            ans = db.select_columns_where(table, columns, conditions)
            return jsonify(ans)
        else:
            abort(403)
    except Exception as ex:
        return str(ex)
    

@app.route('/delete-where', methods = ['DELETE'])
def delete_where():
    try:
        key = request.headers['key']
        database = request.headers['database']
        table = request.headers['table']
        conditions = request.json['conditions']

        if check_key(key):
            db = dataBase(database)
            ans = db.delete_where(table, conditions)
            return jsonify(ans)
        else:
            abort(403)
    except Exception as ex:
        return str(ex)
    

@app.route('/delete-table', methods = ['DELETE'])
def delete_table():

    try:
        key = request.headers['key']
        database = request.headers['database']
        table = request.headers['table']

        if check_key(key):
            db = dataBase(database)
            ans = db.delete_table(table)
            return jsonify(ans)
        else:
            abort(403)

    except Exception as ex:
        return jsonify(ex)
    

@app.route('/update-table' , methods=['POST'])
def update_table():

    try:
        key = request.headers['key']
        database = request.headers['database']
        table = request.headers['table']
        conditions = request.json['conditions']
        values = request.json['values']

        if check_key(key):
            db = dataBase(database)
            ans = db.update_table(table, conditions, values)
            return jsonify(ans)
        else:
            abort(403)

    except Exception as ex:
        return jsonify(ex)


@app.route('/get-databases', methods=['GET'])
def getDatabases():
    try:
        key = request.headers['key']
        if check_key(key):
            data = get_databases()
            return jsonify(data)
        else:
            abort(403)
    except Exception as ex:
        return jsonify(ex)
    
@app.route("/check-login", methods=["GET"])
def check_login():
    try:
        uname = request.headers['username']
        pw = request.headers['password']
        if Login(uname,pw) != False:
            return Login(uname,pw)
        else:
            return "Inccorect"
    except Exception as ex:
        return jsonify(ex)

def checkCredentials(uname,pw):
    db=dataBase("authdata")
    table=db.read_db()['vaccinator_auth']
    for i in table:
        if i != "attributes":
            if table[i]['username'] == uname and table[i]['password'] == pw:
                return True
    return False

@app.route('/verify/<username>/<password>', methods=['GET'])
def checkCreds(username, password):
    if checkCredentials(username, password):
        return 'True'
    return 'False'


