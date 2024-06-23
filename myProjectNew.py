import tkinter as tk

# window
pencere = tk.Tk()
pencere.title("BMI Calculator")
pencere.geometry("300x200")

# function
def hesapla():
  try:
    boy = float(boy_girdisi.get())
    kilo = float(kilo_girdisi.get())
    vki = kilo / (boy / 100) ** 2
    result_string = write_result(vki)
    vki_sonucu.config(text=result_string)
  except ValueError:
    vki_sonucu.config(text="Hatalı Giriş!")

# user login
boy_etiketi = tk.Label(pencere, text="Boy (cm):")
boy_etiketi.grid(row=0, column=0, padx=5, pady=5)

boy_girdisi = tk.Entry(pencere)
boy_girdisi.grid(row=0, column=1, padx=5, pady=5)

kilo_etiketi = tk.Label(pencere, text="Kilo (kg):")
kilo_etiketi.grid(row=1, column=0, padx=5, pady=5)

kilo_girdisi = tk.Entry(pencere)
kilo_girdisi.grid(row=1, column=1, padx=5, pady=5)

hesaplama_dugmesi = tk.Button(pencere, text="Hesapla", command=hesapla)
hesaplama_dugmesi.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

vki_sonucu = tk.Label(pencere, text="")
vki_sonucu.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# function2
def write_result(vki):
    result_string = f"Your BMI is: {round(vki, 2)}. You are "
    if vki <= 16:
        result_string += "severaly thin !"
    elif 16 < vki <= 17:
        result_string += "moderately thin !"
    elif 17 < vki <= 18.5:
        result_string += "mild thin !"
    elif 18.5 < vki <= 25:
        result_string += "normal"
    elif 25 < vki <= 30:
        result_string += "overweight"
    elif 30 < vki <= 35:
        result_string += "obese class1 !"
    elif 35 < vki <= 40:
        result_string += "obese class2 !"
    else:
        result_string += "obese class3 !"
    return result_string

pencere.mainloop()
