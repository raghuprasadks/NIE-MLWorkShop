from flask import Flask  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    return "hello, this is our first flask website"; 

@app.route('/greet') #decorator drfines the   
def greet():  
    return "Hearty congratulations"; 

@app.route('/home')  
def homepage():  
    return "hello, welcome to our website";

@app.route('/home/<name>')  
def homenew(name):  
    return "hello,"+name;  
 
  
if __name__ =='__main__':  
    app.run(debug = True) 