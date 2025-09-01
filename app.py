from flask import Flask, request, render_template_string

app = Flask(__name__)

form_html = """
<!doctype html>
<html>
<head><title>Age Calculator</title></head>
<body style="font-family: Arial; margin: 50px;">
    <h2>Age Calculator</h2>
    <form method="POST" action="/">
        Birth Year: <input type="number" name="birth_year" required><br><br>
        Current Year: <input type="number" name="current_year" required><br><br>
        <input type="submit" value="Calculate Age">
    </form>
    {% if age is not none %}
        <h3>You are {{ age }} years old.</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculate_age():
    age = None
    if request.method == "POST":
        birth_year = int(request.form["birth_year"])
        current_year = int(request.form["current_year"])
        age = current_year - birth_year
    return render_template_string(form_html, age=age)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
