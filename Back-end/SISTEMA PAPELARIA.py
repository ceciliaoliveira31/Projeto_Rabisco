#AULA 13 - SISTEMA PAPELARIA
import os
import mysql.connector #drive BD MySQL

#CONEXÃO COM BANCO DE DADOS
conexaoDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "senai",
    database = "Papelaria"
)

#FUNÇÃO PARA CADASTRAR PRODUTOS
def cadastrar_produto():
    imprimir_header() # cabeçalho
    print("*** CADASTRO DE PRODUTOS ***")
    nome = input("Informe o nome do produto: ")
    descricao = input("Digite a descrição: ")

    try:
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade:"))
    except ValueError:
        print("ERRO! Preço e quantidade devem ser valores numéricos.")
        return # retorna para o menu
    
    #VALIDAÇÃO
    if (not nome) or (not descricao) or (not preco) or (not quantidade):
        print("ERRO! Todos os campos devem sr preenchidos!")
        return # retorna para o menu
    
    if (preco < 0) or (quantidade < 0):
        print("ERRO! Preço e quantidade não pode ser menor que zero")
        return # retorna para o menu
    
    if len(nome) > 50:
        print("ERRO! O nome do produto é maior que 50 caracteres!")
        return # retorna para o menu

    comandoSQL = f'INSERT INTO Produto VALUES (null, "{nome}", "{descricao}", {preco}, {quantidade})'

    try:
        cursorDB = conexaoDB.cursor()
        cursorDB.execute(comandoSQL)
        conexaoDB.commit()
    except mysql.connector.Error as erro:
        print(f"ERRO! Falha ao cadastrar: {erro}")
        return
    
    print("*** OK! Cadastro realizado com sucesso!")
    cursorDB.close()


#FUNÇÃO PARA LISTAR OS PRODUTOS
def listar_produtos():
    imprimir_header()
    print("*** LISTA DE PRODUTOS ***")
    print("- "*50)

    try:
        cursorDB = conexaoDB.cursor()
        cursorDB.execute('SELECT * FROM Produto')
        resultados = cursorDB.fetchall()

        if not resultados:
            print("Não há produtos cadastrados!")
        else:
            for produto in resultados:
                print(f"ID: {produto[0]} - NOME: {produto[1]} - DESCRIÇÃO: {produto[2]} - PREÇO: {produto[3]} - QUANT: {produto[4]}")
                print("- "*50)
    except mysql.connector.Error as erro:
        print(f"ERRO! Falha ao listar: {erro}")
    cursorDB.close()


#FUNÇÃO BUSCA PRODUTO
def get_produto(id_produto):
    cursorDB = conexaoDB.cursor()
    comandoSQL = f'SELECT * FROM Produto WHERE idProduto = {id_produto}'
    cursorDB.execute(comandoSQL)
    resultado = cursorDB.fetchone() # vai pegar um valor só numa lista só
    cursorDB.close()
    return resultado

#FUNÇÃO PARA ALTERAR PREÇO
def altera_preco():
    imprimir_header()
    print("*** ALTERAR QUANTIDADE ***")
    try:
        id_produto = int(input("Informe o ID do produto: "))
    except ValueError:
        print("ERRO! ID deve ser numérico!")
        return
    
    produto = get_produto(id_produto)

    if not produto:
        print("Produto com o ID {id_produto} não encontrado!")
        return
    
    print("Produto encontrado!")
    print(f"ID: {produto[0]} - NOME: {produto[1]} - PREÇO: {produto[3]}")

    try:
        novo_preco = float(input("Informe o novo preço: "))
    except ValueError:
        print("ERRO! Valor do preço deve ser decimal!")
        return
    
    if novo_preco == produto[3]:
        print("O preço informado é igual ao preço anterior!")
        return
    
    if novo_preco < 0:
        print("O preço não pode ser negativo")
        return
    
    try:
        comandoSQL = f'UPDATE Produto SET preco = {novo_preco} WHERE idProduto = {id_produto}'
        cursorDB = conexaoDB.cursor()
        cursorDB.execute(comandoSQL)
        conexaoDB.commit()
    except mysql.connector.Error as erro:
        print(f'ERRO! Falha na atualização: {erro}')

    print("OK! Atualização realizada com sucesso!")
    cursorDB.close()


#FUNÇÃO PARA ALTERAR A QUANTIDADES 
def altera_quantidade():
    imprimir_header()
    print("*** ALTERAR QUANTIDADE ***")
    try:
        id_produto = int(input("Informe o ID do produto: "))
    except ValueError:
        print("ERRO! ID deve ser numérico!")
        return
    
    produto = get_produto(id_produto)

    if not produto:
        print("Produto com o ID {id_produto} não encontrado!")
        return
    
    print("Produto encontrado!")
    print(f"ID: {produto[0]} - NOME: {produto[1]} - QUANTIDADE{produto[4]}")

    try:
        nova_quantidade = int(input("Informe a nova quantidade: "))
    except ValueError:
        print("ERRO! Valor da quantidade deve ser número inteiro!")
        return
    
    if nova_quantidade == produto[4]:
        print("A quantidade informada é igual a quantidade anterior?")
        return
    
    if nova_quantidade < 0 or nova_quantidade > 10000:
        print("A quantidade é inválida")
        return
    
    try:
        comandoSQL = f'UPDATE Produto SET quantidade = {nova_quantidade} WHERE idProduto = {id_produto}'
        cursorDB = conexaoDB.cursor()
        cursorDB.execute(comandoSQL)
        conexaoDB.commit()
    except mysql.connector.Error as erro:
        print(f'ERRO! Falha na atualização: {erro}')

    print("OK! Atualização realizada com sucesso!")
    cursorDB.close()
    


#FUNÇÃO EXCLUIR PRODUTO
def excluir_produto():
    imprimir_header()
    print("*** EXCLUIR PRODUTO ***")
    try:
        id_produto = int(input("Informe o ID do produto: "))
    except ValueError:
        print("ERRO! ID deve ser numérico!")
        return
    
    produto = get_produto(id_produto)

    if not produto:
        print("Produto com o ID {id_produto} não encontrado!")
        return
    
    print("Produto encontrado!")
    print(f"ID: {produto[0]} - NOME: {produto[1]}")

    confirma = input("Digite S para confirmar a exclusão: ")
    if confirma != 'S' and confirma != "s":
        print("Exclusão cancelada!")
        return
    
    try:
        cursorDB = conexaoDB.cursor()
        comandoSQL = f'DELETE FROM Produto WHERE idProduto = {id_produto}'
        cursorDB.execute(comandoSQL)
        conexaoDB.commit()
    except mysql.connector.Error as erro:
        print(f'ERRO! Falha na exclusão: {erro}')
        return
    
    print("OK! Exclusão realizadacom sucesso!")
    cursorDB.close()

def imprimir_header():
    os.system('cls')
    print("- " * 20)
    print("*** SISTEMA PAPELARIA ***")
    print("- " * 20)


#Programa principal - menu
while True:
    imprimir_header()
    print("MENU - Informe a opção desejada: ")
    print("1 - Cadastrar produto")
    print("2 - Alterar quantidade")
    print("3 - Alterar preço")
    print("4 - Mostrar todos os produtos")
    print("5 - Excluir um produto")
    print("6 - Sair")
    opcao = input("Informe a opção desejada: ")
    if opcao == '1':
        cadastrar_produto()
    elif opcao == '2':
        altera_quantidade()
    elif opcao == '3':
        altera_preco()
    elif opcao == '4':
        listar_produtos()
    elif opcao == '5':
        excluir_produto()
    elif opcao == '6':
        break
    else:
        print("Opção INVÁLIDA")


    os.system('pause')

print("SISTEMA ERRADO")
conexaoDB.close()