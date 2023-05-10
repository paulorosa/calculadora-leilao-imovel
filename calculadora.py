import json
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def read_input_file(input_filename):
    f = open(input_filename)
    data = json.load(f)
    f.close()
    return data


def valor_financiado(cota_financiamento: float, valor_lance: float) -> float:
    return (cota_financiamento / 100) * valor_lance;


def handler() -> None:
    data = read_input_file('input.json')
    cota = data['informacoes-investidor']["cota-financiamento"]
    lance = data["dados-basicos"]["valor-lance"]
    valor = valor_financiado(cota, lance)
    print()
    print("Entrada de Dados")
    print(f"\tCota de Financiamento: {locale.currency(cota, grouping=True, symbol=None)} %")
    print(f"\tValor do Lance: R$ {locale.currency(lance, grouping=True, symbol=None)}")
    print("Valor Calculado")
    print(f"\tCota Financiamento: R$ {locale.currency(valor, grouping=True, symbol=None)}")


if __name__ == "__main__":
    handler()
