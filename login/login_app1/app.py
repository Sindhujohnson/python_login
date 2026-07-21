import pandas as pd
data={
    "username":[],
    "password":[]
}
df=pd.DataFrame(data)
df.to_excel("users.xlsx",index=False)
print("users.xlsx created successfully!")
from flask import Flask, render_template,request,redirect,url_for
import pandas as pd
import os
app=Flask(__name__)
FILE="users.xlsx"
@app.route("/",methods=["GET","POST"])
def login():
    message=""
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        df=pd.read_excel(FILE)
        #checkig if the user exists in the database
        user=df[(df["username"]==username) & (df["password"]==password)]
        if not user.empty:
            message="Login Successfull"
        else:
            #Save new user to the database
            new_user=pd.DataFrame([[username,password]],columns=["username","password"])
            df=pd.concat([df,new_user],ignore_index=True)
            df.to_excel(FILE,index=False)
            message="User logged in successfully"
    return render_template("login.html",message=message)
if __name__=="__main__":
    app.run(debug=True)