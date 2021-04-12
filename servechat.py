import tkinter as tk
from socket import AF_INET, socket, SOCK_STREAM
from datetime import datetime
n = datetime.now()
h = str(n.hour)+":"+str(n.minute)+":"+str(n.second)+":"
arqui = open("descriptografado.txt", "r")
arqui.read()
decifrado = arqui.read()
arqui.close()
def pegar():
    login = ed1.get()
    senha = ed2.get()
    if(login == "ADM" and senha == "123"):
        janela.quit()
    else:
        lbl3 = tk.Label(janela, text="Login ou Senha inválido", foreground='red')
        lbl3.place(relx = 0.38, rely = 0.10)
def Receber():
    arqui = open("descriptografado.txt", "r")
    Decifrado = arqui.read()
    arqui.close()
    MensagemClient = h + "Client: " + Decifrado
    chat.insert(tk.END, MensagemClient)
def send():
    Mensagem_enviada = mensagem.get("1.0",'end-1c')
    Mensagem_final = h + "ADM" + ": "+ Mensagem_enviada 
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
janela = tk.Tk()
lbl1 = tk.Label(janela, text="Login: ")
lbl2 = tk.Label(janela, text="Senha: ")
ed1 = tk.Entry(janela,)
ed2 = tk.Entry(janela, show='*')
bt1 = tk.Button(janela, text="Confirmar",command=pegar)
lbl1.place(relx = 0.25, rely = 0.25)
lbl2.place(relx = 0.25, rely = 0.38)
ed1.place(relx = 0.38, rely = 0.25)
ed2.place(relx = 0.38, rely = 0.38)
bt1.place(relx = 0.45, rely = 0.50)
janela.title("Login")
janela.geometry("400x200+200+200")
janela.mainloop()
janela2 = tk.Tk()
frame = tk.Frame(janela2)
frame.place(relwidth=0.7, relheight=0.6, relx=0.15, rely=0.1)  
mensagem = tk.StringVar()
rolagem = tk.Scrollbar(frame)
rolagem.pack(side=tk.RIGHT, fill=tk.Y)
chat = tk.Listbox(frame, yscrollcommand=rolagem.set)
chat.place(relwidth=0.97 , relheight=1 )
mensagem = tk.Text(janela2)
mensagem.place(relx=0.15 , rely=0.71, relwidth=0.679, relheight=0.15)
enviar = tk.Button(janela2, text="Enviar", command=send)
enviar.place(relx=0.68, rely=0.86, relwidth=0.15)
conectar = tk.Button(janela2, text="Receber", command=Receber)
conectar.place(relx=0.619, rely=0.86)
janela2.geometry("800x600+100+100")
janela2.title("Chat - Manager")
janela2.mainloop()