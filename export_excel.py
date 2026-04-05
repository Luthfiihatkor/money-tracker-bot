import pandas as pd
from database import get_transactions


def export_excel(user_id):

    data = get_transactions(user_id)

    df = pd.DataFrame(data, columns=["type","amount","category","note","date"])

    file = "report.xlsx"

    df.to_excel(file, index=False)

    return file
