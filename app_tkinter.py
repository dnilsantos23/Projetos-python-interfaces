import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os

contador = 0
def contador_label(lblRotulo):
   def funcao_contar():
      global contador
      contador = contador + 1
      lblRotulo.config(text=str(contador))
      lblRotulo.after(1000, funcao_contar)
   funcao_contar()
janela = tk.Tk()
janela.title("Contagem dos Segundos")
lblRotulo = tk.Label(janela, fg="green")
lblRotulo.pack()
contador_label(lblRotulo)
btnAcao = tk.Button(janela, text='Clique aqui para Interromper a contagem', height= 20, width=50, command=janela.destroy)
btnAcao.pack()
janela.mainloop()



def submit():
    nome = entry_nome.get() # captura o nome
    idade = entry_idade.get() # captura a idade
    email = entry_email.get() # captura o email
    
   
    print(f"Nome: {nome},\nE-mail: {email}") #imprime os dados no console

    ## Verifica se os campos estão preenchidos
    if not nome or not email or not idade: # se algum campo estiver vazio
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.") # mostra uma mensagem de erro
        return
    messagebox.showinfo("Successo", f"Nome: {nome}, Age: {email}") # mostra uma mensagem de sucesso



def main():
    global entry_nome, entry_email, entry_idade # declara as variáveis globais
    # Cria a janela principal
    root = tk.Tk() # cria a janela
    root.title("Aplicativo Tkinter simples") # define o título da janela
    
    #cria um frame para organizar os widgets
    frame = tk.Frame(root) # cria um frame
    frame.pack(padx=30, pady=30) # adiciona o frame à janela com espaçamento
    
    label_nome = tk.Label(root, text="NOME:") # cria um rótulo para o nome
    label_nome.pack() # adiciona o rótulo à janela
    
    entry_nome = tk.Entry(root) # cria um campo de entrada para o nome
    entry_nome.pack() # adiciona o campo de entrada à janela
    
    label_email = tk.Label(root, text="E-MAIL:") # cria um rótulo para o email
    label_email.pack() # adiciona o rótulo à janela
    
    entry_email = tk.Entry(root) # Alterado de idade para email
    entry_email.pack() 
    
    label_idade = tk.Label(root, text="IDADE:") # cria um rótulo para a idade
    label_idade.pack() # adiciona o rótulo à janela
    
    entry_idade = tk.Entry(root) # cria um campo de entrada para a idade
    entry_idade.pack() # adiciona o campo de entrada à janela
    
    button_submit = tk.Button(root, text="ENVIAR", command=submit) 
    button_submit.pack()
    
    root.mainloop()
    

def mostrar_nomes():
    print("Nome: %s\nSobrenome: %s" % (e1.get(), e2.get()))
janela = tk.Tk()
janela.title("Aplicação GUI com o Widget Entry")
tk.Label(janela,text="Nome").grid(row=0)

tk.Label(janela,text="Sobrenome").grid(row=1)
e1 = tk.Entry(janela)
e2 = tk.Entry(janela)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
tk.Button(janela, text='Sair',command=janela.quit).grid(row=3,column=0,sticky=tk.W,pady=4)
tk.Button(janela, text='Exibir Dados', command=mostrar_nomes).grid(row=3,column=1,sticky=tk.W,pady=4)
tk.mainloop()

janela = tk.Tk()
v = tk.IntVar()
tk.Label(janela,text="""Escolha uma linguagem de programação:""",justify = tk.LEFT, padx = 20).pack()
tk.Radiobutton(janela,text="python",padx = 25,variable=v,value=1).pack(anchor=tk.W)
tk.Radiobutton(janela,text="C++",padx = 25,variable=v,value=2).pack(anchor=tk.W)
janela.mainloop()
    
if __name__ == "__main__":
    main()