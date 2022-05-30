from textblob import TextBlob
#
# self.opentrencevrilenmetinText.delete("1.0","end")
#             text = TextBlob(metin)
#             cevir = text.translate(from_lang="tr", to="en")
#             self.opentrencevrilenmetinText.insert(END, f"{cevir}")
#
from tkinter import *
import tkinter as tk

class Uygulama():
    def __init__(self):
        self.pencere = Tk()
        self.pencere.title("Translation - Tercüman")
        self.pencere.config(bg="#787372")
        self.pencere.geometry("1200x600+0+0")

        # ToolBarFrame
        self.toolbarFrame = Frame(self.pencere, bg="#FF5F1F", width=1200, height=50)

        self.openmenunav = Label(self.toolbarFrame, text="❱", bg="#FF5F1F", fg="#fff",
                                 font=("MonoSpace", 30, "bold"))
        self.openmenunav.bind("<Button-1>", lambda x: self.navmenubaropen())
        self.openmenunav.place(x=0, y=0)

        self.closemenunav = Label(self.toolbarFrame, text="❰", bg="#FF5F1F", fg="#fff",
                                  font=("MonoSpace", 30, "bold"))
        self.closemenunav.bind("<Button-1>", lambda x: self.navmenubarclose())
        # self.closemenunav.place(x=0, y=0)

        self.sendekazanLabel = Label(self.toolbarFrame, text="Translation - Tercüme", bg="#FF5F1F", fg="#fff",
                                     font=("MonoSpace", 30, "bold"))
        self.sendekazanLabel.place(x=375, y=0)

        self.banner = Label(self.toolbarFrame, text="TT", bg="#FF5F1F", fg="#fff", font=("MonoSpace", 30, "bold"))
        self.banner.place(x=1140, y=0)

        self.toolbarFrame.place(x=0, y=0)

        # NavMenuBarFrame
        self.navmenubarFrame = Frame(self.pencere, bg="#FF5F1F", width=225, height=600)

        self.menuFrame = Frame(self.navmenubarFrame, bg="#FF5F1F", width=225, height=190)
        self.menu = Label(self.menuFrame, text="MENU", bg="#FF5F1F", fg="#fff", font=("MonoSpace", 20, "bold"))
        self.menu.place(x=50, y=7)

        # OpenTrEn Button
        self.opentrenbutton = Label(self.menuFrame, text="Translation", bg="#FF5F1F", fg="#fff",
                                    font=("MonoSpace", 15, "bold"))
        self.opentrenbutton.bind("<Button-1>", lambda x: self.opentrans())
        self.opentrenbutton.place(x=10, y=60)

        # OpenHakkımda Button
        self.openhakkimdabutton = Label(self.menuFrame, text="Hakkımda", bg="#FF5F1F", fg="#fff",
                                     font=("MonoSpace", 15, "bold"))
        self.openhakkimdabutton.bind("<Button-1>", lambda x: self.openhakkimda())
        self.openhakkimdabutton.place(x=10, y=90)
        self.menuFrame.place(x=0, y=0)
        # navmenubarFrame.place(x=0,y=0)

        # OpenTrEn
        self.opentrenFrameAcikmi = True
        self.opentrenFrame = Frame(self.pencere, bg="#FFFFFF", width=1167, height=510)

        self.cevrilenbelge = Label(self.opentrenFrame, text="Çevrilen Dili Seçin: ", bg="#FFFFFF", fg="#787372",
                                   font=("MonoSpace", 11, "bold"))

        options1 = ["Türkçe", "İngilizçe", "Rusça", "Almanca", "Azerbaycan", "ABD", "Brezilya", "Bulgaristan", "Çin",
                    "Japonya", "İsveç", "İsviçre"]
        self.clicked1 = StringVar()
        self.clicked1.set(options1[0])
        self.cevrilenbelgesec = OptionMenu(self.opentrenFrame, self.clicked1, *options1)
        print(dir(self.cevrilenbelgesec))
        self.cevrilenbelgesec.place(x=25, y=40)
        self.cevrilenbelge.place(x=15, y=0)

        self.opentrentitle = """        --------------------------------------
        |                                      |
        |              Translation             |
        |                                      |
         --------------------------------------
        """
        self.opentrenLabel = Label(self.opentrenFrame, text=f"{self.opentrentitle}", bg="#FFFFFF", fg="#787372",
                                   font=("MonoSpace", 15, "bold"))
        self.opentrenLabel.place(x=255, y=0)

        self.cevrilecekbelge = Label(self.opentrenFrame, text="Çevrilecek Dili Seçin: ", bg="#FFFFFF", fg="#787372",
                                     font=("MonoSpace", 11, "bold"))
        self.clicked2 = StringVar()
        self.clicked2.set(options1[0])
        self.cevrilecekbelgesec = OptionMenu(self.opentrenFrame, self.clicked2, *options1)
        self.cevrilecekbelgesec.place(x=900, y=40)
        self.cevrilecekbelge.place(x=900, y=0)

        self.opentrencevrilecekmetinLabel = Label(self.opentrenFrame, text="Çevrilecek Metin : ", bg="#FFFFFF", fg="#787372",
                                   font=("MonoSpace", 11, "bold"))
        self.opentrencevrilecekmetinLabel.place(x=15, y=120)

        self.scroll = Scrollbar(self.opentrenFrame, orient='vertical', bg="#FF5F1F")
        self.scroll.place(x=585, y=140)
        self.opentrencevrilecekmetinText = Text(self.opentrenFrame, width=62, height=18, bg="#FF5F1F", fg="#FFFFFF", font=("MonoSpace", 11, "bold"), yscrollcommand=self.scroll.set)
        self.opentrencevrilecekmetinText.place(x=15, y=140)
        self.scroll.config(command=self.opentrencevrilecekmetinText.yview)

        self.opentrencevrilenmetinLabel = Label(self.opentrenFrame, text="Çevrilen Metin : ", bg="#FFFFFF",
                                                  fg="#787372",
                                                  font=("MonoSpace", 11, "bold"))
        self.opentrencevrilenmetinLabel.place(x=610, y=120)

        self.scroll2 = Scrollbar(self.opentrenFrame, orient='vertical', bg="#FF5F1F")
        self.scroll2.place(x=1135, y=140)
        self.opentrencevrilenmetinText = Text(self.opentrenFrame, width=57, height=18, bg="#FF5F1F", fg="#FFFFFF",
                                                font=("MonoSpace", 11, "bold"), yscrollcommand=self.scroll2.set)
        self.opentrencevrilenmetinText.place(x=610, y=140)
        self.scroll2.config(command=self.opentrencevrilenmetinText.yview)

        self.cevirbtn = Button(self.opentrenFrame, text="Metni Çevir", bg="#FF5F1F", fg="#FFFFFF", activebackground="#FFFFFF", activeforeground="#FF5F1F",
                                                font=("MonoSpace", 11, "bold"), command= lambda: self.opentranslation(self.clicked1.get(),self.clicked2.get(),self.opentrencevrilecekmetinText.get("1.0",'end-1c')))

        self.cevirbtn.place(x=520, y=472)
        self.opentrenFrame.place(x=15, y=70)

        # OpenHakkımızda
        self.openhakkimdaFrameAcikmi = False
        self.openhakkimdaFrame = Frame(self.pencere, bg="#FFFFFF", width=930, height=510)

        self.openhakkimdatitle = """        --------------------------------------
        |                                      |
        |               Hakkımda               |
        |                                      |
         --------------------------------------
        """
        self.openhakkimdaLabel = Label(self.openhakkimdaFrame, text=f"{self.openhakkimdatitle}", bg="#FFFFFF", fg="#787372",
                                    font=("MonoSpace", 15, "bold"))
        self.openhakkimdaLabel.place(x=150, y=0)

        # self.openhakkimdaFrame.place(x=250, y=70)
        self.pencere.mainloop()

    def navmenubaropen(self):

        # OpenTrEnFrame Settings
        if self.opentrenFrameAcikmi == True:
            self.opentrenFrame.place(x=250, y=70)
            self.opentrenFrame.config(width=930, height=510)
            self.opentrenLabel.place(x=150, y=0)
            self.opentrencevrilecekmetinLabel.place(x=15, y=120)
            self.opentrencevrilecekmetinText.place(x=15, y=140)
            self.opentrencevrilecekmetinText.config(width=50)
            self.scroll.place(x=480, y=140)
            self.scroll2.place(x=910, y=140)
            self.opentrencevrilenmetinLabel.place(x=500, y=120)
            self.opentrencevrilenmetinText.place(x=500, y=140)
            self.opentrencevrilenmetinText.config(width=44)
            self.cevirbtn.place(x=410, y=472)

        # OpenHakkimdaFrame Settings
        if self.openhakkimdaFrameAcikmi == True:
            self.openhakkimdaFrame.place(x=250, y=70)
            self.openhakkimdaFrame.config(width=930, height=510)
            self.openhakkimdaLabel.place(x=150, y=0)

        self.openmenunav.place_forget()
        self.closemenunav.place(x=0, y=0)
        self.navmenubarFrame.place(x=0, y=50)

    def navmenubarclose(self):

        # OpenTrEnFrame Settings
        if self.opentrenFrameAcikmi == True:
            self.opentrenFrame.place(x=15, y=70)
            self.opentrenFrame.config(width=1167, height=510)
            self.opentrenLabel.place(x=255, y=0)
            self.opentrencevrilecekmetinLabel.place(x=15, y=120)
            self.opentrencevrilecekmetinText.place(x=15, y=140)
            self.opentrencevrilecekmetinText.config(width=62)
            self.scroll.place(x=585, y=140)
            self.scroll2.place(x=1135, y=140)
            self.opentrencevrilenmetinLabel.place(x=610, y=120)
            self.opentrencevrilenmetinText.place(x=610, y=140)
            self.opentrencevrilenmetinText.config(width=57)
            self.cevirbtn.place(x=520, y=472)

        # OpenHakkimdaFrame Settings
        if self.openhakkimdaFrameAcikmi == True:
            self.openhakkimdaFrame.place(x=15, y=70)
            self.openhakkimdaFrame.config(width=1167, height=510)
            self.openhakkimdaLabel.place(x=255, y=0)

        self.openmenunav.place(x=0, y=0)
        self.closemenunav.place_forget()
        self.navmenubarFrame.place_forget()

    def opentrans(self):

        # OpenHakkimdaFrame Check
        if self.openhakkimdaFrameAcikmi == True:
            self.openhakkimdaFrameAcikmi = False
            self.openhakkimdaFrame.place_forget()

        self.opentrenFrameAcikmi = True
        self.opentrenFrame.place(x=250, y=70)

    def openhakkimda(self):

        # OpenTrEnFrame Check
        if self.opentrenFrameAcikmi == True:
            self.opentrenFrameAcikmi = False
            self.opentrenFrame.place_forget()

        self.openhakkimdaFrameAcikmi = True
        self.openhakkimdaFrame.place(x=250, y=70)

    def opentranslation(self,cevrilecekmetin,cevrilenmetin,metin):
        if cevrilecekmetin == " " and cevrilenmetin == " ":
            print("Lütfen Dilleri Seçiniz...!")

        elif cevrilecekmetin == None and cevrilenmetin == None:
            print("Lütfen Dilleri Seçiniz...!")

        #### Türkiye ####
        elif cevrilecekmetin == "Türkçe" and cevrilenmetin == "İngilizçe":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="tr", to="en")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Türkçe" and cevrilenmetin == "Almanca":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="tr", to="de")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Türkçe" and cevrilenmetin == "Rusça":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="tr", to="ru")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Türkçe" and cevrilenmetin == "Azerbaycan":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="tr", to="az")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Türkçe" and cevrilenmetin == "Afganistan":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="tr", to="af")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Türkçe" and cevrilenmetin == "ABD":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="tr", to="us")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Türkçe" and cevrilenmetin == "Brezilya":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="tr", to="br")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Türkçe" and cevrilenmetin == "Bulgaristan":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="tr", to="bg")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Türkçe" and cevrilenmetin == "Çin":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="tr", to="cn")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Türkçe" and cevrilenmetin == "Japonya":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="tr", to="jp")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Türkçe" and cevrilenmetin == "İsveç":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="tr", to="se")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Türkçe" and cevrilenmetin == "İsviçre":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="tr", to="ch")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        ########################################################################
        #### İNGİLİZCE ####
        elif cevrilecekmetin == "İngilizçe" and cevrilenmetin == "Türkçe":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="en", to="tr")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "İngilizçe" and cevrilenmetin == "Almanca":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="en", to="de")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "İngilizçe" and cevrilenmetin == "Rusça":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="en", to="ru")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "İngilizçe" and cevrilenmetin == "Azerbaycan":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="en", to="az")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "İngilizçe" and cevrilenmetin == "Afganistan":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="en", to="af")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "İngilizçe" and cevrilenmetin == "ABD":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="en", to="us")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "İngilizçe" and cevrilenmetin == "Brezilya":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="en", to="br")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "İngilizçe" and cevrilenmetin == "Bulgaristan":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="en", to="bg")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "İngilizçe" and cevrilenmetin == "Çin":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="en", to="cn")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "İngilizçe" and cevrilenmetin == "Japonya":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="en", to="jp")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "İngilizçe" and cevrilenmetin == "İsveç":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="en", to="se")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "İngilizçe" and cevrilenmetin == "İsviçre":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="en", to="ch")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        ########################################################################
        #### ALMANYA ####
        elif cevrilecekmetin == "Almanca" and cevrilenmetin == "Türkçe":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="de", to="tr")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Almanca" and cevrilenmetin == "İngilizçe":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="de", to="de")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Almanca" and cevrilenmetin == "Rusça":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="de", to="ru")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Almanca" and cevrilenmetin == "Azerbaycan":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="de", to="az")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Almanca" and cevrilenmetin == "Afganistan":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="de", to="af")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Almanca" and cevrilenmetin == "ABD":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="de", to="us")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Almanca" and cevrilenmetin == "Brezilya":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="de", to="br")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Almanca" and cevrilenmetin == "Bulgaristan":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="de", to="bg")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Almanca" and cevrilenmetin == "Çin":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="de", to="cn")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Almanca" and cevrilenmetin == "Japonya":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="de", to="jp")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Almanca" and cevrilenmetin == "İsveç":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="de", to="se")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Almanca" and cevrilenmetin == "İsviçre":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="de", to="ch")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        ########################################################################
        #### RUSYA ####
        elif cevrilecekmetin == "Rusça" and cevrilenmetin == "Türkçe":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="ru", to="tr")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Rusça" and cevrilenmetin == "İngilizçe":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="ru", to="de")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Rusça" and cevrilenmetin == "Almanca":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="ru", to="ru")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Rusça" and cevrilenmetin == "Azerbaycan":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="ru", to="az")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Rusça" and cevrilenmetin == "Afganistan":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="ru", to="af")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Rusça" and cevrilenmetin == "ABD":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="ru", to="us")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Rusça" and cevrilenmetin == "Brezilya":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="ru", to="br")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Rusça" and cevrilenmetin == "Bulgaristan":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="ru", to="bg")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Rusça" and cevrilenmetin == "Çin":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="ru", to="cn")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Rusça" and cevrilenmetin == "Japonya":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="ru", to="jp")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Rusça" and cevrilenmetin == "İsveç":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="ru", to="se")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Rusça" and cevrilenmetin == "İsviçre":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="ru", to="ch")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        ########################################################################
        #### AZERBAYCAN ####
        elif cevrilecekmetin == "Azerbaycan" and cevrilenmetin == "Türkçe":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="az", to="tr")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Azerbaycan" and cevrilenmetin == "İngilizçe":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="az", to="de")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Azerbaycan" and cevrilenmetin == "Almanca":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="az", to="ru")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Azerbaycan" and cevrilenmetin == "Rusça":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="az", to="ru")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Azerbaycan" and cevrilenmetin == "Afganistan":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="az", to="af")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Azerbaycan" and cevrilenmetin == "ABD":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="az", to="us")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Azerbaycan" and cevrilenmetin == "Brezilya":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="ru", to="br")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Azerbaycan" and cevrilenmetin == "Bulgaristan":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="az", to="bg")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Azerbaycan" and cevrilenmetin == "Çin":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="az", to="cn")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Azerbaycan" and cevrilenmetin == "Japonya":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="az", to="jp")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Azerbaycan" and cevrilenmetin == "İsveç":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="az", to="se")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

        elif cevrilecekmetin == "Azerbaycan" and cevrilenmetin == "İsviçre":
            self.opentrencevrilenmetinText.delete("1.0", "end")
            text = TextBlob(metin)
            cevir = text.translate(from_lang="az", to="ch")
            self.opentrencevrilenmetinText.insert(END, f"{cevir}")

if __name__ == '__main__':
    Uygulama()
