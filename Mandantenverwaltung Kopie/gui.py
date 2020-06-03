from tkinter import *
import sqlite3
import main

class GUI_Startup(Tk):
    def __init__(self):
        Tk.__init__(self)

        rahmen1 = Frame(self, relief=SUNKEN, borderwidth=2)
        rahmen1.pack()

        farbe = "#878787"

        abstand_x = 3
        abstand_y = 3

        groesse = 20

        self.bu1 = Button(rahmen1, text="Mandanten", width=groesse, command=self.mandanten)
        self.bu1.grid(row=1, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu2 = Button(rahmen1, text="Mandantenliste", width=groesse, command=self.mandantenliste)
        self.bu2.grid(row=1, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu3 = Button(rahmen1, text="Fälle", width=groesse, command=self.faelle)
        self.bu3.grid(row=2, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu4 = Button(rahmen1, text="Fallliste", width=groesse, command=self.fallliste)
        self.bu4.grid(row=2, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

    def mandanten(self):
        person = main.Main.folgende_person(main.Main, 0)
        print(person)
        win = GUI_Person_visit(person)
        mainloop()

    def mandantenliste(self):
        pass

    def faelle(self):
        fall = main.Main.folgender_fall(main.Main, 0)
        win = GUI_Fall_visit(fall)
        mainloop()

    def fallliste(self):
        pass



class GUI_Person_list(Tk):
    def __init__(self):
        Tk.__init__(self)

        frameListbox = Frame(master=self)
        frameListbox.place()


        listboxPersonen = Listbox(frameListbox)
        listboxPersonen.pack()
        if self.get_personen():
            for i in self.get_personen():
                print(i.name)
                listboxPersonen.insert(END, i.name)


    def get_personen(self,n=0):
        list = []
        while main.Main.folgende_person(main.Main, n):
            a = main.Main.folgende_person(main.Main, n)
            list.append(a)
            n += 1
        if not main.Main.folgende_person(main.Main, n) and n < 5:
            n+=1
            GUI_Person_list.get_personen(n)

        return list
    #------------------------------WIP----------------------------------------------------


class GUI_Person_visit(Tk):
    def __init__(self, person):
        Tk.__init__(self)
        print(person.name)

        self.person = person

        rahmen1 = Frame(self, relief=SUNKEN, borderwidth=2)
        rahmen1.pack()

        farbe = "#878787"

        abstand_x = 3
        abstand_y = 3

        groesse = 20

        self.persnr = 1

        self.la1_text = StringVar()
        self.la1_text.set("Name")
        self.la1 = Label(rahmen1, textvariable=self.la1_text, width=groesse, bg=farbe, justify=CENTER)
        self.la1.grid(row=1, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.name = StringVar()
        self.name.set(person.name)
        self.la6 = Label(rahmen1, textvariable=self.name, width=groesse, bg=farbe, justify=CENTER)
        self.la6.grid(row=1, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la2_text = StringVar()
        self.la2_text.set("Vorname")
        self.la2 = Label(rahmen1, textvariable=self.la2_text, width=groesse, bg=farbe, justify=CENTER)
        self.la2.grid(row=2, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.vorname = StringVar()
        self.vorname.set(person.vname)
        self.la7 = Label(rahmen1, textvariable=self.vorname, width=groesse, bg=farbe, justify=CENTER)
        self.la7.grid(row=2, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la3_text = StringVar()
        self.la3_text.set("Geburtsdatum")
        self.la3 = Label(rahmen1, textvariable=self.la3_text, width=groesse, bg=farbe, justify=CENTER)
        self.la3.grid(row=3, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.geburtsdatum = StringVar()
        self.geburtsdatum.set(person.geb)
        self.la8 = Label(rahmen1, textvariable=self.geburtsdatum, width=groesse, bg=farbe, justify=CENTER)
        self.la8.grid(row=3, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la4_text = StringVar()
        self.la4_text.set("Anschrift")
        self.la4 = Label(rahmen1, textvariable=self.la4_text, width=groesse, bg=farbe, justify=CENTER)
        self.la4.grid(row=4, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.anschrift = StringVar()
        self.anschrift.set(person.anschrift)
        self.la9 = Label(rahmen1, textvariable=self.anschrift, width=groesse, bg=farbe, justify=CENTER)
        self.la9.grid(row=4, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la5_text = StringVar()
        self.la5_text.set("Kontaktinformationen")
        self.la5 = Label(rahmen1, textvariable=self.la5_text, width=groesse, bg=farbe, justify=CENTER)
        self.la5.grid(row=5, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.kontakt = StringVar()
        self.kontakt.set(person.kontakt)
        self.la10 = Label(rahmen1, textvariable=self.kontakt, width=groesse, bg=farbe, justify=CENTER)
        self.la10.grid(row=5, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu1 = Button(rahmen1, text="PREVIOUS", width=groesse, command=self.prev)
        self.bu1.grid(row=6, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu2 = Button(rahmen1, text="NEXT", width=groesse, command=self.next)
        self.bu2.grid(row=6, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu3 = Button(rahmen1, text="EDIT", width=groesse, command=self.edit)
        self.bu3.grid(row=7, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu4 = Button(rahmen1, text="ADD PERSON", width=groesse, command=self.add)
        self.bu4.grid(row=9, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu5 = Button(rahmen1, text="SEARCH BY NUM", width=groesse, command=self.search)
        self.bu5.grid(row=8, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu6 = Button(rahmen1, text="DELETE", width=groesse, command=self.delete)
        self.bu6.grid(row=9, column=0, sticky=E, padx=abstand_x, pady=abstand_y)



        self.search = StringVar()
        self.search.set("")
        self.en1 = Entry(rahmen1, width=groesse, textvariable=self.search)
        self.en1.grid(row=8, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

    def update_set(self):
        conn = sqlite3.connect('Mandantenverwaltung.db')
        c = conn.cursor()

        c.execute(
            'UPDATE fall SET vorname=? AND name=? AND geburtsdatum=? AND anschrift=? AND kontaktinformationen=? WHERE persnr=?',
            (self.person.vname, self.person.name, self.person.geb, self.person.anschrift, self.person.kontakt,
             self.person.persnr))

        conn.commit()

    def prev(self):
        p = main.Main()
        vor_person = p.vorherige_person(self.person.persnr)
        if vor_person:
            self.destroy()
            GUI_Person_visit(vor_person)

    def next(self):
        p = main.Main()
        nach_person = p.folgende_person(self.person.persnr)
        if nach_person:
            self.destroy()
            GUI_Person_visit(nach_person)

    def edit(self):
        person = self.person
        self.destroy()
        GUI_Person_Edit(person)

    def add(self):
        person = main.Person()
        try:
            conn = sqlite3.connect('Mandantenverwaltung.db')
            c = conn.cursor()
            for row in c.execute('SELECT MAX(persnr) FROM person'):
                n = row[0] + 1
        except:
            n = 1
        person.up(n)
        self.destroy()
        GUI_Person_Edit(person, True)

    def search(self):
        person = main.Person()
        a = self.search.get()
        b = True
        try:
            int(a)
        except:
            b = False
        if b:
            conn = sqlite3.connect('Mandantenverwaltung.db')
            c = conn.cursor()

            for row in c.execute('SELECT * FROM person WHERE persnr=?', (a,)):
                person.up(row[0], row[1], row[2], row[3], row[4], row[5])
            if person.persnr == None:
                return
            self.destroy()
            GUI_Person_visit(person)

    def delete(self):
        conn = sqlite3.connect('Mandantenverwaltung.db')
        c = conn.cursor()

        c.execute('DELETE FROM person WHERE persnr=?', (self.person.persnr,))
        for row in c.execute('SELECT count(*) from person'):
            a = row[0]
        conn.commit()
        print(self.person.persnr, "aaaaaaa")
        personn = main.Main.folgende_person(main.Main, self.person.persnr)
        ppp = self.person
        for i in range(0, a - self.person.persnr):

            person = main.Main.folgende_person(main.Main, ppp.persnr)
            print(person.persnr, "bbbbbbbb")
            person.persnr -= 1
            person.update_commit()

        self.destroy()
        GUI_Person_visit(personn)



class GUI_Person_Edit(Tk):
    def __init__(self, person, new=False):
        Tk.__init__(self)
        self.new = new

        self.person = person
        self.dest = False

        rahmen1 = Frame(self, relief=SUNKEN, borderwidth=2)
        rahmen1.pack()

        farbe = "#878787"

        abstand_x = 3
        abstand_y = 3

        groesse = 20

        self.persnr = 1

        self.la1_text = StringVar()
        self.la1_text.set("Name")
        self.la1 = Label(rahmen1, textvariable=self.la1_text, width=groesse, bg=farbe, justify=CENTER)
        self.la1.grid(row=1, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.name = StringVar()
        self.name.set(person.name)
        print(self.person.name)
        self.en1 = Entry(rahmen1, width=groesse, textvariable=self.name)
        self.en1.grid(row=1, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la2_text = StringVar()
        self.la2_text.set("Vorname")
        self.la2 = Label(rahmen1, textvariable=self.la2_text, width=groesse, bg=farbe, justify=CENTER)
        self.la2.grid(row=2, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.vorname = StringVar()
        self.vorname.set(person.vname)
        self.en2 = Entry(rahmen1, width=groesse, textvariable=self.vorname)
        self.en2.grid(row=2, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la3_text = StringVar()
        self.la3_text.set("Geburtsdatum")
        self.la3 = Label(rahmen1, textvariable=self.la3_text, width=groesse, bg=farbe, justify=CENTER)
        self.la3.grid(row=3, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.geburtsdatum = StringVar()
        self.geburtsdatum.set(person.geb)
        self.en3 = Entry(rahmen1, width=groesse, textvariable=self.geburtsdatum)
        self.en3.grid(row=3, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la4_text = StringVar()
        self.la4_text.set("Anschrift")
        self.la4 = Label(rahmen1, textvariable=self.la4_text, width=groesse, bg=farbe, justify=CENTER)
        self.la4.grid(row=4, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.anschrift = StringVar()
        self.anschrift.set(person.anschrift)
        self.en4 = Entry(rahmen1, width=groesse, textvariable=self.anschrift)
        self.en4.grid(row=4, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la5_text = StringVar()
        self.la5_text.set("Kontaktinformationen")
        self.la5 = Label(rahmen1, textvariable=self.la5_text, width=groesse, bg=farbe, justify=CENTER)
        self.la5.grid(row=5, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.kontakt = StringVar()
        self.kontakt.set(person.kontakt)
        self.en5 = Entry(rahmen1, width=groesse, textvariable=self.kontakt)
        self.en5.grid(row=5, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu3 = Button(rahmen1, text="SAVE", width=groesse, command=self.done)
        self.bu3.grid(row=7, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

    def done(self):
        person = self.person
        person.vname = self.vorname.get()
        person.name = self.name.get()
        person.geb = self.geburtsdatum.get()
        person.anschrift = self.anschrift.get()
        person.kontakt = self.kontakt.get()
        if self.new:
            person.update_add()
        else:
            person.update_commit()
        self.destroy()
        GUI_Person_visit(person)


class GUI_Fall_visit(Tk):
    def __init__(self, fall):
        Tk.__init__(self)
        print(fall.name)

        self.fall = fall

        rahmen1 = Frame(self, relief=SUNKEN, borderwidth=2)
        rahmen1.pack()

        farbe = "#878787"

        abstand_x = 3
        abstand_y = 3

        groesse = 20

        self.fallnr = 1

        self.la1_text = StringVar()
        self.la1_text.set("Mandant")
        self.la1 = Label(rahmen1, textvariable=self.la1_text, width=groesse, bg=farbe, justify=CENTER)
        self.la1.grid(row=1, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.name = StringVar()
        self.name.set(fall.get_mandant().name)
        self.la6 = Label(rahmen1, textvariable=self.name, width=groesse, bg=farbe, justify=CENTER)
        self.la6.grid(row=1, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la2_text = StringVar()
        self.la2_text.set("Gegner")
        self.la2 = Label(rahmen1, textvariable=self.la2_text, width=groesse, bg=farbe, justify=CENTER)
        self.la2.grid(row=2, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.vorname = StringVar()
        self.vorname.set(fall.get_gegner().name)
        self.la7 = Label(rahmen1, textvariable=self.vorname, width=groesse, bg=farbe, justify=CENTER)
        self.la7.grid(row=2, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la3_text = StringVar()
        self.la3_text.set("Dokumentpfad")
        self.la3 = Label(rahmen1, textvariable=self.la3_text, width=groesse, bg=farbe, justify=CENTER)
        self.la3.grid(row=3, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.geburtsdatum = StringVar()
        self.geburtsdatum.set(fall.geb)
        self.la8 = Label(rahmen1, textvariable=self.geburtsdatum, width=groesse, bg=farbe, justify=CENTER)
        self.la8.grid(row=3, column=1, sticky=E, padx=abstand_x, pady=abstand_y)


        self.bu1 = Button(rahmen1, text="PREVIOUS", width=groesse, command=self.prev)
        self.bu1.grid(row=4, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu2 = Button(rahmen1, text="NEXT", width=groesse, command=self.next)
        self.bu2.grid(row=4, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu3 = Button(rahmen1, text="EDIT", width=groesse, command=self.edit)
        self.bu3.grid(row=5, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu4 = Button(rahmen1, text="ADD Fall", width=groesse, command=self.add)
        self.bu4.grid(row=7, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu5 = Button(rahmen1, text="SEARCH BY NUM", width=groesse, command=self.search)
        self.bu5.grid(row=6, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu6 = Button(rahmen1, text="DELETE", width=groesse, command=self.delete)
        self.bu6.grid(row=7, column=0, sticky=E, padx=abstand_x, pady=abstand_y)



        self.search = StringVar()
        self.search.set("")
        self.en1 = Entry(rahmen1, width=groesse, textvariable=self.search)
        self.en1.grid(row=6, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

    def update_set(self):
        conn = sqlite3.connect('Mandantenverwaltung.db')
        c = conn.cursor()

        c.execute(
            'UPDATE fall SET vorname=? AND name=? AND geburtsdatum=? AND anschrift=? AND kontaktinformationen=? WHERE fallnr=?',
            (self.fall.vname, self.fall.name, self.fall.geb, self.fall.anschrift, self.fall.kontakt,
             self.fall.fallnr))

        conn.commit()

    def prev(self):
        p = main.Main()
        vor_fall = p.vorheriger_fall(self.fall.fallnr)
        if vor_fall:
            self.destroy()
            GUI_Fall_visit(vor_fall)

    def next(self):
        p = main.Main()
        nach_fall = p.folgender_fall(self.fall.fallnr)
        if nach_fall:
            self.destroy()
            GUI_Fall_visit(nach_fall)

    def edit(self):
        fall = self.fall
        self.destroy()
        GUI_Fall_Edit(fall)

    def add(self):
        fall = main.Fall()
        try:
            conn = sqlite3.connect('Mandantenverwaltung.db')
            c = conn.cursor()
            for row in c.execute('SELECT MAX(fallnr) FROM fall'):
                n = row[0] + 1
        except:
            n = 1
        fall.up(n)
        self.destroy()
        GUI_Fall_Edit(fall, True)

    def search(self):
        fall = main.Fall()
        a = self.search.get()
        b = True
        try:
            int(a)
        except:
            b = False
        if b:
            conn = sqlite3.connect('Mandantenverwaltung.db')
            c = conn.cursor()

            for row in c.execute('SELECT * FROM fall WHERE fallnr=?', (a,)):
                fall.up(row[0], row[1], row[2], row[3], row[4], row[5])
            if fall.fallnr == None:
                return
            self.destroy()
            GUI_Fall_visit(fall)

    def delete(self):
        pass



class GUI_Fall_Edit(Tk):
    def __init__(self, fall, new=False):
        Tk.__init__(self)
        self.new = new

        self.fall = fall
        self.dest = False

        rahmen1 = Frame(self, relief=SUNKEN, borderwidth=2)
        rahmen1.pack()

        farbe = "#878787"

        abstand_x = 3
        abstand_y = 3

        groesse = 20

        self.fallnr = 1

        self.la1_text = StringVar()
        self.la1_text.set("Mandant(persnr)")
        self.la1 = Label(rahmen1, textvariable=self.la1_text, width=groesse, bg=farbe, justify=CENTER)
        self.la1.grid(row=1, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.name = StringVar()
        self.name.set(fall.name)
        print(self.fall.name)
        self.en1 = Entry(rahmen1, width=groesse, textvariable=self.name)
        self.en1.grid(row=1, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la2_text = StringVar()
        self.la2_text.set("Gegner(persnr)")
        self.la2 = Label(rahmen1, textvariable=self.la2_text, width=groesse, bg=farbe, justify=CENTER)
        self.la2.grid(row=2, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.vorname = StringVar()
        self.vorname.set(fall.vname)
        self.en2 = Entry(rahmen1, width=groesse, textvariable=self.vorname)
        self.en2.grid(row=2, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la3_text = StringVar()
        self.la3_text.set("Dokumentpfad")
        self.la3 = Label(rahmen1, textvariable=self.la3_text, width=groesse, bg=farbe, justify=CENTER)
        self.la3.grid(row=3, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.geburtsdatum = StringVar()
        self.geburtsdatum.set(fall.geb)
        self.en3 = Entry(rahmen1, width=groesse, textvariable=self.geburtsdatum)
        self.en3.grid(row=3, column=1, sticky=E, padx=abstand_x, pady=abstand_y)



        self.bu3 = Button(rahmen1, text="SAVE", width=groesse, command=self.done)
        self.bu3.grid(row=7, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

    def done(self):
        fall = self.fall
        fall.vname = self.vorname.get()
        fall.name = self.name.get()
        fall.geb = self.geburtsdatum.get()
        if self.new:
            fall.update_add()
        else:
            fall.update_commit()
        self.destroy()
        GUI_Fall_visit(fall)



if __name__ == '__main__':
    #FÜR FALLANSICHT AUSKOMMENTIEREN
    #person = main.Main.folgender_fall(main.Main, 0)
    #print(person)
    #win = GUI_Fall_visit(person)
    #mainloop()
    #-------------------------------------------------
    person = main.Main.folgende_person(main.Main, 0)
    print(person)
    win = GUI_Person_visit(person)
    mainloop()