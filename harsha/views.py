from flask import Flask,render_template,redirect,request
import pymysql as py
app=Flask(__name__)
@app.route('/')
def display():
    try:
        db=py.Connect(host='localhost',user='root',password='',database='library')
        cur=db.cursor()
        sqq= 'select * from records'
        cur.execute(sqq)
        data=cur.fetchall()
    except Exception as e:
        print('Error:',e)    
    return render_template('splashboard.html',data=data)

@app.route('/create')
def create():
    return render_template('form.html')

@app.route('/Reach')
def Reach():
    return render_template('ReachUS.html')


@app.route('/replace/<rid>')
def replace(rid):
    try:
        db=py.Connect(host='localhost',user='root',password='',database='library')
        cur=db.cursor()
        sq3="select * from records where id='{}'".format(rid)
        cur.execute(sq3)
        data=cur.fetchall()
        return render_template('replaceform.html',data=data)
    except Exception as e:
        print('Error',e)
    
        
@app.route('/store',methods=['POST'])
def store():
    p=request.form['Pustak']
    cat=request.form['Category']
    au=request.form['Author']
    pr=request.form['Price']

    try:
        db=py.Connect(host='localhost',user='root',password='',database='library')
        cur=db.cursor()
        qu='insert into records(Pustak,Category,Author,Price) values("{}","{}","{}","{}")'.format(p,cat,au,pr)
        cur.execute(qu)
        db.commit()
    except Exception as e:
        print('FAILED to INSERT',e)
    return redirect('/')

@app.route('/update/<rid>',methods=['POST'])
def update(rid):
    p=request.form['Pustak']
    cat=request.form['Category']
    au=request.form['Author']
    pr=request.form['Price']
    try:
        db=py.Connect(host='localhost',user='root',password='',database='library')
        cur=db.cursor()
        sq2="update records set Pustak='{}',Category='{}',Author='{}',Price='{}' where id='{}'".format(p,cat,au,pr,rid)
        cur.execute(sq2)
        db.commit()
    except Exception as e:
        print('Failed to update',e)
    return redirect('/')

    
@app.route('/delete/<rid>')
def delete(rid):
    try:
        db=py.Connect(host='localhost',user='root',password='',database='library')
        cur=db.cursor()
        sq1="delete from records where id='{}'".format(rid)
        cur.execute(sq1)
        data=cur.fetchall()
        db.commit()
        return redirect('/')
    except Exception as e:
        print('Error',e)
    
app.run(debug=True)
