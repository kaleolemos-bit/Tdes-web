import tkinter as tk
import random

#1
'''
def convercao():
    valor = float(entrada.get())
    tipo = opcao.get()

    if tipo == 'C - F':
        resultado.config(text=f'{valor} C = {round(valor * 9 / 5 + 32, 2)} F')
    elif tipo == 'F - C':
        resultado.config(text=f'{valor} F = {round(valor - 32 * 5 / 9, 2)} C')
    elif tipo == 'KM - MIL':
        resultado.config(text=f'{valor} KM = {round(valor * 0.62, 2)} MIL')
    elif tipo == 'MIL - KM':
        resultado.config(text=f'{valor} MIL = {round(valor / 0.62, 2)} KM')
    elif tipo == 'KG - LB':
        resultado.config(text=f'{valor} KG = {round(valor * 2.2, 2)} LB')
    elif tipo == 'LB - KG':
        resultado.config(text=f'{valor} LB = {round(valor / 2.2, 2)} KG')

    janela = tk.TK()
    janela.title('Conversor de unidades')
    janela.geometry('600x400')

    tk.Label(janela, text='Conversor de unidades', font='Verdana 14 bold').pack(pady=10)

    tk.Label(janela, text='Digite um valor: ').pack()
    entrada = tk.Entry(janela)
    entrada.pack()

    opcao = tk.StringVar()
    opcao.set('C - F')

    tk.Radiobutton(janela, text='Celsius para Fharenheit', value = 'C - F', variable = opcao).pack()
    tk.Radiobutton(janela, text='Fharenheit para Celsius', value='F-C', variable = opcao).pack()
    tk.Radiobutton(janela, text='Km para Milhas', value='KM - MI', variable = opcao).pack()
    tk.Radiobutton(janela, text='Milhas para Km', value='MI - KM', variable = opcao).pack()
    tk.Radiobutton(janela, text='Kg para Libras', value='KG - LB', variable = opcao).pack()
    tk.Radiobutton(janela, text='Libras para Kg', value='LB - KG', variable = opcao).pack()

    tk.Button(janela, text='Converter', font='Verdana 10 bold',fg='white', command=convercao).pack(pady=10)

    resultado = tk.label(janela, text='Resultado: ', font='Verdana 12 bold')
    resultado.pack()

    janela.mainloop()
'''
 
#2
'''
def gerar():
    tamanho = escala.get()
 
    caracteres = 'abcdefghijklmnopqrstuvwxyz'
 
    if maiusculas_var.get():
        caracteres = caracteres + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if numeros_var.get():
        caracteres = caracteres + '0123456789'
    if simbolos_var.get():
        caracteres = caracteres + '!@#$%&*?'
 
    senha = ''
    for n in range(tamanho):
        senha = senha + random.choice(caracteres)
 
    senha_atual.set(senha)
    resultado.config(text=senha)
 
def copiar():
    janela.clipboard_clear()
    janela.clipboard_append(senha_atual.get())
    aviso.config(text='Senha copiada!')
 
janela = tk.Tk()
janela.title('Gerador de Senhas')
janela.geometry('600x400')
 
tk.Label(janela, text='Gerador de Senhas', font='Verdana 14 bold').pack(pady=10)
 
tk.Label(janela, text='Tamanho da senha:').pack()
escala = tk.Scale(janela, from_=4, to=32, orient=tk.HORIZONTAL, length=250)
escala.set(12)
escala.pack()
 
maiusculas_var = tk.IntVar()
numeros_var = tk.IntVar()
simbolos_var = tk.IntVar()
 
tk.Checkbutton(janela, text='Incluir maiúsculas', variable=maiusculas_var).pack()
tk.Checkbutton(janela, text='Incluir números', variable=numeros_var).pack()
tk.Checkbutton(janela, text='Incluir símbolos', variable=simbolos_var).pack()
tk.Button(janela, text='Gerar senha', font='Verdana 10 bold', fg='white', bg='#4CAF50',
          command=gerar).pack(pady=10)
 
senha_atual = tk.StringVar()
resultado = tk.Label(janela, text='', font='Courier 14 bold')
resultado.pack()
tk.Button(janela, text='Copiar senha', command=copiar).pack(pady=5)
aviso = tk.Label(janela, text='')
aviso.pack()
 
janela.mainloop()
'''
#3
'''
def contar():
    if rodando.get() == 1:
        segundos.set(segundos.get() + 1)

        total = segundos.get()
        horas = total // 3600
        minutos = (total % 3600) // 60
        seg = total % 60
        tempo.config(text=f'{horas:02d}:{minutos:02d}:{seg:02d}')

    janela.after(1000, contar)

def iniciar():
    rodando.set(1)

def pausar():
    rodando.set(0)

def resetar():
    rodando.set(0)
    segundos.set(0)
    tempo.config(text='00:00:00')

janela = tk.Tk()
janela.title('Cronômetro')
janela.geometry('600x400')
segundos = tk.IntVar()
rodando = tk.IntVar()
tempo = tk.Label(janela, text='00:00:00', font='Courier 40 bold')
tempo.pack(pady=40)
tk.Button(janela, text='Iniciar', width=10, font='Verdana 10 bold', fg='white', bg='#4CAF50',
          command=iniciar).pack(pady=3)
tk.Button(janela, text='Pausar', width=10, font='Verdana 10 bold', bg='orange',
          command=pausar).pack(pady=3)
tk.Button(janela, text='Resetar', width=10, font='Verdana 10 bold', fg='white', bg='red',
          command=resetar).pack(pady=3)

contar()
janela.mainloop()
'''
#4
'''
def contar():
    if rodando.get() == 1:
        segundos.set(segundos.get() + 1)

        total = segundos.get()
        horas = total // 3600
        minutos = (total % 3600) // 60
        seg = total % 60
        tempo.config(text=f'{horas:02d}:{minutos:02d}:{seg:02d}')

    janela.after(1000, contar)

def iniciar():
    rodando.set(1)

def pausar():
    rodando.set(0)

def resetar():
    rodando.set(0)
    segundos.set(0)
    tempo.config(text='00:00:00')

janela = tk.Tk()
janela.title('Cronômetro')
janela.geometry('600x400')
segundos = tk.IntVar()
rodando = tk.IntVar()
tempo = tk.Label(janela, text='00:00:00', font='Courier 40 bold')
tempo.pack(pady=40)
tk.Button(janela, text='Iniciar', width=10, font='Verdana 10 bold', fg='white', bg='#4CAF50',
          command=iniciar).pack(pady=3)
tk.Button(janela, text='Pausar', width=10, font='Verdana 10 bold', bg='orange',
          command=pausar).pack(pady=3)
tk.Button(janela, text='Resetar', width=10, font='Verdana 10 bold', fg='white', bg='red',
          command=resetar).pack(pady=3)

contar()
janela.mainloop()
'''
#5

votos = [0, 0, 0]

def mostrar():
    label_ana.config(text=f'Ana: {votos[0]} votos')
    label_bruno.config(text=f'Bruno: {votos[1]} votos')
    label_carla.config(text=f'Carla: {votos[2]} votos')
    label_total.config(text=f'Total de votos: {votos[0] + votos[1] + votos[2]}')

def votar_ana():
    votos[0] = votos[0] + 1
    mostrar()

def votar_bruno():
    votos[1] = votos[1] + 1
    mostrar()

def votar_carla():
    votos[2] = votos[2] + 1
    mostrar()

def vencedor():
    maior = max(votos)

    if maior == 0:
        label_vencedor.config(text='Nenhum voto ainda')
    elif votos.count(maior) > 1:
        label_vencedor.config(text='Deu empate!')
    elif votos[0] == maior:
        label_vencedor.config(text='Vencedor: Ana')
    elif votos[1] == maior:
        label_vencedor.config(text='Vencedor: Bruno')
    else:
        label_vencedor.config(text='Vencedor: Carla')

def resetar():
    votos[0] = 0
    votos[1] = 0
    votos[2] = 0
    label_vencedor.config(text='')
    mostrar()

janela = tk.Tk()
janela.title('Votação')
janela.geometry('600x400')
tk.Label(janela, text='Sistema de Votação', font='Verdana 14 bold').pack(pady=10)
tk.Button(janela, text='Votar em Ana', width=20, command=votar_ana).pack(pady=3)
tk.Button(janela, text='Votar em Bruno', width=20, command=votar_bruno).pack(pady=3)
tk.Button(janela, text='Votar em Carla', width=20, command=votar_carla).pack(pady=3)
label_ana = tk.Label(janela, text='Ana: 0 votos')
label_ana.pack()
label_bruno = tk.Label(janela, text='Bruno: 0 votos')
label_bruno.pack()
label_carla = tk.Label(janela, text='Carla: 0 votos')
label_carla.pack()
label_total = tk.Label(janela, text='Total de votos: 0', font='Verdana 10 bold')
label_total.pack(pady=5)
tk.Button(janela, text='Mostrar vencedor', width=20, fg='white', bg='#4CAF50',
          command=vencedor).pack(pady=3)
tk.Button(janela, text='Resetar votação', width=20, fg='white', bg='red',
          command=resetar).pack(pady=3)

label_vencedor = tk.Label(janela, text='', font='Verdana 12 bold', fg='blue')
label_vencedor.pack()

janela.mainloop()