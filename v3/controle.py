def validar_usuario(usuario, senha):
    if usuario=='admin' and senha=="1010":
        print("Correto")
        return True
    else:
        print("Incorreto")
        return False