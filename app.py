from flask import Flask, render_template_string, request

app = Flask(__name__)

# Simple HTML page
html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>UPI Fraud Detection</title>
</head>
<body style="font-family: Arial; text-align: center; margin-top: 50px;">

    <h2>UPI Transaction Check</h2>

    <form method="POST">
        <input type="text" name="amount" placeholder="Enter Amount" required><br><br>
        <input type="text" name="upi_id" placeholder="Enter UPI ID" required><br><br>
        <button type="submit">Check Transaction</button>
    </form>

    {% if result %}
        <h3>Result: {{ result }}</h3>
    {% endif %}

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        amount = float(request.form['amount'])

        # Simple fraud logic (you can replace with ML model)
        if amount > 10000:
            result = "⚠️ Fraud Detected!"
        else:
            result = "✅ Safe Transaction"

    return render_template_string(html_page, result=result)

if __name__ == '__main__':
    app.run()