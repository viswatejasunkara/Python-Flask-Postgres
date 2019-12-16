from _ast import Add

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template,request,redirect,url_for
from forms import AddForm
import datetime
import datetime
from sqlalchemy import extract

# db_string = 'postgres://postgres:475951@localhost:5432/postgres'


app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:475951@localhost:5432/postgres'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# import os
# os.urandom(16)
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_REGISTERABLE'] = True
app.debug= True
db = SQLAlchemy(app)

from models import *

@app.route('/page1',methods=['GET'])
def page1():

    emp = Employees.query.filter((extract('day', Employees.dateofbirth) == datetime.datetime.today().day)).filter(
        extract('month', Employees.dateofbirth) == datetime.datetime.today().month).all()
    todaysdate = datetime.date.today()
    currentyear = datetime.date.today().year
    db.session.close()
    if emp:
        return render_template('test1.html',emp=emp,todaysdate=todaysdate,currentyear=currentyear)
    else:
        return render_template('quotes.html')

@app.route('/page2',methods=['GET'])
def page2():
    emp = Employees.query.filter((extract('day', Employees.dateofbirth) == datetime.datetime.today().day)).filter(
        extract('month', Employees.dateofbirth) == datetime.datetime.today().month).all()

    todaysdate = datetime.date.today()
    currentyear = datetime.date.today().year
    db.session.close()
    if emp:
        return render_template('test2.html',emp=emp,todaysdate=todaysdate,currentyear=currentyear)
    else:
        return render_template('quotes.html')

@app.route('/page3',methods=['GET'])
def page3():
    emp = Employees.query.filter((extract('day', Employees.dateofbirth) == datetime.datetime.today().day))
    emp = emp.filter(extract('month', Employees.dateofbirth) == datetime.datetime.today().month).all()
    todaysdate = datetime.date.today()
    currentyear = datetime.date.today().year
    db.session.close()
    return render_template('test3.html',emp=emp,todaysdate=todaysdate,currentyear=currentyear)


# @app.route('/dynamic/<emmid>/<emmname>/<emmdateofbirth>',methods=['GET'])
# def dynamic(emmid,emmname,emmdateofbirth):
#     return render_template('birthdays.html',emmid=emmid,emmname=emmname,emmdateofbirth=emmdateofbirth)


@app.route('/',methods=['GET'])
def index():
    return render_template('home.html')

@app.route('/addemp',methods=['GET'])
def addemp():
    form = AddForm()
    return render_template('addemployee.html',form=form)


@app.route('/addempnew',methods=['POST'])
def addempnew():
    newemployee = Employees(request.form['empid'],request.form['empname'],request.form['dateofbirth'])
    db.session.add(newemployee)
    db.session.commit()
    return render_template('/')

@app.route('/deleteemp',methods=['GET'])
def deleteemp():
    return render_template('deleteemployee.html')

@app.route('/deleteempnew',methods=['POST'])
def deleteempnew():
    # x = request.form.get('empid')
    # deleteemployee = Employees.query.filter(extract(Employees.empid = 'request.form.get('empid')')).first_or_404().all()
    deleteemployee = db.session.query(Employees).filter(Employees.empid == request.form.get('empid')).first_or_404()
    db.session.delete(deleteemployee)
    db.session.commit()
    return redirect(url_for('index'))


if __name__=='__main__':
    app.run(port =5000)
