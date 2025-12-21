import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os

contador = 0
#Janela contador de segundos
def contador_label(lblRotulo):
    def funcao_contar():
        global contador
        contador += 1
        lblRotulo.config(text=str(contador))
        lblRotulo.after(1000, funcao_contar)
    funcao_contar()
janela = tk.Tk()
janela.title("Contagem dos Segundos")
lblRotulo = tk.Label(janela, fg="green", anchor="center", justify='center', font=("Verdana", 30))
lblRotulo.pack()
contador_label(lblRotulo)
btnAcao = tk.Button(janela, text='Clique aqui para Interromper a contagem', height= 20, width=50, command=janela.destroy)
btnAcao.pack()
janela.mainloop()

# Formulário simples com validação
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



# Radio Buttons
janela = tk.Tk() # cria a janela
janela.geometry("300x200") # define o tamanho da janela
v = tk.IntVar()# variável para armazenar o valor selecionado
tk.Label(janela,text="""Escolha uma linguagem de programação:""",justify = tk.LEFT, padx = 20).pack() #.pack() empacota o widget na janela
tk.Radiobutton(janela,text="python",padx = 25,variable=v,value=1).pack(anchor=tk.W)#.pack() empacota o widget na janela
tk.Radiobutton(janela,text="C++",padx = 25,variable=v,value=2).pack(anchor=tk.W)
janela.mainloop()# inicia o loop principal da janela

# Entry Widget
def mostrar_nomes():
    print("Nome: %s\nSobrenome: %s" % (e1.get(), e2.get()))
janela = tk.Tk() # cria a janela
janela.geometry("300x120") # define o tamanho da janela
janela.title("Aplicação GUI com o Widget Entry") # define o título da janela
tk.Label(janela,text="Nome").grid(row=0) # cria um rótulo para o nome

tk.Label(janela,text="Sobrenome").grid(row=1)
e1 = tk.Entry(janela)
e2 = tk.Entry(janela)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
tk.Button(janela, text='Sair',command=janela.destroy).grid(row=3,column=0,sticky=tk.W,pady=4)
tk.Button(janela, text='Exibir Dados', command=mostrar_nomes).grid(row=3,column=1,sticky=tk.W,pady=4)
tk.mainloop()

def main():
    global entry_nome, entry_email, entry_idade # declara as variáveis globais
    # Cria a janela principal
    root = tk.Tk() # cria a janela
    root.title("Aplicativo Tkinter simples") # define o título da janela
    root.geometry("400x400") # define o tamanho da janela
    
    #cria um frame para organizar os widgets
    frame = tk.Frame(root, padx=20, pady=20) # cria um frame
    frame.pack(fill='both', expand=True) # adiciona o frame à janela com espaçamento
    
    tk.Label(frame, text="NOME:").pack(anchor='w') # cria um rótulo para o nome
    entry_nome = tk.Entry(frame) # cria um campo de entrada para o nome
    entry_nome.pack(fill='x', pady=5) # adiciona o campo de entrada à janela com espaçamento

    tk.Label(frame, text="E-MAIL:").pack(anchor='w', pady=(0, 10)) # cria um rótulo para o email
    entry_email = tk.Entry(frame) # cria um campo de entrada para o email
    entry_email.pack(fill='x', pady=5) # adiciona o rótulo à janela

    tk.Label(frame, text="IDADE:").pack(anchor='w', pady=(0, 10)) # cria um rótulo para a idade
    entry_idade = tk.Entry(frame) # cria um campo de entrada para a idade
    entry_idade.pack(fill='x', pady=5) # adiciona o campo de entrada à janela
    
    button_submit = tk.Button(root, text="ENVIAR", command=submit) # cria o botão de envio
    button_submit.pack(pady=(0, 20)) # adiciona o botão à janela com espaçamento
    
    root.mainloop()
    
if __name__ == "__main__":
    main()