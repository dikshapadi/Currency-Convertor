from tkinter import Tk, ttk
from tkinter import *
from PIL import Image, ImageTk
import json
import requests

clr1 = "#FFFFFF"
clr2 = "#333333"
clr3 = "#569DAA"

window = Tk()
window.geometry('300x340')
window.title('Currency Convertor')
window.configure(bg=clr1)
window.resizable(height=FALSE, width=FALSE)

top = Frame(window, width=340, height=60, bg=clr1)
top.grid(row=0, column=0)

main = Frame(window, width=340, height=260, bg=clr1)
main.grid(row=1, column=0)


# API
def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
    currency1 = combo1.get()
    currency2 = combo2.get()
    amount = value.get()
    querystring = {"from": currency1, "to": currency2, "amount": amount}

    headers = {
        "X-RapidAPI-Key": "a12e70917bmsh3387789a04d76bbp1cd75cjsn39153899c063",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    formatted = '{:,.2f}'.format(converted_amount)
    result['text'] = formatted


icon = Image.open('images/icons8-currency-exchange-50.png')
icon = icon.resize((30, 30))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image=icon, compound=LEFT, text='CURRENCY CONVERTOR', height=5, padx=8, pady=30, anchor=CENTER,
                 font='Arial 15 bold', bg=clr3, fg=clr1)
app_name.place(x=0, y=0)

# main Frame
result = Label(main, compound=LEFT, width=16, height=2, pady=7, relief="solid", anchor=CENTER,
               font='Ivy 15 bold', bg=clr1, fg=clr2)
result.place(x=50, y=10)

currency = ['CAD', 'INR', 'USD', 'EUR', 'BRL']

# from label
from_label = Label(main, text="from", compound=LEFT, width=8, height=1, padx=0, pady=0, relief="flat", anchor=NW,
                   font='Ivy 10', bg=clr1, fg=clr2)
from_label.place(x=48, y=90)

combo1 = ttk.Combobox(main, width=8, justify=CENTER, font='Ivy 12 bold')
combo1['values'] = currency
combo1.place(x=50, y=115)

# to label
to_label = Label(main, text="to", compound=LEFT, width=8, height=1, padx=0, pady=0, relief="flat", anchor=NW,
                 font='Ivy 10', bg=clr1, fg=clr2)
to_label.place(x=158, y=90)

combo2 = ttk.Combobox(main, width=8, justify=CENTER, font='Ivy 12 bold')
combo2['values'] = currency
combo2.place(x=160, y=115)

# entry
value = Entry(main, width=22, justify=CENTER, font='Ivy 12 bold', relief=SOLID)
value.place(x=50, y=155)

# convertor button
button = Button(main, text="Convert", width=20, padx=5, height=1, bg=clr3, fg=clr1, font='Ivy 12 bold',
                command=convert)
button.place(x=42, y=210)

window.mainloop()
