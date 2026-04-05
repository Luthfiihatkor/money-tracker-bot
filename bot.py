
import telebot
import os

TOKEN = os.getenv("8654904952:AAHUiaqZAwCNeZvALoR3igccGjyaMR8u67A")
bot = telebot.TeleBot(TOKEN)

balance = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,
    "💰 Money Tracker Bot\n\n"
    "Perintah:\n"
    "/add 10000 = tambah pemasukan\n"
    "/out 5000 = catat pengeluaran\n"
    "/saldo = cek saldo")

@bot.message_handler(commands=['add'])
def add_money(message):
    global balance
    amount = int(message.text.split()[1])
    balance += amount
    bot.reply_to(message, f"✅ Pemasukan ditambah\nSaldo: {balance}")

@bot.message_handler(commands=['out'])
def out_money(message):
    global balance
    amount = int(message.text.split()[1])
    balance -= amount
    bot.reply_to(message, f"💸 Pengeluaran dicatat\nSaldo: {balance}")

@bot.message_handler(commands=['saldo'])
def check_balance(message):
    bot.reply_to(message, f"💰 Saldo kamu: {balance}")

bot.infinity_polling()
