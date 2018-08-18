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
    return json.dumps(result)

@app.route('/filterInvoice', methods=['POST'])
def filterInvoice():
    req = request.form['invoice_id']
    mycursor.execute("Select * from invoice where invoice_id LIKE '%"+req+"%'")
    result = mycursor.fetchall()
    print result
    return json.dumps(result)

@app.route('/getItems', methods=['POST'])
def getItems():
    req = request.form['invoice_id']
    mycursor.execute("Select * from items where invoice_id = '" + req + "'")
    result = mycursor.fetchall()
    print result
    return json.dumps(result)

@app.route('/createInvoice', methods=['POST'])
def createInvoice():
    req = request.form
    
    default_val = ""

    name = req.get('name', default_val)
    email = req.get('email', default_val)
    phone = req.get('phone', default_val)
    address = req.get('address', default_val)
    pincode = req.get('pincode', default_val)

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

    sql = "INSERT INTO invoice (invoice_id,created_at,tax,discount,discount_percent,total,tax_percent,subtotal, name, email, phone, address, pincode) values ('"+ req['invoice_id']+ "', '" + req['created_at'] + "'," + req['tax'] + "," + req['discount'] + "," + req['discount_percent'] + "," + req['total'] + "," + req['tax_percent'] + "," + req['subtotal'] + ",'" + name + "','" + email + "','" + phone + "','" + address + "','" + pincode + "')"

    print sql

    try:
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        return json.dumps(req)
    except:
        return "exception caught"


@app.route('/createItems', methods=['POST'])
def createItems():
    req = request.form
    # print req



    sql = "INSERT INTO items (invoice_id, name, quantity, price) values ('" + req['invoice_id'] + "','" + req['name'] + "','" + req['quantity'] + "','" + req['price'] + "')"

    print sql

    try:
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        return json.dumps(req)
    except:
        return "exception caught"


if __name__ == '__main__':
    app.run(debug=True)