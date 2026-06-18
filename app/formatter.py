import json
from typing import Any

def print_json(data: Any) -> None:
    """
    Imprime dados no terminal em formato JSON bonito.
    """

    print(json.dumps(data, indent=2, ensure_ascii=False))

def print_list(items: list[str]) -> None:
    """
    Imprime uma lista simples no terminal.
    """

    for item in items:
        print(f"- {item}")

def print_search_results(results: list[dict]) -> None:
    """
    Imprime os resultados da busca por palavra-chave.
    """

    if not results:
        print("Nenhum resultado encontrado.")
        return

    for result in results:
        print(f"[{result['match_type']}] {result['path']} -> {result['value']}")