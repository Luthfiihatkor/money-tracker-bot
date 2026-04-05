from flask import Flask,render_template_string
from database import get_transactions

app=Flask(__name__)


@app.route("/")
def home():

    data=get_transactions()

    html="""
    <h1>Finance Dashboard</h1>

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

    return render_template_string(html,data=data)


if __name__=="__main__":
    app.run()
