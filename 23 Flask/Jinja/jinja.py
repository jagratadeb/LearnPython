# Building URL Dynamically
# Variable Rule
# Jinja 2 Template Engine

from flask import Flask, render_template, request,redirect

# WSGI Application
app = Flask(__name__)

@app.route("/")
def start():
    return "<html><h1>This is an H1 Tag</h1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

# @app.route('/submit',methods=['GET','POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form['name']
#         return f"Hello {name}!"
#     return render_template("form.html")

# Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',results=res)


@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score >= 50:
        res="PASS"
    else:
        res="FAIL"

    exp = {'Score':score,'Result':res}
    return render_template('result1.html', results=exp)


@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html',results=score)


@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method == "POST":
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        history = float(request.form['history'])

        total_score = (science + maths + history)/3
    return redirect(url_for('successres', score = total_score))

if __name__ == "__main__":
    app.run(debug=True)




# Jinja 2 Template Engine
'''
{{ }} expressions to print output in html
{%...%} conditions, for loops
{#...#} comments
'''