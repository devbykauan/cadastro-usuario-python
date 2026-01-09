def validar_nome(nome):
    nome = nome.strip()
    if nome == '':
        return None
    return None

def validar_idade(texto):
    try:
        idade = int(texto)
        if idade < 0 or idade > 100:
            return None
        return idade
    except ValueError:
        return None


