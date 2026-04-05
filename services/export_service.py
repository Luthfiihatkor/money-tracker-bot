import pandas as pd
from services.finance_service import get_transactions


def export_excel():

    data = get_transactions()

    df = pd.DataFrame(
        data,
        columns=["id","type","amount","category","note","date"]
    )

    file = "finance_report.xlsx"

    df.to_excel(file, index=False)

    return file
