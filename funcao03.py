dict_alunos = {
    'nome_aluno' : 'bruno fabro',
    'email_aluno ' : 'bruno12@gmail.com',
    'serie_aluno' : '2TB'
}

def mostrar_dados_dicionario(aluno):
    for i in aluno.values():
        print(i)

mostrar_dados_dicionario(dict_alunos)

def mostrar_dados():
    dict_alunos = {
        'nome_aluno' : 'bruno',
        'email_aluno ' : 'brunolourencone12@gmail.com',
        'serie_aluno' : '2TB'
    }

    for aluno in dict_alunos.values():
        print(aluno)


mostrar_dados()

