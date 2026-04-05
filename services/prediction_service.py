import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from services.finance_service import get_transactions


def predict_expense():

    data = get_transactions()

    df = pd.DataFrame(data,
        columns=["id","type","amount","category","note","date"])

    exp = df[df["type"]=="expense"]

    exp["date"]=pd.to_datetime(exp["date"])

    exp = exp.groupby("date")["amount"].sum().reset_index()

    exp["day"] = range(len(exp))

    X = exp[["day"]]

    y = exp["amount"]

    model = LinearRegression()

    model.fit(X,y)

    pred = model.predict(np.array([[len(exp)+1]]))[0]

    return int(pred)
