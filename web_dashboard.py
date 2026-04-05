from flask import Flask, render_template_string
from services.finance_service import get_transactions

app = Flask(__name__)


@app.route("/")
def dashboard():

    data = get_transactions()

    income = 0
    expense = 0

    for d in data:

        if d[1] == "income":
            income += d[2]

        if d[1] == "expense":
            expense += d[2]

    balance = income - expense

    html = """
    <h1>Personal Finance Dashboard</h1>

    <h2>Summary</h2>

    <p>Income : {{income}}</p>
    <p>Expense : {{expense}}</p>
    <p>Balance : {{balance}}</p>

    <h2>Transactions</h2>

    <table border=1>

    <tr>
        <th>ID</th>
        <th>Type</th>
        <th>Amount</th>
        <th>Category</th>
        <th>Note</th>
        <th>Date</th>
    </tr>

    {% for row in data %}
    <tr>
        <td>{{row[0]}}</td>
        <td>{{row[1]}}</td>
        <td>{{row[2]}}</td>
        <td>{{row[3]}}</td>
        <td>{{row[4]}}</td>
        <td>{{row[5]}}</td>
    </tr>
    {% endfor %}

    </table>
    """

    return render_template_string(
        html,
        data=data,
        income=income,
        expense=expense,
        balance=balance
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=8080
    )
