from gtts import gTTS
import speech_recognition as sr
import pygame
import os
import pyautogui
from bs4 import BeautifulSoup
import requests

import random

sadeceespiri = ["Mafya babası olmak için oğlumun adını “Mafya” koydum.","Kim vurduya gittim birazdan gelecem...","Zenginler et, fakirler hayalet yer.","Bugünlerde gözüm çok KIZarıyor.- Benimde arıyor ya!","Hava korsanı uçağı kaçıracaktı ama yapamadı çünkü uçağı kaçırdı.","GİT’Arı’ getir de biraz şarkı söyleyelim. -Abi arı sokmasın!","Sana bir kıllık yapayım, kıllarını koyarsın.","Seven unutmaz oğlum, eight unutur.","Cem Uzan, üstünü örteyim.","Geçenlerde izdivaç programında adam evim, arabam, param var dedi üç hatun aynı anda elektrik aldı. Adam bildiğin üçlü priz çıktı.","Haydi Unkapanı’na gidip birkaç kapan kuralım. Belki un yakalarız","SSaçını sarıya boyatıp kaşlarını zift karası bırakınca doğal sarışın olmuyorsun tatlım. Borussia Dortmund deplasman forması gibi oluyon.","Sonuçta çubuk krakerle sigara içme taklidi yapan çocuklardık biz. Hangi ara bu kadar cool olduk.","Adamın biri güneşte yanmış, ay da düz.","Ben Yedigün içiyorum sen Onbeşgün iç.","Sinemada on dakika ara dedi, aradım aradım açmadı.","Röntgen Filmi çektirdik, yakında sinemalarda.","Adamın Biri Notebook Almış, DELLenmiş.","Geçen gün taksi çevirdim hala dönüyor.","Ben hikâye yazarım Ebru Destan.","Geçen gün geçmiş günlerimi aradım ama meşguldü.","Tebrikler kazandınız, şimdi tencere oldunuz!","Kaba kuvvet uygulama, kap kırılabilir.","Türkiye’nin en yeni şehri – Nevşehir","Ayna'nın karşısında süslenme, manga'nın karşısında süslen.","Geçen ‘fil’e çorap aldım, zürafaya almadım.","Yılanlardan korkma, yılmayanlardan kork.","Ben kahve içiyorum, Nurgül Yeşilçay.","Bak şu karşıdaki uçak PİSTİ, ama bir türlü temizlemediler.","Geçen gün geçmiş günlerimi aradım ama meşguldü","Adamın birisi televizyona çıkmış bir daha indirememişler.","Adamın biri gülmüş, saksıya koymuşlar.","Sinüs 60, kosinüs tutmuş…","Adamın biri kızmış istemeye gelmişler.","Ayda 5 milyon kazanma ister misin? Evet.  O zaman Ay’a git.","Funda Arar dediler ama hala daha aramadı.","Adamın kafası atmış bacakları eşek.","Uzun lafın kısası : U.L.","Yağmur yağmış, kar peynir!","Sakla samanı, inekler aç kalsın.","Baraj dendi mi, akan sular durur.","Dünya dönermiş ay da köfte…","Son gülen en geç anlayandır.","Bu erikson, başka erik yok.","Seven unutmaz oğlum, eight unutur.","Sen kamyonu al, Leonardo da vinci.","Adamın biri gülmüş, bahçeye dikmişler.","Tekel'in nesi var, İki elin sesi var.","Top ağlarda, ben ağlamaz mıyım? ","Esra Erol ile - İs The Watch.","Burger King, bende Vezir.","Adamın biri gülmüş, bahçeye dikmişler.","Ben yürüyelim diyorum Gerard Depardieu.","Beni ayda bir sinemaya götürme, Marsta bir sinemaya götür.","Sevgilisi olmayanlar bul-aşık makinası alsınlar.","Ben ekmek yedim Will Smith.","Aaaaa siz çok terlemişsiniz durun size terlik getiriyim.","Temel bir gün Fransa’ya gitmiş:”Aaa burayı da mı Sabancı aldı.” demiş.","Geçen gün arkadaşlarla fırında patates yiyorduk, fırın sıcak geldi bahçeye çıktı.","İngilizcem yok, tanıdığım bütün Cem'ler Türk.","Sarımsağı havanda dövmüşsün, Ha Muş'ta.","Dondurmayı ben yalamam, himalayalar.","Kalbinin sesini dinle güzelse kaset yap.","Bağırsaklarda yaşayan tenya kurtları bağırsakta yaşarlar bağırmasak da yaşar.","Çiçeğin biri solmuş diğeri de sağ.","Aklımı kaçırdım, 100.000 TL fidye istiyorum.","Altılıda 1. ayakta yattım. Yarış bitmiş uyanamadım.","Ayakkabıcı sıkıyorsa alma dedi, bende korktum aldım","Balık ekmek 3 liraymış, hadi balık ekelim.","Bekarlık sultanlıktır, fakat er ya da geç demokrasiye geçilir"]

def text_to_speech(text, lang='tr'):
    tts = gTTS(text=text, lang=lang)
    tts.save('output.mp3')

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language='tr')
        return text
    except sr.UnknownValueError:
        print("Anlaşılmadı")
    except sr.RequestError:
        print("İnternet bağlantısı yok")

# Sesli asistan döngüsü
while True:
    print("Bir komut söyleyin...")
    command = speech_to_text()
    mert = str(command).lower()
    if command is not None:
        if 'merhaba' in mert:
            text_to_speech("Merhaba, nasılsınız?")
        elif 'iyiyim' in mert:
            text_to_speech("Buna Sevindim Canım")
        elif 'tarayıcıyı kapat' in mert:
            text_to_speech("Tarayıcı Kapatılıyor")
            os.system("taskkill /f /im {}".format("chrome.exe"))
        elif 'android aç' in mert:
            text_to_speech("Android Stüdyo Hemen Açılıyor.")
            os.startfile("D:\\Android\\bin\\studio64.exe")
        elif 'şarkı aç' in mert or 'müzik aç' in mert:
            text_to_speech("Şarkı Açılıyor Hemen Açılıyor.")
            os.startfile("https://www.youtube.com/watch?v=ecSfOsNf8rg&list=RDMMecSfOsNf8rg&index=1&ab_channel=Halilibrahimatalay")
        elif 'hava durumunu söyle' in mert:
            try:
                deger = mert.split(" ")
                url = "https://www.ntv.com.tr/'{}'-hava-durumu".format(deger[0])
                mert = requests.get(url)
                sayfa_icerigi = mert.content
                soup = BeautifulSoup(sayfa_icerigi, "html.parser")
                toplam = []
                for i in soup.find_all("p", {"class": "hava-durumu--detail-data-item-bottom-temp-max"}):
                    toplam.append(i.text)
                mesaj = []
                for e in soup.find_all("div", {"class": "container hava-durumu--detail-data-item-bottom-desc"}):
                    mesaj.append(e.text)
                durum = str(mesaj[0]).strip("\r\n\r\n ")
                text_to_speech("Söylüyorum "+deger[0]+toplam[0]+durum)
            except:
                text_to_speech("İstediginiz Yer Bulunamadı Lütfen Tekrar Dene")
        elif 'kötüyüm' in mert:
            sayi = random.randint(0,len(sadeceespiri))
            text_to_speech("Daha İyi Olman İçin Hemen Sana Espiri Yapıyorum."+sadeceespiri[sayi])
        elif 'görüşürüz' in mert:
            text_to_speech("Görüşmek üzere!")
        elif 'müzik atla' in mert:
            text_to_speech("Müzik Değişiyor.")
            pyautogui.press('prevtrack')
        elif 'müzik durdur' in mert:
            text_to_speech("Müzik Duruyor.")
            pyautogui.press('playpause')
        elif 'ses aç' in mert:
            text_to_speech("Ses Açılıyor!")
            s =0
            while(s < 5):
                print("girdi")
                pyautogui.press('volumeup')
                s+=1
        elif 'doların fiyatını söyle' in mert:
            dolar = []
            euro = []
            btc = []
            url = "https://bigpara.hurriyet.com.tr/doviz/dolar/"
            mert = requests.get(url)
            sayfa_icerigi = mert.content
            soup = BeautifulSoup(sayfa_icerigi, "html.parser")
            for e in soup.find_all("span", {"class": "value up"}):
                dolar.append(e.text)
            url1 = "https://bigpara.hurriyet.com.tr/doviz/euro/"
            mert1 = requests.get(url1)
            sayfa_icerigi1 = mert1.content
            soup = BeautifulSoup(sayfa_icerigi1, "html.parser")
            for a in soup.find_all("span", {"class": "value up"}):
                euro.append(a.text)
            url2 = "https://coinmarketcap.com/tr/currencies/bitcoin/"
            mert2 = requests.get(url2)
            sayfa_icerigi2 = mert2.content
            soup = BeautifulSoup(sayfa_icerigi2, "html.parser")
            for w in soup.find_all("div", {"priceValue smallerPrice"}):
                btc.append(w.text)
            euro1 = str(euro[0])
            btc1 = str(btc).strip("[]',₺")
            dolar1 = str(dolar[0])
            text_to_speech("Şimdi Söylüyorum"+dolar1+"TÜRK LİRASI")
        elif 'ses düşür' in mert:
            text_to_speech("Ses kısılıyor!")
            s = 0
            while (s < 5):
                print("girdi")
                pyautogui.press('volumedown')
                s += 1
        else:
            text_to_speech("Anlamadım")

        # Ses dosyasını çal
        pygame.mixer.init()
        pygame.mixer.music.load('output.mp3')
        pygame.mixer.music.play()

        # Çalma tamamlanana kadar bekleyin
        while pygame.mixer.music.get_busy():
            continue

        # Ses çalmayı durdur ve ses sistemini kapat
        pygame.mixer.music.stop()
        pygame.mixer.quit()

        # Ses dosyasını sil
        os.remove('output.mp3')
        if 'görüşürüz' in mert:
            break