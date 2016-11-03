import csv


# Processa os resultados e gera um arquivo .csv
def gerar_csv(arquivo, nomes_campos, dados):
    try:
        with open(arquivo, 'w') as arquivoCSV:
            gerador = csv.DictWriter(
                arquivoCSV, fieldnames=nomes_campos)

            gerador.writeheader()
            for dado in dados:
                gerador.writerow(dado)
    except Exception as e:
        raise e
