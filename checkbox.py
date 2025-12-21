import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

janela = tk.Tk()
janela.title("Checkbox Exemplo")
janela.geometry("400x280")

def escolha_carreira():
    escolha = []

    if var1.get():
        escolha.append("Gerencial")
    if var2.get():
        escolha.append("Técnica")

    if not escolha:
        escolha.append("Nenhuma opção selecionada")

    messagebox.showinfo(
        "Escolha de Carreira",
        "Você escolheu:\n" + "\n".join(escolha)
    )

# Configuração da coluna
janela.columnconfigure(0, weight=1)

ttk.Label(
    janela,
    text="Escolha sua vocação:",
    font=("Arial", 12)
).grid(row=0, column=0, sticky=tk.S, padx=10, pady=20)

var1 = tk.IntVar()
ttk.Checkbutton(
    janela,
    text="Gerencial",
    variable=var1
).grid(row=1, column=0, sticky=tk.S, padx=10, pady=5)

var2 = tk.IntVar()
ttk.Checkbutton(
    janela,
    text="Técnica",
    variable=var2
).grid(row=2, column=0, sticky=tk.S, padx=10, pady=5)

ttk.Button(
    janela,
    text='Mostrar',
    command=escolha_carreira
).grid(row=3, column=0, sticky=tk.S, padx=10, pady=(10, 5))

ttk.Button(
    janela,
    text='Sair',
    command=janela.quit
).grid(row=4, column=0, sticky=tk.S, padx=10, pady=5)

janela.mainloop()
