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
    
    return render_template("staff.html")

@app.route("/mark")
def insert_mark():
    return render_template("mark.html")   

@app.route("/read_stu")
def read_stude():
    return render_template("read_student.html")   

@app.route("/delete")
def delete_data():
    
    return render_template("delete.html")

@app.route("/update")
def update_data():
    
    return render_template("update.html")

@app.route("/read")
def read():
    students = mycol.find()
    students= list(students)
    return render_template("View_students.html",students=students)

@app.route("/grade")
def read_grade():
    students = mycol2.find()
    students= list(students)
    return render_template("view_grade.html",students=students)

@app.route("/update_email")
def update():
    name=request.args.get("name")
    new_email = request.args.get("new_email")
    myquery = {"name":name}
    newvalues= {"$set" : {"email": new_email}}
    mycol.update_one(myquery,newvalues)
    x="Record updated"
    return render_template("response.html",res=x)

@app.route("/update_marks")
def update_grade():
    mycol2.update_many(
    {"Total": { "$gt": "30" } },
        {
            "$set": { "passed" : "Pass" }
        }
)
    x="Record updated"
    return render_template("response.html",res=x)


@app.route("/add_marks")
def Add_marks():
    id=request.args.get("m1")
    name = request.args.get("m2")
    dbms= request.args.get("num1")
    os= request.args.get("num2")
    daa= request.args.get("num3")
    se= request.args.get("num4")
    we= request.args.get("num5")
    sum = request.args.get("sum")
    myVal = {"id":id,"name":name,"DBMS":dbms,"OS":os,"DAA":daa,"SE":se,"WEBDESIGN":we,"Total":sum}
    mycol2.insert_one(myVal)
    x="Record Inserted"
    return render_template("response.html",res=x)

@app.route("/remove")
def delete():
    name = request.args.get("name")
    myquery = {"name": name}
    mycol.delete_one(myquery)
    x="Record delete"
    return render_template("delete_response.html",res=x)

if __name__ == '__main__':
   app.run(debug=True,port=3000)