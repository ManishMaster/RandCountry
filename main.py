from tkinter import *
import random

root = Tk()
root.title("RANDOM COUNTRIES AND CAPITALS")
root.geometry("500x500")

input00 = Entry(root)
input01 = Entry(root)


label0neg1 = Label(root, text="Enter the capital: and also the country name")
label0neg1.place(relx=0.5, rely=0.1, anchor=CENTER)

input00.place(relx=0.5, rely=0.3, anchor=CENTER)
input01.place(relx=0.5, rely=0.2, anchor=CENTER)

country_arr = []
capital_arr = []

label00 = Label(root)
label01 = Label(root)

label00.place(relx=0.5, rely=0.6, anchor=CENTER)
label01.place(relx=0.5, rely=0.7, anchor=CENTER)

label02 = Label(root)
label03 = Label(root)

label02.place(relx=0.5, rely=0.8, anchor=CENTER)
label03.place(relx=0.5, rely=0.9, anchor=CENTER)


def show_countries_show_capital():
    country_arr.append(input00.get())
    capital_arr.append(input01.get())

    label00["text"] = "The countries are: " + str(country_arr)
    label01["text"] = "The capitals are: " + str(capital_arr)


def show_countries_show_capital_random():
    length1 = len(country_arr)
    randvar = random.randint(0, length1)

    label02["text"] = " The random country: " + country_arr[randvar]
    label03["text"] = " The random capital: " + capital_arr[randvar]


button00 = Button(
    root, text="Show countries and their respective capital", command=show_countries_show_capital)
button01 = Button(
    root, text="Show random countries and random capital", command=show_countries_show_capital_random)

button00.place(relx=0.5, rely=0.4, anchor=CENTER)
button01.place(relx=0.5, rely=0.11, anchor=CENTER)

root.mainloop()
