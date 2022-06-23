import csv

def criaCsv(lista1: list, lista2: list, tamanho: int) -> bool:
    file = open('csv-result.csv', 'w', newline='', encoding='utf-8') # abre o arquivo

    fileCsv = csv.writer(file) # habilita o csv a ser escrito

    for i in range(tamanho):
        fileCsv.writerow([lista1[i], lista2[i]]) # imprime cada elemento da lista em uma linha do csv
    
    file.close()

    return True