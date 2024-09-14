from flask import Flask, request, render_template

import subprocess as sp
import json

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["Student"]

mycol2  = mydb["Teacher"]
app = Flask(__name__)


@app.route("/")
def my_home():
    
    return render_template("student.html")

@app.route("/insert")
def add_data():
    
    return render_template("insert.html")

@app.route("/find")
def find_data():
    
    return render_template("find.html")

@app.route("/detail")
def find_detail():
    return render_template("detail.html")   


@app.route("/mark")
def insert_mark():
    return render_template("mark.html")   

@app.route("/search")
def find():
    name=request.args.get("name")
    myquery = {"name":name}
    filter = {"_id": 0}
    cursor=mycol2.find_one(myquery,filter)
    print(cursor)
    return render_template("View_result.html",res=cursor)

@app.route("/stu_detail")
def detail():
    id=request.args.get("id")
    myquery = {"id":id}
    filter = {"_id": 0}
    cursor=mycol.find_one(myquery,filter)
    print(cursor)
    return render_template("view_detail.html",res=cursor)

@app.route("/add")
def insert():
    id=request.args.get("s1")
    name = request.args.get("t1")
    age = request.args.get("t2")
    email=request.args.get("t3")
    date=request.args.get("t5")
    gender=request.args.get("gender")
    myVal = {"id":id,"name":name,"age":age,"email":email,"date":date,"gender":gender}
    mycol.insert_one(myVal)
    x="Record Inserted"
    return render_template("response.html",res=x)

if __name__ == '__main__':
   app.run(debug=True)