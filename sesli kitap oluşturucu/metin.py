import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog



def pdf_metin_cikart(pdf_yolu):
      metin=""
      pdf_okuyucu=PyPDF2.PdfReader(open(pdf_yolu,"rb"))
      for sayfa_num in range(len(pdf_okuyucu.pages)):
            metin+= pdf_okuyucu.pages[sayfa_num].extract_text()
      return metin
#metni seli hale çeviren fonksiyon
 
def metni_sese_cevir(metin,cikti_dosyasi):
      sesli_cevirici=gTTS(text=metin, lang='tr')
      sesli_cevirici.save(cikti_dosyasi)


#dosya seçme metodu
def dosya_sec():
      dosya_yolu=filedialog.askopenfilename(filetypes=[("PDF Dosyaları ","*pdf")])
      if dosya_yolu:
            pdf_metin =pdf_metin_cikart(dosya_yolu)
            metni_sese_cevir(pdf_metin,"kaydet.mp3")
            os.system("start kaydet.mp3")



#tkinter  arayüzü
app=tk.Tk()
app.title("Sesli kitap Uygulması")
app.geometry("200x150")
secim_butonu =tk.Button(app,text="PDF Seç", command=dosya_sec,padx=20,pady=20, fg="black",bg="red")
secim_butonu.pack(pady=20)


app.mainloop()
