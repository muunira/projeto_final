import tkinter as tk
import sqlite3

root = tk.Tk()
root.geometry('500x500')
root.title("CÁLCULO DE IMC")

def imc():
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())
    imc = peso//(altura*altura)
    resultado.config(text = f'Resultado{float(imc)}')
    if imc <= 18.5:
        print('Você está abaixo do peso.')
    elif imc > 18.5 <= imc < 24.99:
        print('Você está normal.')
    elif imc > 25 <= imc < 29.99:
        print('Você está com sobrepeso.')
    elif imc >= 30:
        print('Você está com obesidade.')

text_label = tk.Label(root, text = 'Calcule seu IMC')
text_label.pack()

entry_peso = tk.Entry(root , text = 'Digite seu peso: ')
entry_peso.pack()

entry_altura = tk.Entry(root , text = 'Digite sua altura: ')
entry_altura.pack()

resultado = tk.Label(root, text = 'Resultado: ')
resultado.pack()

btn = tk.Button(root, text = 'Calcular', command = imc)
btn.pack()

root.mainloop()