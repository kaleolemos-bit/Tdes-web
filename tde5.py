import tkinter as tk
'''conversor
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