from apscheduler.schedulers.background import BackgroundScheduler
from services.ai_service import analyze
from services.finance_service import get_transactions

from telegram import Bot
from config import TOKEN, OWNER_ID

bot = Bot(token=TOKEN)


async def daily_report():

    data = get_transactions()

    income = 0
    expense = 0

    for d in data:

        if d[1] == "income":
            income += d[2]

        if d[1] == "expense":
            expense += d[2]

    text = f"""
DAILY FINANCE REPORT

Income : {income}

Expense : {expense}

Balance : {income-expense}
"""

    await bot.send_message(chat_id=OWNER_ID, text=text)


async def ai_report():

    text = analyze()

    await bot.send_message(
        chat_id=OWNER_ID,
        text=text
    )


def start_scheduler():

    scheduler = BackgroundScheduler()

    # laporan harian jam 21:00
    scheduler.add_job(
        daily_report,
        "cron",
        hour=21,
        minute=0
    )

    # AI report mingguan
    scheduler.add_job(
        ai_report,
        "cron",
        day_of_week="sun",
        hour=20
    )

    scheduler.start()
