liste = ["AliEmre","AliKurt","Ayse","Bahar","Burak","Edanur","Emin","Hakan","Hedayah","Kaan",
"Melike","Metehan","Andac","Esra","Omer","Sonay","Tarik","Turan","Cagan","OmerA","Irfancan","Ediz"]
import os
# os.mkdir("Egzersiz")
for item in liste:
    try:
        os.mkdir(f"Egzersiz/{item}")
        open(f"Egzersiz/{item}/ilk.py","a+")
    except:
        pass