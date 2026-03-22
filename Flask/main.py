from flask import Flask, render_template,request # Import Flask class
app=Flask(__name__) # Creating objct of flask class


@app.route("/displayName")
def displayName():
    name="Abhishek"
    return render_template("DisplayName.html",uname=name)

@app.route("/displayNames")
def displayNames():
    firstname="Abhishek"
    lastname="Walikar"
    return render_template("DisplayNames.html",
                           firstname=firstname,lastname=lastname)

@app.route("/displayList")
def displayList():
    data=['Abhishek','Ved','Manoj','Atharv']
    return render_template("DisplayList.html",data=data)


@app.route("/displayNestedList")
def displayNestedList():
    data=[[101,'Abhishek',98],[102,'Ved',94],[103,'Manoj',98],[104,'Atharv',89]]
    return render_template("DisplayNestedList.html",data=data)



@app.route("/DisplayDict")
def displayDict():
    data={101:['Abhishek',98],102:['Ved',94],103:['Manoj',98],104:['Atharv',89]}
    return render_template("Displaydict.html",data=data)

@app.route('/login',methods=["GET","POST"])  # Links URL with function
def login():
    if request.method=="GET":
        return render_template('login.html')
    else:
        uname=request.form["uname"]
        pwd=request.form["pwd"]

        if uname=='Firstbit' and pwd=='flask123':
            return 'Login successful'
        else:
            return 'Login failed'

@app.route("/sum",methods=['GET','POST'])
def getSum():
    if request.method=='GET':
        return render_template('AddNumber.html')
    else:
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        result=num1+num2
        # return "Sum:"+str(result)
        return render_template('Addnumber.html',result="Sum:"+str(result))

    

@app.route('/signup')
def register():
    return 'I am register method'

if __name__=='__main__':
    app.run(debug=True) # Starts the server