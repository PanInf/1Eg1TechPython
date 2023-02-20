kod = "3M5A2R7E4K"
tekst = ""
for i in range(0,len(kod),2):
    tekst += int(kod[i]) * kod[i+1]
print(tekst)