from flask import Flask,render_template,redirect,url_for,request
import sqlite3 as sql
import mysql.connector
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
# # @app.route("/")
# # @app.route("/home")
# def home():
#     # return"<h1>hello home page</h1>"
#     return render_template("./home.html")
# @app.route("/account")   
# def account():
#     return"<h1>welcome to account page<h1>"  
# @app.route("/account/mass")
# def mass():
#     return"<h1>hi flask world<h1>"

# @app.route("/king/<name>/<int:age>")
# def king(name,age):
#     #  return render_template("./villa.html")
#     # if age>=18:
#     #     return redirect("/account")
#     # else:    
#     #     return redirect(url_for("mass"))   
#     return f"the user name is {name},and the age is {age}"
# @app.route('/i_types/<int:a>')
# def i_type(a):
#     return f"the types is {a}"
# @app.route('/s_types/<string:a>')
# def s_type(a):
#     return f"the types is {a}"
# @app.route('/f_types/<float:a>')
# def f_type(a):
#     return f"the types is {a}"
# @app.route("/variable")
# def variable():
#     name="giri"
#     return render_template("./jinja.html",name=name)
# @app.route("/admin")
# def admin():
#     return "<h2>welcome admin <h2>"

# @app.route("/user")
# def user():
#     return "<h2>welcome user <h2>"
# @app.route("/manager")
# def manager():
#     return "<h2>welcome manager <h2> "   
# @app.route("/tl")
# def tl():
#     return "<h2>welcome tl <h2>"
# @app.route("/input/<name>")
# def input(name):
#     if name=="admin":
#         return redirect(url_for("admin"))
#     elif name=="user":
#         return redirect(url_for("user"))
#     elif name=="manager":
#         return redirect(url_for("manager")) 
#     elif name=="tl":
#         return redirect(url_for("tl"))
#     else:
#         return "<h2> enter valid name <h2>"
# @app.route("/help")
# def help():
#     new = {
#     "gp": {
#         "name": "mari",
#         "age": 24,
#         "tamil": 85,
#         "english": 80,
#         "maths": 95,
#         "science": 95,
#         "average":90,
#     }
#     }
#     return render_template("jinja2.html",new=new)
# @app.route("/base")
# def base():
#     return render_template("base.html")
# @app.route("/contact")
# def contact():
#     return render_template("contact.html")
# @app.route("/aboutas")
# def aboutas():
#     return render_template("aboutas.html")
# @app.route("/acc")
# def acc():
#     return render_template("acc.html")
# # @app.route("/")
# @app.route("/form")
# def form():
#     return render_template("register.html")
# #WTforms
# @app.route("/form2",methods=['POST'])
# def form2():
#     name=request.form["username"]#Error
#     password=request.form.get("pass") #None
#     confirm_password=request.form.get("c_psw")
#     email=request.form.get("email")
    
#     if not name or not password or not confirm_password or not email:
#         return "❌ All Values are Required"
#     if len(name)<=3:
#         return "❌ Your Name must be 3 characters"
#     if len(password)<=3:
#         return "❌ The Password is must be 4 values"
#     if password!=confirm_password:
#         return "❌ The Password is mismatch"
#     if "@" not in email or "." not in email:
#         return "❌ Enter Valid Email"
    
#     return render_template("login.html",name=name,password=password,confirm_password=confirm_password,email=email)
# @app.route("/end")
# def end():
#     return render_template("index.html")
# @app.route("/home",methods=["POST"])
# def home():
#     name=request.form.get("username")
#     password=request.form.get("password")
#     conn=sql.connect("kps.db") 
#     cur=conn.cursor() 
#     cur.row_factory=sql.Row
#     cur.execute("insert into stude(name,password)values(?,?)",(name,password))
#     cur.execute("select * from stude")
#     rows=cur.fetchall()
#     conn.commit()
#     conn.close()
#     return render_template("endlogin.html",rows=rows) 
# # @app.route("/")
# # def layout():
# #     con=sql.connect("kps.db")
# #     con.row_factory=sql.Row
# #     cur=con.cursor()
# #     cur.execute("select * from user")
# #     data=cur.fetchall()
# #     con.commit()
# #     return render_template("layout.html",datas=data)


# # @app.route("/get")
# # def get():
# #     return render_template("add_user.html")
    
    
# # @app.route("/add",methods=["POST"])
# # def add():
# #     if request.method=='POST':
# #         name=request.form.get("username")
# #         email=request.form.get("email")
    
# #         con=sql.connect("kps.db")
# #         con.row_factory=sql.Row
# #         cur=con.cursor()
# #         cur.execute("insert into user(username,email) values(?,?)",(name,email))
# #         con.commit()
# #         # con.close()
# #         # return render_template("layout_sql.html")
# #     return redirect("/")
# # @app.route("/getedit/<id>",methods=["POST","GET"]) 
# # def getedit(id):
# #      con=sql.connect("kps.db")
# #      con.row_factory=sql.Row
# #      cur=con.cursor()
     
# #      cur.execute("select * from user where userid=?",(id))
# #      data=cur.fetchone()
# #      con.commit()
# #      return render_template("edit.html",datas=data)
     
# # @app.route("/update/<int:userid>",methods=["POST"]) 
# # def update(userid):
# #     name=request.form.get("username")
# #     email=request.form.get("email")
# #     con=sql.connect("kps.db")
# #     con.row_factory=sql.Row
# #     cur=con.cursor()
# #     cur.execute("UPDATE USER SET username=?,email=?",(name,email,id))
# #     con.commit()
# #     return redirect("/") 
# # @app.route("/delete/<id>",methods=["POST","GET"])  
# # def delete(id):
# #     con=sql.connect("kps.db")
# #     con.row_factory=sql.Row
# #     cur=con.cursor()
# #     cur.execute("delete from user where userid=?",(id))
# #     con.commit()
# #     return redirect("/") 
# @app.route("/registers")
# def registers():
#     # con=sql.connect("kps.db")
#     # con.row_factory=sql.Row
#     # cur=con.cursor()
#     # cur.execute("select * from reg")
#     # data=cur.fetchall()
#     # con.commit()
#     return render_template("register form.html")


# @app.route("/get",methods=["POST"])
# def get():
#     if request.method=="POST":
#         password=request.form.get("password" )
#         confirmpassword=request.form.get("confirm_password")
#         if password==confirmpassword:
#             return render_template("login2.html")
#         else:
#             return f"your password is incorrect"
# @app.route("/end",methods=[""])
# def end():
#     return f"yes"
    
    
# @app.route("/add",methods=["POST"])
# def add():
#     if request.method=='POST':
#         name=request.form.get("username")
#         email=request.form.get("email")
#         gender=request.form.get("gender")
    
#         con=sql.connect("kps.db")
#         con.row_factory=sql.Row
#         cur=con.cursor()
#         cur.execute("insert into reg(username,email) values(?,?)",(name,email))
#         con.commit()
#         # con.close()
#         # return render_template("layout_sql.html")
#     return redirect("/registers")
# @app.route("/getedit/<id>",methods=["POST","GET"]) 
# def getedit(id):
#      con=sql.connect("kps.db")
#      con.row_factory=sql.Row
#      cur=con.cursor()
     
#      cur.execute("select * from reg where userid=?",(id))
#      data=cur.fetchall()
#      con.commit()
#      return render_template("edit.html",datas=data)
     
# @app.route("/update/<int:userid>",methods=["POST"]) 
# def update(userid):
#     name=request.form.get("username")
#     email=request.form.get("email")
#     con=sql.connect("kps.db")
#     con.row_factory=sql.Row
#     cur=con.cursor()
#     cur.execute("UPDATE USER SET username=?,email=?",(name,email,id))
#     con.commit()
#     return redirect("/registers") 
# @app.route("/delete/<id>",methods=["POST","GET"])  
# def delete(id):
#     con=sql.connect("kps.db")
#     con.row_factory=sql.Row
#     cur=con.cursor()
#     cur.execute("delete from reg where userid=?",(id))
#     con.commit()
#     return redirect("/registers") 
# @app.route("/")
# def create_table():
#     conn=mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="root",
#         database="emp"
#     )
#     cur=conn.cursor()
#     cur.execute("create table if not exists people(id int auto_increment primary key,name varchar(100),mark int)")
#     conn.commit()
#     conn.close()
#     return render_template()




# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' #Give The location of the database
import os
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "kps.db")
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # disabling the warnings

db=SQLAlchemy(app) 

#Initialize the table and column here
class Userv(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)

#create the table and column here
with app.app_context():
    db.create_all()
    
    #insert the data here
    user = Userv(name="John",email="John@gmail.com") 
    db.session.add(user)
    db.session.commit()
    #This is for confirmation messgae
    print("Table created and user add successfully...")




   
    if __name__=="__main__":
     app.run(debug=True)
    # app.run(host="0.0.0.0",port=8000)


    