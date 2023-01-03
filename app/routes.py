from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    kullanici = {"kullaniciAdi":"Uzaktanegitim"}
    bilgiler = [{"adi":{"tur":"Kazak","marka":"KAFT"},"adet":12,"fiyat":25.50},
                {"adi":{"tur":"Kot","marka":"COLINS"},"adet":13,"fiyat":32.50}]
    return render_template("index.html",baslik="Ana Sayfa",user=kullanici,malzemeler=bilgiler)