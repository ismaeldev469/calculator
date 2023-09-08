import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")

display = tk.Entry(janela, width=20)
display.grid(row=0, column=0, columnspan=4)



def clique_botao(numero):
    conteudo_atual = display.get()
    novo_conteudo = conteudo_atual + numero
    display.delete(0, tk.END)
    display.insert(0, novo_conteudo)

def clique_operador(operador):
    expressao = display.get()

    try:
        resultado = str(eval(expressao))
        display.delete(0, tk.END)
        display.insert(0, resultado)
    except:
        display.delete(0, tk.END)

def limpar():
    display.delete(0, tk.END)

botoes = ['7', '8', '9', '/',
          '4', '5', '6', '*',
          '1', '2', '3', '-',
          '0', '.', '=', '+',
          'C'
]

row = 1
col = 0

for botao in botoes:
    if botao == '=':
        tk.Button(janela, text=botao, padx=20, pady=20, command=lambda: clique_operador(botao)).grid(row=row,
                                                                                                     column=col)
    elif botao == 'C':
        tk.Button(janela, text=botao, padx=20, pady=20, command=limpar).grid(row=row, column=col)
    else:
        tk.Button(janela, text=botao, padx=20, pady=20, command=lambda num=botao: clique_botao(num)).grid(row=row,
                                                                                                          column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

janela.mainloop()