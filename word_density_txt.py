import sys
from collections import Counter
import string

def remove_punctuation(text):
    all_punctuation = string.punctuation + "“”‘’—-—"  # Adicione qualquer pontuação extra aqui
    translator = str.maketrans('', '', all_punctuation)
    return text.translate(translator).lower()

def calculate_word_count(filepath, exclude_words):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()

        # Aplicar a remoção de pontuação e converter para minúsculas
        text = remove_punctuation(text)
    
        # Dividir o texto em palavras
        words = text.split()

        # Contar a frequência de cada palavra
        word_count = Counter(words)

        # Remover palavras que estão na lista de exclusão
        for word in exclude_words:
            word_count.pop(word, None)

        # Calcular o total de palavras após a exclusão
        total_words = sum(word_count.values())
        
        # Calcular o número de palavras únicas
        unique_words = len(word_count)

        return word_count, total_words, unique_words
    except FileNotFoundError:
        print("O arquivo não foi encontrado. Por favor, verifique o caminho.")
        return {}, 0
    except Exception as e:
        print(f"Erro ao processar o arquivo: {str(e)}")
        return {}, 0

def print_word_count(word_count, total_words, unique_words, topdown):
    if word_count:
        print("Contagem de palavras no documento:")
        for word, count in sorted(word_count.items(), key=lambda item: item[1], reverse=topdown):
            percentage = count/total_words*100
            count = str(count)
            print(f"{count.ljust(4)}  {word.ljust(17)}{percentage:.2f}%")
        formatado = "{:,}".format(total_words).replace(',', '.')
        unique_formatado = "{:,}".format(unique_words).replace(',', '.')
        print("--------------------------------------------------------------------")
        print(f"Total de palavras relevantes:\t{formatado}\t(já excluídas as stopwords)")
        print(f"Total de palavras únicas: \t{unique_formatado}\t(já excluídas as stopwords)")
        print("--------------------------------------------------------------------")
    else:
        print("Nenhum dado para exibir.")

def main():
    filepath = input("Por favor, insira o caminho completo do arquivo de texto: ")
    print()
    print("Ordenação")
    escolha = int(input("[1] crescente | [2] decrescente: "))
    if escolha == 2:
        topdown = True
    elif escolha == 1:
        topdown = False

    exclude_words = ['e', 'é', 'me', '-', '—', 'o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas', 'de', 'da', 'do', 'das', 'dos', 'em', 'no', 'na', 'nos', 'nas', 'que', 'não', 'se', 'para', 'com', 'como', 'por', 'ao', 'aos', 'às', 'à']
    word_count, total_words, unique_words = calculate_word_count(filepath, exclude_words)
    print_word_count(word_count, total_words, unique_words, topdown)

if __name__ == "__main__":
    main()
