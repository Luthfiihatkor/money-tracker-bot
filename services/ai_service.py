from services.finance_service import get_transactions
from services.prediction_service import predict_expense


def analyze():

    data = get_transactions()

    income = 0
    expense = 0

    for d in data:

        if d[1]=="income":
            income += d[2]

        if d[1]=="expense":
            expense += d[2]

    balance = income-expense

    pred = predict_expense()

    report=f"""
AI FINANCIAL ANALYSIS

Income : {income}

Expense : {expense}

Balance : {balance}

Predicted next expense : {pred}
"""

    if expense > income:
        report += "\n⚠️ Spending lebih besar dari income"

    elif expense > income*0.8:
        report += "\n⚠️ Pengeluaran sudah sangat tinggi"

    else:
        report += "\n✅ Keuangan masih sehat"

    return report
