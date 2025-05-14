def info_ficha(nome, cpf, rg, data_nasci, endereco, cidade, estado, telefone, email):
    ficha = {
        'nome': nome,
        'cpf': cpf,
        'rg': rg,
        'data de nascimento': data_nasci,
        'endereco': endereco,
        'cidade': cidade,
        'estado': estado,
        'telefone': telefone,
        'email': email
    }
    
    return ficha

def preenchi_ficha():
    nome = input("Digite o seu nome: ")
    cpf = int(input("Digite o seu cpf: "))
    rg = int(input("Digite o seu rg: "))
    data_nasci = int(input("Digite a sua data de nascimento: "))
    endereco = input("Digite o seu endereco: ")
    cidade = input("Digite a sua cidade: ")
    estado = input("Digite o seu estado: ")
    telefone = int(input("Digite seu numero de telefone: "))
    email = input("Digite o seu email: ")

    return info_ficha(nome, cpf, rg, data_nasci, endereco, cidade, estado, telefone, email)

def exibir_ficha(ficha):
    print('--------sua ficha de cadastro:--------')
    for chave, valor in ficha.items():
        print(f"{chave}: {valor}")
    print('-------ficha exibida com sucesso!--------')

def main():
    ficha = preenchi_ficha()
    exibir_ficha(ficha)

print('--------preencha sua ficha aqui em baixo:--------')

main()
