from flask import Flask,request,render_template

app = Flask(__name__)

    
@app.route('/',methods=['GET',"POST"])
def test():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def mycalci():
    if (request.method=='POST'):
        ops = request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        if ops=='add':
            r=num1+num2
            result = 'this is sum of ' + str(num1) + 'and' + str(num2) + 'is' + str(r)

        if ops=='subtract':
            r=num1-num2
            result = 'this is sub of ' + str(num1) + 'and' + str(num2) + 'is' + str(r)

        if ops=='multiply':
            r=num1*num2
            result = 'this is multiplication of ' + str(num1) + 'and' + str(num2) + 'is' + str(r)

        if ops=='divide':
            r=num1/num2
            result = 'this is division of ' + str(num1) + 'and' + str(num2) + 'is' + str(r)

        if ops=='log':
            r=num1lognum2
            result = 'this is log of ' + str(num1) + 'and' + str(num2) + 'is' + str(r)            
    return render_template('results.html',result=result)
 


if __name__=='__main__':
    app.run(host='0.0.0.0')