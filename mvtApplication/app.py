from flask import Flask, render_template, request, flash
from joblib import load

app = Flask(__name__)

model = load('model.joblib')

@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'POST':
        passenger_class = request.form['passs']
        age = request.form['age']
        gender = request.form['gender']
        if gender == "1":
            female = 0
            male = 1
        else:
            female = 1
            male = 0
        y_pred = [[passenger_class, age, female, male]]      
        preds = model.predict(y_pred)
        if preds == 0:
            flash("No Survived", 'danger')
        else:
            flash("Survived", 'success')
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key = 'Your secret key'
    app.run(debug=True)