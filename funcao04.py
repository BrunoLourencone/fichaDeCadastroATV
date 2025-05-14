
alunos = []

def dados_pessoais():
    nome = input('digite o seu nome completo: ')
    email = input('digite seu email: ')
    serie = input('qual a sua serie escolar?: ')

    dados_aluno = {
        'nome' : nome,
        'email' : email,
        'serie' : serie
    }
    return dados_aluno

print(dados_pessoais())

def cadastro(aluno):
    return print(aluno)

cadastro(dados_pessoais())


