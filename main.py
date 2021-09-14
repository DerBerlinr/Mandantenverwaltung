import sqlite3
import gui


class Person:
    def __init__(self):
        self.persnr = None
        self.name = ""
        self.vname = ""
        self.geb = ""
        self.anschrift = ""
        self.kontakt = ""

    def up(self, persnr, name="", vname="", geb="", anschrift="", kontakt=""):
        self.persnr = persnr
        self.name = name
        self.vname = vname
        self.geb = geb
        self.anschrift = anschrift
        self.kontakt = kontakt

    def update_add(self):
        conn = sqlite3.connect('Mandantenverwaltung.db')
        c = conn.cursor()

        c.execute(
            'CREATE TABLE IF NOT EXISTS person (persnr INT, name TEXT, vorname TEXT, geburtsdatum TEXT, anschrift TEXT, kontaktinformationen TEXT)')

        c.execute(
            'INSERT INTO person (persnr, name, vorname, geburtsdatum, anschrift, kontaktinformationen) VALUES (?, ?, ?, ?, ?, ?)'
            , (self.persnr, self.name, self.vname, self.geb, self.anschrift, self.kontakt))

        conn.commit()

    def update_get(self, a, b):
        conn = sqlite3.connect('Mandantenverwaltung.db')
        c = conn.cursor()

        c.execute(
            'CREATE TABLE IF NOT EXISTS person (name TEXT, vorname TEXT, geburtsdatum TEXT, anschrift TEXT, kontaktinformationen TEXT')

        conn.commit()

        c.execute(
            'SELECT * from person WHERE ? is ?', (a, b))

    def update_commit(self):
        conn = sqlite3.connect('Mandantenverwaltung.db')
        c = conn.cursor()
        print((self.persnr, self.name, self.vname, self.geb, self.anschrift, self.kontakt, self.persnr))

        c.execute(
            'UPDATE person SET persnr=? name=?, vorname=?, geburtsdatum=?, anschrift=?, kontaktinformationen=? WHERE persnr=?',
            (self.persnr, self.name, self.vname, self.geb, self.anschrift, self.kontakt, self.persnr))

        conn.commit()


class Fall:
    def __init__(self):
        self.fallnr = None
        self.name = ""
        self.vname = ""
        self.geb = ""
        self.anschrift = ""
        self.kontakt = ""

    def up(self, fallnr, name="", vname="", geb="", anschrift="", kontakt=""):
        self.fallnr = fallnr
        self.name = name
        self.vname = vname
        self.geb = geb
        self.anschrift = anschrift
        self.kontakt = kontakt

    def update_add(self):
        conn = sqlite3.connect('Mandantenverwaltung.db')
        c = conn.cursor()

        c.execute(
            'CREATE TABLE IF NOT EXISTS fall (fallnr INT, name TEXT, vorname TEXT, geburtsdatum TEXT, anschrift TEXT, kontaktinformationen TEXT)')

        c.execute(
            'INSERT INTO fall (fallnr, name, vorname, geburtsdatum, anschrift, kontaktinformationen) VALUES (?, ?, ?, ?, ?, ?)'
            , (self.fallnr, self.name, self.vname, self.geb, self.anschrift, self.kontakt))

        conn.commit()

    def update_get(self, a, b):
        conn = sqlite3.connect('Mandantenverwaltung.db')
        c = conn.cursor()

        c.execute(
            'CREATE TABLE IF NOT EXISTS fall (name TEXT, vorname TEXT, geburtsdatum TEXT, anschrift TEXT, kontaktinformationen TEXT')

        conn.commit()

        c.execute(
            'SELECT * from fall WHERE ? is ?', (a, b))

    def update_commit(self):
        conn = sqlite3.connect('Mandantenverwaltung.db')
        c = conn.cursor()
        print((self.fallnr, self.name, self.vname, self.geb, self.anschrift, self.kontakt, self.fallnr))

        c.execute(
            'UPDATE fall SET fallnr=? name=?, vorname=?, geburtsdatum=?, anschrift=?, kontaktinformationen=? WHERE fallnr=?',
            (self.fallnr, self.name, self.vname, self.geb, self.anschrift, self.kontakt, self.fallnr))

        conn.commit()

    def get_mandant(self):
        person = Person()
        conn = sqlite3.connect('Mandantenverwaltung.db')
        c = conn.cursor()
        for row in c.execute('SELECT * FROM person WHERE persnr=?', (self.name,)):
            person.up(row[0], row[1], row[2], row[3], row[4], row[5])
        return person

    def get_gegner(self):
        person = Person()
        conn = sqlite3.connect('Mandantenverwaltung.db')
        c = conn.cursor()
        for row in c.execute('SELECT * FROM person WHERE persnr=?', (self.vname,)):
            person.up(row[0], row[1], row[2], row[3], row[4], row[5])
        return person


class Main:
    def neue_person(self):
        try:
            conn = sqlite3.connect('Mandantenverwaltung.db')
            c = conn.cursor()
            for row in c.execute('SELECT MAX(persnr) FROM person'):
                n = row[0] + 1
        except:
            n = 1

        person = Person()
        person.up(n, gui.GUI_Person_Edit.name.get(), gui.GUI_Person_Edit.vname.get(), gui.GUI_Person_Edit.geburtsdatum.get(), gui.GUI_Person_Edit.anschrift.get(), gui.GUI_Person_Edit.kontakt.get())
        person.update_add()
        return person

    def vorherige_person(self, persnr):
        person = Person()
        conn = sqlite3.connect('Mandantenverwaltung.db')
        c = conn.cursor()
        for row in c.execute('SELECT * FROM person WHERE persnr=?', (str(int(persnr) - 1))):
            person.up(row[0], row[1], row[2], row[3], row[4], row[5])
        if person.persnr == None:
            return
        return person

    def folgende_person(self, persnr):
        person = Person()
        conn = sqlite3.connect('Mandantenverwaltung.db')
        c = conn.cursor()
        for row in c.execute('SELECT * FROM person WHERE persnr=?', str((persnr) + 1)):
            person.up(row[0], row[1], row[2], row[3], row[4], row[5])
        if person.persnr == None:
            return
        return person
    def neuer_fall(self):
        try:
            conn = sqlite3.connect('Mandantenverwaltung.db')
            c = conn.cursor()
            for row in c.execute('SELECT MAX(fallnr) FROM fall'):
                n = row[0] + 1
        except:
            n = 1

        fall = Fall()
        fall.up(n, gui.GUI_Fall_Edit.name.get(), gui.GUI_Fall_Edit.vname.get(), gui.GUI_Fall_Edit.geburtsdatum.get(), gui.GUI_Fall_Edit.anschrift.get(), gui.GUI_Fall_Edit.kontakt.get())
        fall.update_add()
        return fall

    def vorheriger_fall(self, fallnr):
        fall = Fall()
        conn = sqlite3.connect('Mandantenverwaltung.db')
        c = conn.cursor()
        for row in c.execute('SELECT * FROM fall WHERE fallnr=?', (str(int(fallnr) - 1))):
            fall.up(row[0], row[1], row[2], row[3], row[4], row[5])
        if fall.fallnr == None:
            return
        return fall

    def folgender_fall(self, fallnr):
        fall = Fall()
        conn = sqlite3.connect('Mandantenverwaltung.db')
        c = conn.cursor()
        for row in c.execute('SELECT * FROM fall WHERE fallnr=?', str((fallnr) + 1)):
            fall.up(row[0], row[1], row[2], row[3], row[4], row[5])
        if fall.fallnr == None:
            return
        return fall


