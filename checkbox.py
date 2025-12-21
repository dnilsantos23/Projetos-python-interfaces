import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
janela = tk.Tk() # cria a janela

def escolha_carreira():  
   
   # Mostrar os dados selecionados no console
   print("Você escolheu:")
   if var1.get() == 1:
      print("Gerencial")
   if var2.get() == 1:
      print("Técnica")
   if var1.get() == 0 and var2.get() == 0:
      print("Nenhuma opção selecionada")

   # Mostra os dados selecionados na tela
   messagebox.showinfo("Escolha de Carreira", "Você escolheu:\n" + 
      ("Gerencial\n" if var1.get() == 1 else "") +
      ("Técnica\n" if var2.get() == 1 else "") +
      ("Nenhuma opção selecionada" if var1.get() == 0 and var2.get() == 0 else "")) 

ttk.Label(janela, text="Escolha sua vocação:").grid(row=0, sticky=tk.W)
var1 = tk.IntVar()
ttk.Checkbutton(janela, text="Gerencial", variable=var1).grid(row=1, sticky=tk.W)
var2 = tk.IntVar()
ttk.Checkbutton(janela, text="Técnica", variable=var2).grid(row=2, sticky=tk.W) 
ttk.Button(janela, text='Sair', command=janela.quit).grid(row=3, sticky=tk.W, pady=4) # Adiciona o botão para sair
ttk.Button(janela, text='Mostrar', command=escolha_carreira).grid(row=4, sticky=tk.W, pady=4) # Adiciona o botão para mostrar os dados


janela.mainloop()