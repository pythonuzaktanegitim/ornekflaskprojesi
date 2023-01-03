liste = ["AliEmre","AliKurt","Ayse","Baha","Burak","Edanur","Emin","Hakan","Hedayah","Kaan",
"Melike","Metehan","Andac","Esra","Omer","Sonay","Tarik","Turan","Cagan","OmerA","Irfancan","Ediz"]
for item in liste:
    dosya = open(f"Egzersiz/{item}/ilk.py","a+")
    if  'print' not in dosya.read():
        print(item)