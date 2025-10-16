from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi = None
    category = None
    if request.method == 'POST':
        height = float(request.form['height']) / 100  # convert cm to meters
        weight = float(request.form['weight'])
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

    return render_template('index.html', bmi=bmi, category=category)

if __name__ == '__main__':
    app.run(debug=True)

