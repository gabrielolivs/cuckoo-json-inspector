import argparse

from app.extractor import (
    build_summary,
    get_by_path,
    list_top_level_keys,
    search_keyword,
)
from app.formatter import print_json, print_list, print_search_results
from app.json_loader import load_json

def create_parser() -> argparse.ArgumentParser:
    """
    Cria e configura os argumentos da linha de comando.
    """

    parser = argparse.ArgumentParser(
        prog="cuckoo-json-inspector",
        description="Ferramenta CLI para extrair informações de relatórios JSON do Cuckoo Sandbox."
    )

    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="Caminho para o arquivo report.json gerado pelo Cuckoo."
    )

    parser.add_argument(
        "--keys",
        action="store_true",
        help="Lista as seções principais do relatório JSON."
    )

    parser.add_argument(
        "--path",
        help="Extrai uma informação usando caminho com ponto. Exemplo: behavior.processes"
    )

    parser.add_argument(
        "--search",
        help="Busca uma palavra-chave em todo o relatório JSON."
    )

    parser.add_argument(
        "--summary",
        action="store_true",
        help="Mostra um resumo básico do relatório."
    )

    parser.add_argument(
        "--menu",
        action="store_true",
        help="Abre um menu interativo no terminal."
    )

    return parser

def interactive_menu(data: dict) -> None:
    """
    Exibe um menu simples para o usuário escolher o que deseja extrair.
    """

    while True:
        print("\n=== Cuckoo JSON Inspector ===")
        print("1 - Listar seções principais")
        print("2 - Extrair por caminho")
        print("3 - Buscar palavra-chave")
        print("4 - Mostrar resumo")
        print("0 - Sair")

        option = input("Escolha uma opção: ").strip()

        if option == "1":
            print_list(list_top_level_keys(data))

        elif option == "2":
            path = input("Digite o caminho. Exemplo: behavior.processes: ").strip()
            result = get_by_path(data, path)

            if result is None:
                print("Caminho não encontrado.")
            else:
                print_json(result)

        elif option == "3":
            keyword = input("Digite a palavra-chave: ").strip()
            results = search_keyword(data, keyword)
            print_search_results(results)

        elif option == "4":
            summary = build_summary(data)
            print_json(summary)

        elif option == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")

def main() -> None:
    """
    Função principal da aplicação.
    """

    parser = create_parser()
    args = parser.parse_args()

    try:
        data = load_json(args.file)

        if args.menu:
            interactive_menu(data)

        elif args.keys:
            print_list(list_top_level_keys(data))

        elif args.path:
            result = get_by_path(data, args.path)

            if result is None:
                print("Caminho não encontrado.")
            else:
                print_json(result)

        elif args.search:
            results = search_keyword(data, args.search)
            print_search_results(results)

        elif args.summary:
            summary = build_summary(data)
            print_json(summary)

        else:
            parser.print_help()

    except Exception as error:
        print(f"Erro: {error}")