from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['Post'])
def process():
    if len(request.form['textarea']) > 120:
        flash("Comments cannot be more than 120 characters!")
        return redirect('/')
    else:
        pass
    if len(request.form['textarea']) < 1:
        flash("Comments cannot be empty!")
        return redirect('/')
    else:
        pass
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    else:
        pass
    comment = request.form['textarea']
    return render_template('results.html', comment = comment)

@app.route('/back', methods=['Post'])
def back():

    return render_template('index.html')

app.run(debug=True)
