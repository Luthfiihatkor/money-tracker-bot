import openpyxl
from database import c

def export(user):

    wb=openpyxl.Workbook()
    ws=wb.active

    ws.append(["Tanggal","Tipe","Kategori","Jumlah","Wallet","Note"])

    c.execute("SELECT tanggal,tipe,kategori,jumlah,wallet,note FROM transaksi WHERE user=?",(user,))
    data=c.fetchall()

    for d in data:
        ws.append(d)

    file="report.xlsx"
    wb.save(file)

    return file
