import telebot
import re
import os
from datetime import datetime
from database import conn,c

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)


def saldo(user):

    c.execute("SELECT SUM(jumlah) FROM transaksi WHERE user=? AND tipe='in'",(user,))
    masuk=c.fetchone()[0] or 0

    c.execute("SELECT SUM(jumlah) FROM transaksi WHERE user=? AND tipe='out'",(user,))
    keluar=c.fetchone()[0] or 0

    return masuk-keluar



@bot.message_handler(commands=['start'])
def start(m):

    bot.reply_to(m,"""
👑 PERSONAL FINANCE OS

Contoh:

beli kopi 15000
makan 20000
jual belut 500000

Commands:

/saldo
/stat
/history
/analysis
""")


@bot.message_handler(commands=['saldo'])
def saldo_cmd(m):

    bot.reply_to(m,f"💰 Saldo : {saldo(m.from_user.id)}")



@bot.message_handler(func=lambda m: True)
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


bot.infinity_polling()
