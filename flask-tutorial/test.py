from flask import Flask, render_template, request
app  =  Flask (__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        entered_name = request.form.get("name")
        entered_age = request.form.get('age')
        if entered_age == '50':
            return render_template('user.html', name=entered_name)
        return render_template('fail.html')
    return render_template('index.html')
