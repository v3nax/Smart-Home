
from tkinter import *
import sqlite3

#varijable
tipkovnica = ['1','2','3','4','5','6','7','8','9','0']
k_list = []
unosi = []
unos_pin = ''

#stilovi
visina = 700
sirina = 610
boja_pozadine = '#ffffff'

#glavni prozor
SmartKey = Tk()
SmartKey.title('Smart Key')
#SmartKey.resizable(width=False, height=False)

screenwidth = SmartKey.winfo_screenwidth()
screenheight = SmartKey.winfo_screenheight()

SmartKey.pack_propagate()

#importanje baze
conn = sqlite3.connect("Ukucani.db")

c = conn.cursor()

c = conn.cursor()
c.execute("SELECT * FROM Ukucani")
svi_ukucani = c.fetchall()

#glavni okvir
sadrzaj = Frame(SmartKey, width=50, height=70,bg=boja_pozadine)
sadrzaj.grid(column=0, columnspan=3, row=0, rowspan=3)

#sporedni okviri
okvir1 = LabelFrame(sadrzaj, text='Panel s gumbima', borderwidth=2, width=310,padx=240, pady=20,bg=boja_pozadine)
okvir2 = LabelFrame (sadrzaj, text='Glavni panel',  borderwidth=2, width=300, height=150 , padx=0, pady=10,bg=boja_pozadine)
okvir3 = LabelFrame (sadrzaj, text='Upravljanje dodijeljenim kljucevima',  borderwidth=2, width=200, padx=40,bg=boja_pozadine)

#sporedni: panel za pocetak
okvir1.columnconfigure((0, 1, 2), weight=1, minsize=90)
okvir1.grid(row=0, column=0,padx=10, pady=2, ipadx=150, ipady=40)

#okviri unutar sporednih okvira
okvir4 = LabelFrame (okvir2, text='PIN panel',  borderwidth=2, width=50, bg=boja_pozadine)
improvizacija = Label (okvir2, text='DOBRODOSLI!', borderwidth=2, width=30,height=15, bg=boja_pozadine)

status = LabelFrame(okvir2,borderwidth=1, text='Poruka', bg=boja_pozadine)
status.grid(row=0, column=4, rowspan=5)
status.place(x=240, y=0, width=300, height=225)

#konfiguracija admin-panela

#listbox operacije
lista_ukucana = Listbox(okvir3, borderwidth=1, bg=boja_pozadine, width=30, height=15, background='#F7ECEA')
lista_ukucana.grid(row=0, column=0, rowspan=6,padx=10, pady=10)
lista_ukucana.insert(0, 'LISTA UKUCANA:\n')

def oznaci_ukucana(event):
    for i in lista_ukucana.curselection():
        lista = lista_ukucana.get(i)
    
        ime.delete(0, END)
        prezime.delete(0,END)
        PIN_ukucan.delete(0,END)

        ime.insert(0, lista[1])
        prezime.insert(0, lista[2])
        PIN_ukucan.insert(0, lista[3])
    
    return

for ukucan in svi_ukucani:
    lista_ukucana.insert(END, ukucan)
    print(ukucan)

lista_ukucana.bind('<<ListboxSelect>>', oznaci_ukucana)
conn.commit()


ime_text= Label(okvir3, text='Ime: ', justify='right',width=10,height=1, borderwidth=0,bg=boja_pozadine)
ime_text.grid(row=0, column=1,padx=5, pady=10)
ime = Entry(okvir3,width=20,bg='#F7ECEA')
ime.grid(row=0, column=2,padx=5, pady=10)

prezime_text= Label(okvir3, text='Prezime: ',justify=RIGHT,width=10,height=1, borderwidth=0,bg=boja_pozadine)
prezime_text.grid(row=1, column=1,padx=5, pady=10)
prezime = Entry(okvir3,width=20,bg='#F7ECEA')
prezime.grid(row=1, column=2,padx=5, pady=10)

pin_text= Label(okvir3, text='PIN: ',justify=RIGHT, width=10,height=1, borderwidth=0,bg=boja_pozadine)
pin_text.grid(row=2, column=1,padx=5, pady=10)
PIN_ukucan = Entry(okvir3,width=20,bg='#F7ECEA')
PIN_ukucan.grid(row=2, column=2,padx=5, pady=10)

#CheckVar = IntVar(value=True)

aktiviranje_text= Label(okvir3, text='Aktivirati: ',justify=RIGHT, width=10,height=1, borderwidth=0,bg=boja_pozadine)
aktiviranje_text.grid(row=3, column=1,padx=5, pady=10)
#aktiviranje = Checkbutton(okvir3,borderwidth='1px',width=1,bg=boja_pozadine,justify="right",variable=CheckVar)
#aktiviranje.grid(row=3, column=2,padx=0, pady=0)

spremi = Button(okvir3, text='Spremi', width=10, command=lambda:[unesi()])
spremi.grid(row=5, column=1,padx=5, pady=2)

izbrisi = Button(okvir3, text='Izbrisi',width=10,command=lambda:obrisati_ukucana())
izbrisi.grid(row=5, column=2,padx=5, pady=2)

odustani = Button(okvir3, text='Odustani',width=10, command=lambda:odustati())
odustani.grid(row=5,column=3,padx=5, pady=2)


#gumbi za pocetak
pozvoni = Button (okvir1, text='Pozvoni', command=lambda:pozvoniti())
otkljucaj = Button (okvir1, text='Otkljucaj', command=lambda:otkljucati())

pozvoni.grid(row=0,column=0)
pozvoni.place(x=-100, y=0, width=70, height=25)

otkljucaj.grid(row=0,column=3)
otkljucaj.place(x=150, y=0, width=70, height=25)

#Entry za pin
pin1 = Entry(okvir4, show="*", width=5,bg='#F7ECEA')
pin2 = Entry(okvir4, show="*", width=5,bg='#F7ECEA')
pin3 = Entry(okvir4, show="*", width=5,bg='#F7ECEA')
pin4 = Entry(okvir4, show="*", width=5,bg='#F7ECEA')

pin1.grid(row=0, column=0, pady=2, padx=5)
pin2.grid(row=0, column=1, pady=2, padx=5)
pin3.grid(row=0, column=2, pady=2, padx=5)
pin4.grid(row=0, column=3, pady=2, padx=5)

unosi = [pin1,pin2,pin3,pin4]

#brojevna tipkovnica
r = 1
c = 0
for b in tipkovnica:
    b = Button(okvir4, text=b, padx=10, pady=10, command=lambda btn=b:tipkaj(btn))
    b.grid(row=r,column=c)
    c += 1
    if c > 2:
        c = 0
        r += 1

#gumbi za provjeru
ok_gumb=Button(okvir4, text='OK', padx=26, pady=10, command = lambda:provjera())
ok_gumb.grid(row=4, column=1, columnspan=2)

clear_gumb=Button(okvir4, text='C', padx=10, pady=10, command = lambda:brisanje())
clear_gumb.grid(row=4, column=3)

#poruke
poruka_gost = LabelFrame(status, borderwidth=0, width=40, bg=boja_pozadine)
poruka_ukucan = Label(status, borderwidth=0, width=40, bg=boja_pozadine)
poruka_admin = Label(status, borderwidth=0, width=40, bg=boja_pozadine)

def unesi():
    c = conn.cursor()
    i = len(svi_ukucani) + 1
    
    sql = f'''  INSERT INTO Ukucani 
                    VALUES('{i}', '{str(ime.get())}', '{str(prezime.get())}', '{str(PIN_ukucan.get())}')'''

    c.execute(sql)
    oznaci_sve_prema_id(i)
    novi = c.fetchall()
    lista_ukucana.insert(END, novi)
    print('Uspjesno pohranjeno!')
    ime.delete(0, END)
    prezime.delete(0, END)
    PIN_ukucan.delete(0, END)
    ime.focus_set()
    conn.commit()
    
    return c.lastrowid

def odustati():
    ime.delete(0, END)
    prezime.delete(0, END)
    PIN_ukucan.delete(0, END)
    ime.focus_set()

def ocisti_prouke():
    poruka_admin.pack_forget()
    poruka_ukucan.pack_forget()
    poruka_gost.pack_forget()

def vrati():
    okvir2.grid_forget()
    okvir4.grid_forget()
    improvizacija.grid_forget()


def ocisti_okvire():
    okvir4.grid_forget()
    improvizacija.grid_forget()
    okvir3.grid_forget()
    pozvoni['state'] = NORMAL
    otkljucaj['state'] = NORMAL
    
def pozvoniti():
    ocisti_okvire()
    ocisti_prouke()

    poruka_gost.pack()
    
    okvir2.columnconfigure((0, 1, 2, 3, 4), weight=1, minsize=86)
    okvir2.grid(row=1, column=0,padx=0, pady=5, ipadx=2, ipady=0)

    improvizacija.grid(row=0, column=0,padx=0, pady=0, ipadx=20, ipady=5)

    klik = Label(poruka_gost,text='Pozvonili ste, pricekajte otvaranje vrata.', width=40, height=10, bg=boja_pozadine)
    klik.grid(row=0, column=4)

    ok = Button(poruka_gost, text='OK', command=lambda: [ocisti_prouke(),vrati(), ocisti_okvire()])
    ok.grid(row=1, column=4)

def otkljucati():
    ocisti_prouke()
    ocisti_okvire()
    okvir2.columnconfigure((0, 1, 2, 3, 4), weight=1, minsize=90)
    okvir2.grid(row=1, column=0,padx=0, pady=5, ipadx=2, ipady=0)

    okvir4.grid(row=0, column=0,padx=15, pady=2, ipadx=15, ipady=2)
    poruka_ukucan.pack()

    klik = Label(poruka_ukucan,text='Unesite svoj pin', width=40, height=10, bg=boja_pozadine)
    klik.grid(row=0, column=0)

    izadji = Button(poruka_ukucan, text='Izadji', command=lambda:[ocisti_prouke(),vrati(), ocisti_okvire()])
    izadji.grid(row=1, column=0)

def brisanje():
    pin1.configure(state=NORMAL)
    pin1.focus_set()
    pin2.configure(state=NORMAL)
    pin3.configure(state=NORMAL)
    pin4.configure(state=NORMAL)
    pin1.delete(0, END)
    pin2.delete(0, END)
    pin3.delete(0, END)
    pin4.delete(0, END)
    k_list.clear()

def tipkaj(b):
    global unos_pin
    unos_pin = ''.join(k_list)
    if len(pin1.get()) == 0:
        pin1.delete(0, END)
        pin1.insert(END, b)
        unos_pin = unos_pin + str(pin1.get())
        k_list.append(pin1.get())
        pin1.configure(state=DISABLED)
    elif len(pin1.get()) == 1 and len(pin2.get()) == 0:
        pin2.focus()
        pin2.delete(0,END)
        pin2.insert(END, b)
        k_list.append(pin2.get())
        unos_pin = unos_pin + str(pin2.get())
        pin2.configure(state=DISABLED)
    elif len(pin2.get()) == 1 and len(pin3.get()) == 0:
        pin3.focus()
        pin3.delete(0,END)
        pin3.insert(END, b)
        unos_pin = unos_pin + str(pin3.get())
        k_list.append(pin3.get())
        pin3.configure(state=DISABLED)
    elif len(pin3.get()) == 1 and len(pin4.get()) == 0:
        pin4.focus()
        pin4.delete(0,END)
        pin4.insert(END, b)
        unos_pin = unos_pin + str(pin4.get())
        k_list.append(pin4.get())
        pin4.configure(state=DISABLED)
    else:
        brisanje()

    print(k_list)
    print(unos_pin)

    if len(k_list) == 4:
        for pin in unosi:
            pin.configure(state=DISABLED)

def provjera():
    ocisti_prouke()
    poruka = Label(poruka_admin,text='', width=40, height=10,bg=boja_pozadine)
    poruka.grid(row=0, column=0)
    provjera_admin=svi_ukucani[0][3]
    print(svi_ukucani[0][3])

    if unos_pin == provjera_admin:
        poruka.configure(text=f'Dobrodosao {svi_ukucani[0][1]} {svi_ukucani[0][2]}!')

        izadji = Button(poruka_admin, text='Izadji', width=10, command=lambda: [ocisti_prouke(),brisanje(),vrati(),ocisti_okvire()])
        izadji.grid(row=1, column=0)
        
        okvir3.columnconfigure((0, 1, 2, 3), weight=1, minsize=50)
        okvir3.grid(row=2, column=0, padx=5, pady=2, ipadx=0, ipady=2)
        pozvoni['state'] = DISABLED
        otkljucaj['state'] = DISABLED

        poruka_admin.pack()  

    elif (unos_pin in svi_ukucani):
        for i in svi_ukucani:
            poruka.configure(text=f'Dobrodosao kuci {svi_ukucani[i][1]} {svi_ukucani[i][2]}!')

        izadji = Button(poruka_admin, text='Izadji', width=10, command=lambda: [ocisti_prouke(),brisanje(),vrati(),ocisti_okvire()])
        izadji.grid(row=1, column=0)
        
        pozvoni['state'] = DISABLED
        otkljucaj['state'] = DISABLED

        poruka_admin.pack() 

    else:
        poruka_admin.pack()
        poruka.configure(text='Pogresan pin! Pokusajte ponovo.')

        ponovi = Button(poruka_admin, text='Ponovi', width=10, command=lambda: [ocisti_prouke(),brisanje()])
        ponovi.grid(row=1, column=0)


#SQLite REPO

def create_table(db_connection, create_table_sql):
    try:
        cursor = db_connection.cursor()
        cursor.execute(create_table_sql)
    
    except sqlite3.Error as db_error:
        print(db_error)

def update_ukucana():
    i = lista_ukucana.curselection()[0]
    cursor = conn.cursor()
    cursor.execute(f''' UPDATE Ukucani
              SET Ime = '{ime.get()}' ,
                  Prezime = '{prezime.get()}',
                  Pin = '{PIN_ukucan.get()}'
              WHERE id = '{i}' ''')
    print('Uspjesno pohranjeno!')
    conn.commit()
    
    


# Metoda za brisanje zapisa o djelatniku u tabeli na osnovu ID broja retka
def obrisati_ukucana():
    
    cursor = conn.cursor()
    select = lista_ukucana.curselection()[0]
    cursor.execute(f''' DELETE FROM Ukucani WHERE id='{select}' ''')
    print('Uspjesno ste obrisali ukucana')
    conn.commit()
    lista_ukucana.delete(select, END)
    ime.delete(0, END)
    prezime.delete(0, END)
    PIN_ukucan.delete(0, END)
    ime.focus_set()

def ocisti_tablicu(db_connection):
    sql = 'DELETE FROM Ukucani'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    db_connection.commit()


# Metoda za dohvat svih zapisa o djelatnicima
def oznaci_sve_ukucane(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM Ukucani")

    rows = cursor.fetchall()

    for row in rows:
        print(row)


def oznaci_sve_prema_id(db_connection, id):

    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM Ukucani WHERE priority=?", (id,))


    rows = cursor.fetchall()

    for row in rows:
        print(row)




SmartKey.mainloop()
