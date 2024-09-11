# Método de Busca Escrever
with open("text2.txt", "w", encoding="utf-8") as arquivo:
    conteudo = arquivo.write("Olá, mundo")

    # Método de Busca Acrescentar a
    with open("text.txt", "a", encoding ="utf-8" ) as arquivo:
        arquivo.write('\nmacarrao')