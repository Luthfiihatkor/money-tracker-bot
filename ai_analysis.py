from database import c

def analyze(user):

    c.execute("SELECT kategori,SUM(jumlah) FROM transaksi WHERE user=? AND tipe='out' GROUP BY kategori",(user,))
    data=c.fetchall()

    text="🧠 Analisa Keuangan\n\n"

    if not data:
        return "Belum ada data."

    for d in data:
        text+=f"{d[0]} : {d[1]}\n"

    return text
