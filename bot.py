from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from database import add_transaction, get_transactions, get_balance
from ai_analysis import analyze_finance
from export_excel import export_excel
from config import BOT_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
💰 MONEY GOD SYSTEM

/add jumlah catatan
/income jumlah catatan
/history
/balance
/report
"""

    await update.message.reply_text(text)


async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user.id

    amount = int(context.args[0])
    note = " ".join(context.args[1:])

    category = auto_category(note)

    add_transaction(user,"expense",amount,category,note)

    await update.message.reply_text(
        f"✅ Pengeluaran tercatat\nKategori: {category}"
    )


async def income(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user.id

    amount = int(context.args[0])
    note = " ".join(context.args[1:])

    category = auto_category(note)

    add_transaction(user,"income",amount,category,note)

    await update.message.reply_text("💰 Pemasukan tercatat")


async def history(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user.id

    data = get_transactions(user)

    text = "📊 Riwayat\n\n"

    for d in data:
        text += f"{d[4]} | {d[0]} | {d[1]} | {d[3]}\n"

    await update.message.reply_text(text)


async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user.id

    bal = get_balance(user)

    await update.message.reply_text(f"💰 Saldo kamu: {bal}")


async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user.id

    file = export_excel(user)

    await update.message.reply_document(open(file,"rb"))


async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user.id

    report = analyze_finance(user)

    await update.message.reply_text(report)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start",start))
app.add_handler(CommandHandler("add",add))
app.add_handler(CommandHandler("income",income))
app.add_handler(CommandHandler("history",history))
app.add_handler(CommandHandler("balance",balance))
app.add_handler(CommandHandler("report",report))
app.add_handler(CommandHandler("analyze", analyze))

app.run_polling()
