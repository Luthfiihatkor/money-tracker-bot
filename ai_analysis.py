from database import get_transactions

def analyze_finance(user_id):

    data = get_transactions(user_id)

    total_income = 0
    total_expense = 0

    categories = {}

    for d in data:

        tipe = d[0]
        amount = d[1]
        category = d[2]

        if tipe == "income":
            total_income += amount
        else:
            total_expense += amount

        if category not in categories:
            categories[category] = 0

        categories[category] += amount

    balance = total_income - total_expense

    biggest = max(categories, key=categories.get)

    report = f"""
📊 ANALISIS KEUANGAN

💰 Total Income : {total_income}
💸 Total Expense : {total_expense}
🏦 Balance : {balance}

🔥 Pengeluaran terbesar:
{biggest}

"""

    if total_expense > total_income:
        report += "\n⚠️ Kamu lebih banyak mengeluarkan uang daripada pemasukan."

    if categories.get("food",0) > total_expense*0.4:
        report += "\n🍔 Pengeluaran makan cukup tinggi."

    return report
