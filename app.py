#!flask/bin/python
from flask import Flask
from flask import request
import json
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="weavedin"
)

mycursor = mydb.cursor()

@app.route('/', methods=['GET'])
def home():
    return 'hello'

@app.route('/showAll', methods=['POST'])
def showAll():
    mycursor.execute("Select * from invoice")
    result = mycursor.fetchall()
    print result
    return "result"

@app.route('/createInvoice', methods=['POST'])
def createInvoice():
    req = request.form
    # print req

    # keyList = ""
    # valList = ""

    # for key in req:

    #     keyList += key + ","

    #     if key == "created_at" or key == "invoice_id":
    #         valList += "'" + req[key] + "', "
    #     else:
    #         valList += req[key] + ", "

    # keyList += "\b"
    # valList += "\b\b"

    # # print keyList
    # # print valList

    # sql= "INSERT INTO invoice ("+ keyList + ") values (" + valList + ")"
    print req['created_at']

    sql = "INSERT INTO invoice (invoice_id,created_at,tax,discount,discount_percent,total,tax_percent,subtotal) values ('"+ req['invoice_id']+ "', '" + req['created_at'] + "'," + req['tax'] + "," + req['discount'] + "," + req['discount_percent'] + "," + req['total'] + "," + req['tax_percent'] + "," + req['subtotal'] + ")"

    print sql

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

    return json.dumps(req)

@app.route('/createItems', methods=['POST'])
def createItems():
    x = request.form
    print x
    return json.dumps(x)

if __name__ == '__main__':
    app.run(debug=True)