from telegram import Update
from telegram.ext import ApplicationBuilder,CommandHandler,ContextTypes

from scheduler import start_scheduler
from config import TOKEN,OWNER_ID
from models import init_db

from services.finance_service import add_transaction,get_transactions
from services.category_service import detect_category
from services.chart_service import category_chart
from services.export_service import export_excel
from services.ai_service import analyze
from services.prediction_service import predict_expense


def is_owner(user):

    return user == OWNER_ID


async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):

    if not is_owner(update.effective_user.id):
        return

    await update.message.reply_text(
"""
PERSONAL FINANCE AI

/in jumlah note
/out jumlah note

/summary
/chart
/export
/ai
/predict
"""
)


async def income(update,context):

    if not is_owner(update.effective_user.id):
        return

    amount=int(context.args[0])

    note=" ".join(context.args[1:])

    cat=detect_category(note)

    add_transaction("income",amount,cat,note)

    await update.message.reply_text("income saved")


async def expense(update,context):

    if not is_owner(update.effective_user.id):
        return

    amount=int(context.args[0])

    note=" ".join(context.args[1:])

    cat=detect_category(note)

    add_transaction("expense",amount,cat,note)

    await update.message.reply_text("expense saved")


async def summary(update,context):

    data=get_transactions()

    inc=0
    exp=0

    for d in data:

        if d[1]=="income":
            inc+=d[2]

        if d[1]=="expense":
            exp+=d[2]

    await update.message.reply_text(
f"""
SUMMARY

Income : {inc}

Expense : {exp}

Balance : {inc-exp}
"""
)


async def chart(update,context):

    file=category_chart()

    await update.message.reply_photo(open(file,"rb"))


async def export(update,context):

    file=export_excel()

    await update.message.reply_document(open(file,"rb"))


async def ai(update,context):

    text=analyze()

    await update.message.reply_text(text)


async def predict(update,context):

    p=predict_expense()

    await update.message.reply_text(
        f"Predicted expense next day : {p}"
    )


def main():

    init_db()

    app=ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start",start))
    app.add_handler(CommandHandler("in",income))
    app.add_handler(CommandHandler("out",expense))
    app.add_handler(CommandHandler("summary",summary))
    app.add_handler(CommandHandler("chart",chart))
    app.add_handler(CommandHandler("export",export))
    app.add_handler(CommandHandler("ai",ai))
    app.add_handler(CommandHandler("predict",predict))

def main():

    init_db()

    start_scheduler()

    app = ApplicationBuilder().token(TOKEN).build()
    
    app.run_polling()


if __name__=="__main__":
    main()
