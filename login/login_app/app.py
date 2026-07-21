from flask import Flask, render_template, request,redirect, url_for
app = Flask(__name__)
USERNAME= input("Enter username:")
PASSWORD= input("Enter password:")
@app.route("/", methods=['GET','POST'])
def login():
    if request.method =='POST':
        username=request.form['username']
        password=request.form['password']
        if username==USERNAME and password==PASSWORD:
            return"Login Successfull"
        else:
            return"Invalid credentials"
    return render_template('login.html')
if __name__=='__main__':
 app.run(debug=True)