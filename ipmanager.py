from socket import AF_INET, socket, SOCK_STREAM

HOST = ''  
PORT = 33000      
if __name__ == "__main__":
    print("Aguardando conexão...")
with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    conn, addr = s.accept()
    print("%s:%s has connected." % addr)
    while True:
        data = conn.recv(1024)
        arqui = open("Recebido.txt", "wb")
        arqui.write(data)
        arqui.close
        print(data)
        arqui = open('Recebido.txt', 'r')
        Alfabeto = "CZDFAGMSTNVXPQLEUHKYBORWIJ "
        crip = 0
        descrip = ""
        modo = "D"
        chave = 3
        mensagem = arqui.read()
        for caractere in mensagem:
            if caractere in Alfabeto:
                crip = Alfabeto.find(caractere)
            if modo == "D" or "d":
                crip = (crip - chave) % len(Alfabeto)
            if crip > len(Alfabeto):
                crip = crip-len(Alfabeto)
            elif crip < 0:
                crip = crip + len(Alfabeto)
            descrip = descrip + Alfabeto[crip]
        else:     
            print(descrip)
            arqui.close()
            arqui = open("descriptografado.txt", "w")
            arqui.write(descrip)
            arqui.close()
        if not data:
            break
        conn.sendall(data)