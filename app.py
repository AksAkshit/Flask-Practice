## Create a simple flask application

from flask import Flask,render_template,request,redirect,url_for

# render_template - Function to render an HTML webpage
# url_for - Function to create a route for particular decorator route in the backend
# request - library to use various methods related to requests
# redirect - Function to redirect to an already created route from the backend using url_for()





## Create the flask app

app=Flask(__name__)                           # Entry of the program

@app.route('/')                               # When we hit this route home() is called
def home():
    return "<h2>Hello, World!</h2>"

@app.route('/welcome')
def welcome():
    return "Welcome to the Flask Tutorials"

@app.route('/index')
def index():
    return render_template('index.html')                    # All the HTML templates should be present in the 
                                                            # 'templates' (naming convention) folder 
                                                            # If template not available => TemplateNotFound Exception

@app.route('/success/<int:score>')                               # This way we can directly pass the score as a parameter 
def success(score):                                              # through the URL
    return "the person is passed and the score is "+str(score)   

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the score is "+str(score)  # By default everything returned by the function should be a string


@app.route('/calculate',methods=['POST','GET'])     
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3
        result="" 
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        # return redirect(url_for(result,score=average_marks))


        return render_template('result.html',results=average_marks)     # results - argument which can be referred 
                                                                        # in the HTML page 


## Assignemnt Try for loop



if __name__=='__main__':
    app.run(debug=True)         # debug=True : To reload the app automatically when we make changes to app.py


