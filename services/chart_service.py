import pandas as pd
import matplotlib.pyplot as plt
from services.finance_service import get_transactions


def category_chart():

    data = get_transactions()

    df = pd.DataFrame(data,
        columns=["id","type","amount","category","note","date"])

    expense = df[df["type"]=="expense"]

    chart = expense.groupby("category")["amount"].sum()

    chart.plot(kind="pie", autopct="%1.1f%%")

    plt.title("Expense Distribution")

    file = "category_chart.png"

    plt.savefig(file)

    plt.close()

    return file
