liste = ["AliEmre","AliKurt","Ayse","Baha","Burak","Edanur","Emin","Hakan","Hedayah","Kaan",
"Melike","Metehan","Andac","Esra","Omer","Sonay","Tarik","Turan","Cagan","OmerA","Irfancan","Ediz","Samet"]
import os
dosya_ismi = "02_Donguler.py"
# os.mkdir("Egzersiz")
for item in liste:
    try:
        open(f"Egzersiz/{item}/{dosya_ismi}","a+")
    except:
        pass