# Importando tkinter (biblioteca de interface gráfica que permite criar aplicativos com uma interface visual)
from tkinter import * 
from tkinter import ttk 

# CORES
cor1 = "#2f302f" # Preto
cor2 = "#feffff" # Branca
cor3 = "#38576b" # Azul
cor4 = "#ECEFF1" # Cinza
cor5 = "#FFAB40" # Laranja

# Função para centralizar o texto nos botões
def centralizar_texto(botao):
    botao.config(justify=CENTER, anchor="center")

# Criando a janela principal
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.configure(bg=cor1)

# Adicionar transparência
janela.attributes('-alpha', 0.8)  # Ajuste o valor para a transparência desejada (0.0 a 1.0)

# Criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_botoes = Frame(janela, width=235, height=268)
frame_botoes.grid(row=1, column=0)

# Variável para armazenar todos os valores
todos_valores = ''

# Lista de operadores válidos
operadores = ['+', '-', '*', '/', '%']

# Função para calcular
def calcular():
    global todos_valores
    try:
        resultado = eval(todos_valores)
        
        # Verifica se o resultado é um número inteiro e converte para int se for
        if isinstance(resultado, float) and resultado.is_integer():
            resultado = int(resultado)
        
        # Formata o resultado para exibir sem a parte decimal ".0" se for um número float
        if isinstance(resultado, float):
            resultado_str = "{:.0f}".format(resultado)
        else:
            resultado_str = str(resultado)
        
        # Define o texto do valor a ser exibido
        valor_texto.set(resultado_str)
        
        # Atualiza todos_valores para o resultado atual, para permitir a continuidade da operação
        todos_valores = resultado_str
        
    except Exception as e:
        valor_texto.set("Erro")
        todos_valores = ''

        
# Limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# Função para entrar valores
def entrar_valores(event):
    global todos_valores
    
    # Verifica se é um número, ponto decimal ou operador
    if event.isdigit() or event == '.':
        # Se o resultado anterior for exibido, limpa para inserir novo número
        if valor_texto.get() == 'Erro':
            limpar_tela()
        
        # Adiciona número ou ponto à expressão
        todos_valores += str(event)
        
    elif event in operadores:
        # Verifica se já há um operador no final de todos_valores
        if todos_valores and todos_valores[-1] in operadores:
            # Substitui o operador anterior pelo novo operador clicado
            todos_valores = todos_valores[:-1] + event
        elif todos_valores:
            # Se houver um resultado anterior, usa o resultado como primeiro operando
            try:
                resultado = eval(todos_valores)
                todos_valores = str(resultado) + event
            except:
                valor_texto.set("Erro")
                todos_valores = ''
        else:
            # Ignora a adição de operador se não houver números antes
            return
    
    valor_texto.set(todos_valores)



# Criando Label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 13'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

# Criando botões
b_1 = Button(frame_botoes, command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_botoes, command=lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_botoes, command=lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_botoes, command=lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_botoes, command=lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_botoes, command=lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_botoes, command=lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button(frame_botoes, command=lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_botoes, command=lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_botoes, command=lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_botoes, command=lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(frame_botoes, command=lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_botoes, command=lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_botoes, command=lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_botoes, command=lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_16 = Button(frame_botoes, command=lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_botoes, command=lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(frame_botoes, command=calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)

janela.mainloop()