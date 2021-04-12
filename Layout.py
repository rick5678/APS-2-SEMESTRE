import tkinter as tk
from socket import AF_INET, socket, SOCK_STREAM
from datetime import datetime
n = datetime.now()
h = str(n.hour)+":"+str(n.minute)+":"+str(n.second)+":"
arqui = open("descriptografado.txt", "r")
arqui.read()
decifrado = arqui.read()
arqui.close()
def name():
    usuario = nome.get()
    arq = open('usuario.txt', 'w')
    arq.write(usuario)
    arq.close()
    root.quit()
def Receber():
    arqui = open("descriptografado.txt", "r")
    Decifrado = arqui.read()
    arqui.close()
    MensagemADM = h + " ADM: " + Decifrado
    chat.insert(tk.END, MensagemADM)
def send():
    Mensagem_enviada = mensagem.get("1.0",'end-1c')
    arquivo =open("usuario.txt", "r")
    Mensagem_final = h + arquivo.read() + ": "+ Mensagem_enviada 
    chat.insert(tk.END,Mensagem_final)
    mensagem.delete("1.0",'end-1c')
    Alfabeto = "CZDFAGMSTNVXPQLEUHKYBORWIJ "
    cripti = ""
    modo = "E"
    chave = 3
    crip = 0
    Mensagem_enviada = Mensagem_enviada.upper()
    for caractere in Mensagem_enviada:
        if caractere in Alfabeto:
         crip = Alfabeto.find(caractere)
        if modo == "E" or "e":
         crip = (crip + chave) % len(Alfabeto)
        if crip> len(Alfabeto):
         crip = crip-len(Alfabeto)
        elif crip < 0:
         crip = crip + len(Alfabeto)   
        cripti = cripti + Alfabeto[crip] 
    else: 
        print(cripti)
        arqui = open("criptografado.txt", "w")
        arqui.write(cripti)
        arqui.close()
    client_socket.send(cripti.encode('utf-8'))
HOST = input('Enter host: ')
PORT = 33000
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)
BUFSIZ = 1024
ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
root = tk.Tk()
root.title("Login Cliente")
root.geometry("+200+200")
canvas = tk.Canvas(root, height=300, width=400)#command=IP
canvas.pack()
top_frame = tk.Frame(root)
top_frame.place(relwidth=1, relheight=1)
label = tk.Label(top_frame, font="Bold 10", text="Digite seu nome:")
label.place(rely=0.3, relx=0.3)
nome = tk.StringVar()
nome = tk.Entry(top_frame)
nome.place(rely=0.4, relx=0.3)
proximo = tk.Button(top_frame, text="Próximo", command=name)
proximo.place(rely=0.5, relx=0.4)
root.mainloop()
janela = tk.Tk()
frame = tk.Frame(janela)
frame.place(relwidth=0.7, relheight=0.6, relx=0.15, rely=0.1)  
mensagem = tk.StringVar()
rolagem = tk.Scrollbar(frame)
rolagem.pack(side=tk.RIGHT, fill=tk.Y)
chat = tk.Listbox(frame, yscrollcommand=rolagem.set)
chat.place(relwidth=0.97 , relheight=1 )
mensagem = tk.Text(janela)
mensagem.place(relx=0.15 , rely=0.71, relwidth=0.679, relheight=0.15)
enviar = tk.Button(janela, text="Enviar", command=send)
enviar.place(relx=0.68, rely=0.86, relwidth=0.15)
conectar = tk.Button(janela, text="Receber", command=Receber)
conectar.place(relx=0.619, rely=0.86)
janela.geometry("800x600+100+100")
janela.title("Chat Cliente")
janela.mainloop()