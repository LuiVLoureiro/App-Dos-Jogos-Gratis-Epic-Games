from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image
import tkinter as tk

# Função para mostrar uma janela Tkinter com tema escuro
def mostrar_janela(icon, item):
    if not mostrar_janela.janela:
        # Cria a janela
        mostrar_janela.janela = tk.Tk()
        mostrar_janela.janela.title("Janela Tkinter")
        
        # Aplica o tema escuro
        mostrar_janela.janela.configure(bg='#333333')
        
        # Cria um label com texto branco e fundo escuro
        label = tk.Label(mostrar_janela.janela, text="Olá, mundo Tkinter!",
                         fg='white', bg='#333333')
        label.pack()
        
        # Define uma ação para quando a janela for fechada
        mostrar_janela.janela.protocol("WM_DELETE_WINDOW", fechar_janela)
        mostrar_janela.janela.mainloop()
    else:
        mostrar_janela.janela.focus()

mostrar_janela.janela = None

# Função para fechar a janela Tkinter
def fechar_janela():
    mostrar_janela.janela.destroy()
    mostrar_janela.janela = None

# Função para fechar o ícone da bandeja e terminar o programa
def sair(icon, item):
    icon.stop()
    if mostrar_janela.janela:
        mostrar_janela.janela.destroy()

# Carrega uma imagem para o ícone da bandeja (ajuste o caminho conforme necessário)
image = Image.open(r'C:\Users\luipo\Desktop\Projeto_Jogos_Gratis_Epic_Games\app\icone.png')  # Certifique-se de substituir 'seu_icone_aqui.png'

# Cria o ícone da bandeja com um menu
icone = icon('test', image, menu=menu(
    item('Abrir Janela', mostrar_janela),
    item('Sair', sair)
))

# Roda o ícone da bandeja
icone.run()
