from tkinter import *
from tkinter import messagebox
import requests


def przelicz():
    z = waluta1.get()
    do = waluta2.get()
    ile = ilosc.get()
    try:
        ile = float(ile)
    except:
        messagebox.showwarning("Uwaga", "Najpierw podaj ilość!")
        return
    try:
        waluty = requests.get("https://open.er-api.com/v6/latest/" + z).json()
        kurs = waluty["rates"][do]
        print(kurs, kurs * ile)
        wartoscVar.set(round(kurs * ile, 2))
    except:
        messagebox.showerror("Błąd", "Błąd połączenia z API")
    return


print("Rates By Exchange Rate API (https://www.exchangerate-api.com)")
root = Tk()

root.geometry("400x200")
root.title("Przelicznik walut")
root.minsize(400, 200)

label0 = Label(root, text="Przelicznik walut", font="16px")

label1 = Label(root, text="Podaj ilość:")
label2 = Label(root, text="Z:")
label3 = Label(root, text="Do:")
label4 = Label(root, text="Wartość:")

label0.grid(row=0, column=0, columnspan=2)
label1.grid(row=1, column=0)
label2.grid(row=2, column=0)
label3.grid(row=3, column=0)
label4.grid(row=4, column=0)

waluta1 = StringVar(root)
waluta2 = StringVar(root)
wartoscVar = StringVar(root)
waluta1.set("USD")
waluta2.set("PLN")
wartoscVar.set("00.00")

ilosc = Entry(root)
wartosc = Entry(root, state="disabled", textvariable=wartoscVar)

waluty = requests.get("https://open.er-api.com/v6/latest/USD").json()
waluty = waluty["rates"].keys()

walutaZ = OptionMenu(root, waluta1, *waluty)
walutaZ.grid(row=2, column=1)
walutaDo = OptionMenu(root, waluta2, *waluty)
walutaDo.grid(row=3, column=1)

ilosc.grid(row=1, column=1)
wartosc.grid(row=4, column=1)

button = Button(root, text="Zamień", command=przelicz)
button.grid(row=5, column=0, columnspan=2, pady=5)

label5 = Label(root, text="Author Alan Kołodziej")
label6 = Label(root, text="Rates By Exchange Rate API (https://www.exchangerate-api.com)")
label5.grid(row=6, column=0, columnspan=2, sticky="W")
label6.grid(row=7, column=0, columnspan=2, sticky="W")
root.mainloop()
