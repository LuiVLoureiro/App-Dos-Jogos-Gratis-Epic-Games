from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image
import tkinter as tk

# Função para mostrar uma janela Tkinter
def mostrar_janela(icon, item):
    if not mostrar_janela.janela:
        mostrar_janela.janela = tk.Tk()
        mostrar_janela.janela.title("Dev Lui")
        mostrar_janela.janela.configure(bg='#333333')
        mostrar_janela.janela.overrideredirect(True)
        canvas = tk.Canvas(mostrar_janela.janela, width=300, height=1)
        

        # Configura o tamanho da janela
        largura_janela = 250
        altura_janela = 400
        mostrar_janela.janela.geometry(f'{largura_janela}x{altura_janela}')

        # Calcula posição para a janela abrir no canto inferior direito
        largura_tela = mostrar_janela.janela.winfo_screenwidth()
        altura_tela = mostrar_janela.janela.winfo_screenheight()
        x_posicao = largura_tela - largura_janela
        y_posicao = altura_tela - altura_janela
        mostrar_janela.janela.geometry(f'+{x_posicao - 50}+{y_posicao - 70}')

        label = tk.Label(mostrar_janela.janela, text="JOGOS GRATIS EPIC GAMES", bg='#333333', font='impact', fg='#ffffff', pady='30')
        
        label.pack()
        canvas.create_line(1, 1, 1, 1, fill='white')
        canvas.pack()

        # Define uma ação para quando a janela for fechada
        mostrar_janela.janela.protocol("WM_DELETE_WINDOW", fechar_janela)
        mostrar_janela.janela.mainloop()
    else:
        # Se a janela já está criada, traz para o foco
        mostrar_janela.janela.focus()

# Inicializa o atributo da função como None
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
image = Image.open(r'C:\Users\luipo\Desktop\Projeto_Jogos_Gratis_Epic_Games\app\icone.png')

# Cria o ícone da bandeja com um menu
icone = icon('test', image, menu=menu(
    item('Abrir Janela', mostrar_janela),
    item('Fechar Janela', fechar_janela),
    item('Sair', sair)
))

# Roda o ícone da bandeja
icone.run()
