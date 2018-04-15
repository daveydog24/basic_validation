from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    if 'name' not in session:
        session['name']=''
    return render_template('index.html')

@app.route('/process', methods=['Post'])
def process():
    if len(request.form['name']) < 1:
       flash("Validation error")
    else:
        name = request.form['name']
        flash("Success! Your name is " + name)
    return redirect('/')
app.run(debug=True)
