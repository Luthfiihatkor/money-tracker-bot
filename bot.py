import telebot
import re
from datetime import datetime

from config import TOKEN
from database import conn,c
from ai_analysis import analyze
from export_excel import export

bot=telebot.TeleBot(TOKEN)


def saldo(user):

    c.execute("SELECT SUM(jumlah) FROM transaksi WHERE user=? AND tipe='in'",(user,))
    masuk=c.fetchone()[0] or 0

    c.execute("SELECT SUM(jumlah) FROM transaksi WHERE user=? AND tipe='out'",(user,))
    keluar=c.fetchone()[0] or 0

    return masuk-keluar



@bot.message_handler(commands=['start'])
def start(m):

    bot.reply_to(m,"""
👑 PERSONAL MONEY AI

contoh:

beli kopi 15000
makan 20000
jual belut 500000

commands

/saldo
/history
/analysis
/export
""")


@bot.message_handler(commands=['saldo'])
def s(m):

    bot.reply_to(m,f"💰 Saldo : {saldo(m.from_user.id)}")



@bot.message_handler(commands=['analysis'])
def a(m):

    bot.reply_to(m,analyze(m.from_user.id))



@bot.message_handler(commands=['export'])
def ex(m):

    file=export(m.from_user.id)

    bot.send_document(m.chat.id,open(file,"rb"))



@bot.message_handler(func=lambda m:True)
def catat(m):

    text=m.text.lower()

    angka=re.findall(r'\d+',text)

    if not angka:
        return

    jumlah=int(angka[0])

    if "jual" in text:
        tipe="in"
    else:
        tipe="out"

    c.execute("""
    INSERT INTO transaksi VALUES(NULL,?,?,?,?,?,?,?)
    """,(m.from_user.id,tipe,jumlah,"general","cash",text,str(datetime.now().date())))

    conn.commit()

    bot.reply_to(m,"✅ transaksi dicatat")


print("BOT AKTIF")

bot.infinity_polling()
