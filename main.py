from utils import validar_nome, validar_idade
from functions import criar_cadastro

print('\n === Cadastro Simples === ')
nome = None
while nome is None:
    nome = validar_nome(input('Digite o seu nome: '))
    if nome is None:
        print('\nNome inválido.')

idade = None
while idade is None:
    idade = validar_idade(input('\nDigite sua idade: '))
    if idade is None:
        print('\nIdade inválida.')

usuario = criar_cadastro(nome, idade)

print('\nCadastro criado com sucesso!')
print(usuario)
