from tkinter import *

def gravar_consulta():
    nome = str(caixa_nome.get())
    rg = str(caixa_rg.get())
    telefone = str(caixa_telefone.get())
    data = str(caixa_data.get())
    hora = str(caixa_hora.get())
    arquivo = open("consultas.txt", "a")
    arquivo.write("Nome:..............{} \n".format(nome))
    arquivo.write("RG:................{}\n".format(rg))
    arquivo.write("Telefone:..........{} \n".format(telefone))
    arquivo.write("Data:..............{} \n".format(data))
    arquivo.write("Horário:...........{} \n".format(hora))
    arquivo.close()
    
def gravar_exame():
    nome = str(caixa_nome.get())
    rg = str(caixa_rg.get())
    telefone = str(caixa_telefone.get())
    data = str(caixa_data.get())
    hora = str(caixa_hora.get())
    arquivo = open("exames.txt", "a")
    arquivo.write("Nome:..............{} \n".format(nome))
    arquivo.write("RG:................{}\n".format(rg))
    arquivo.write("Telefone:..........{} \n".format(telefone))
    arquivo.write("Data:..............{} \n".format(data))
    arquivo.write("Horário:...........{} \n".format(hora))
    arquivo.close()
    
def gravar_cirurgia():
    nome = str(caixa_nome.get())
    rg = str(caixa_rg.get())
    telefone = str(caixa_telefone.get())
    data = str(caixa_data.get())
    hora = str(caixa_hora.get())
    arquivo = open("cirurgias.txt", "a")
    arquivo.write("Nome:..............{} \n".format(nome))
    arquivo.write("RG:................{}\n".format(rg))
    arquivo.write("Telefone:..........{} \n".format(telefone))
    arquivo.write("Data:..............{} \n".format(data))
    arquivo.write("Horário:...........{} \n".format(hora))
    arquivo.close()
    
def gravar_pos():
    nome = str(caixa_nome.get())
    rg = str(caixa_rg.get())
    telefone = str(caixa_telefone.get())
    data = str(caixa_data.get())
    hora = str(caixa_hora.get())
    arquivo = open("pos-cirurgias.txt", "a")
    arquivo.write("Nome:..............{} \n".format(nome))
    arquivo.write("RG:................{}\n".format(rg))
    arquivo.write("Telefone:..........{} \n".format(telefone))
    arquivo.write("Data:..............{} \n".format(data))
    arquivo.write("Horário:...........{} \n".format(hora))
    arquivo.close()

def abrir_consulta():
    ramo = Tk()
    menubar = Menu(ramo)

    ramo.geometry("360x300")
    ramo.resizable(0,0)
    ramo.title("Consultas")
    
    E = Text(ramo)
    arquivo = open("consultas.txt", "r")
    texto = arquivo.read()
    E.insert(0.0,texto)
    E.pack()
    
    #arquivo = open("consultas.txt", "r")
    #texto = arquivo.read()
    #text = Label(ramo, text="{}".format(texto),bd='0', font=("arial", 12, "bold"), fg="#333333", cursor="hand2", justify="left")
    #text.place(x=10,y=15)
    #arquivo.close()
    
    ramo.mainloop()
    
def abrir_exame():
    ramo = Tk()
    menubar = Menu(ramo)

    ramo.geometry("360x300")
    ramo.resizable(0,0)
    ramo.title("Exames")
    
    E = Text(ramo)
    arquivo = open("exames.txt", "r")
    texto = arquivo.read()
    E.insert(0.0,texto)
    E.pack()
    
    #arquivo = open("exames.txt", "r")
    #texto = arquivo.read()
    #text = Label(ramo, text="{}".format(texto),bd='0', font=("arial", 12, "bold"), fg="#333333", cursor="hand2", justify="left")
    #text.place(x=10,y=15)
    #arquivo.close()
    
def abrir_cirurgias():
    ramo = Tk()
    menubar = Menu(ramo)

    ramo.geometry("360x300")
    ramo.resizable(0,0)
    ramo.title("Cirurgias")
    
    E = Text(ramo)
    arquivo = open("cirurgias.txt", "r")
    texto = arquivo.read()
    E.insert(0.0,texto)
    E.pack()
    
    #arquivo = open("cirurgias.txt", "r")
    #texto = arquivo.read()
    #text = Label(ramo, text="{}".format(texto),bd='0', font=("arial", 12, "bold"), fg="#333333", cursor="hand2", justify="left")
    #text.place(x=10,y=15)
    #arquivo.close()
    
def abrir_pos():
    ramo = Tk()
    menubar = Menu(ramo)

    ramo.geometry("360x300")
    ramo.resizable(0,0)
    ramo.title("Pós-cirurgias")
    
    E = Text(ramo)
    arquivo = open("pos-cirurgias.txt", "r")
    texto = arquivo.read()
    E.insert(0.0,texto)
    E.pack()
    
    #arquivo = open("pos-cirurgias.txt", "r")
    #texto = arquivo.read()
    #text = Label(ramo, text="{}".format(texto),bd='0', font=("arial", 12, "bold"), fg="#333333", cursor="hand2", justify="left")
    #text.place(x=10,y=15)
    #arquivo.close()
    


root = Tk()
menubar = Menu(root)

root.geometry("360x160")
root.resizable(0,0)
root.title("Cadastro")

savemenu = Menu(menubar, tearoff= 0)
savemenu.add_command(label="Consultas", command= gravar_consulta)
savemenu.add_command(label="Exames", command= gravar_exame)
savemenu.add_command(label="Cirurgias", command= gravar_cirurgia)
savemenu.add_command(label="Pós-cirurgias", command= gravar_pos)
menubar.add_cascade(label="Salvar", menu= savemenu)

openmenu = Menu(menubar, tearoff= 0)
openmenu.add_command(label="Consultas", command= abrir_consulta)
openmenu.add_command(label="Exames", command= abrir_exame)
openmenu.add_command(label="Cirurgias", command= abrir_cirurgias)
openmenu.add_command(label="Pós-cirurgias", command= abrir_pos)
menubar.add_cascade(label="Abrir", menu= openmenu)

root.config(menu=menubar)

#labels
text = Label(root, text="Insira o nome:",bd='0', font=("arial", 12, "bold"), fg="#333333", cursor="hand2")
text.place(x=10,y=15)
text = Label(root, text="Insira o RG:",bd='0', font=("arial", 12, "bold"), fg="#333333", cursor="hand2")
text.place(x=10,y=40)
text = Label(root, text="Insira o telefone:",bd='0', font=("arial", 12, "bold"), fg="#333333", cursor="hand2")
text.place(x=10,y=65)
text = Label(root, text="Insira a data:",bd='0', font=("arial", 12, "bold"), fg="#333333", cursor="hand2")
text.place(x=10,y=90)
text = Label(root, text="Insira o horário:",bd='0', font=("arial", 12, "bold"), fg="#333333", cursor="hand2")
text.place(x=10,y=115)

#caixas de entrada
caixa_nome = StringVar()
caixa_nomeBox = Entry(root, textvariable=caixa_nome)
caixa_nomeBox.place(x= 150, y=15, width=200, height=25)
caixa_rg = StringVar()
caixa_rgBox = Entry(root, textvariable=caixa_rg)
caixa_rgBox.place(x= 150, y=40, width=200, height=25)
caixa_telefone = StringVar()
caixa_telefoneBox = Entry(root, textvariable=caixa_telefone)
caixa_telefoneBox.place(x= 150, y=65, width=200, height=25)
caixa_data = StringVar()
caixa_dataBox = Entry(root, textvariable=caixa_data)
caixa_dataBox.place(x= 150, y=90, width=200, height=25)
caixa_hora = StringVar()
caixa_horaBox = Entry(root, textvariable=caixa_hora)
caixa_horaBox.place(x= 150, y=115, width=200, height=25)

root.mainloop()