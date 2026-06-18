from typing import Any

def list_top_level_keys(data: dict) -> list[str]:
    """
    Retorna as chaves principais do relatório JSON.
    """

    return list(data.keys())

def get_by_path(data: dict, path: str) -> Any:
    """
    Extrai uma informação do JSON usando caminho com ponto.
    Exemplo: behavior.processes
    """

    current_value: Any = data

    for key in path.split("."):
        if isinstance(current_value, dict):
            current_value = current_value.get(key)
        elif isinstance(current_value, list):
            try:
                index = int(key)
                current_value = current_value[index]
            except (ValueError, IndexError):
                return None
        else:
            return None

        if current_value is None:
            return None

    return current_value

def search_keyword(data: Any, keyword: str, current_path: str = "") -> list[dict]:
    """
    Busca uma palavra-chave em todo o JSON.
    Retorna os caminhos onde a palavra foi encontrada.
    """

    results = []

    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{current_path}.{key}" if current_path else key

            if keyword.lower() in str(key).lower():
                results.append({
                    "path": new_path,
                    "match_type": "key",
                    "value": key
                })

            results.extend(search_keyword(value, keyword, new_path))

    elif isinstance(data, list):
        for index, item in enumerate(data):
            new_path = f"{current_path}.{index}"
            results.extend(search_keyword(item, keyword, new_path))

    else:
        if keyword.lower() in str(data).lower():
            results.append({
                "path": current_path,
                "match_type": "value",
                "value": data
            })

    return results

def build_summary(data: dict) -> dict:
    """
    Gera um resumo básico do relatório Cuckoo.
    """

    behavior = data.get("behavior", {})
    target = data.get("target", {})
    signatures = data.get("signatures", [])
    network = data.get("network", {})

    processes = behavior.get("processes", [])

    return {
        "target": target,
        "total_processes": len(processes),
        "total_signatures": len(signatures),
        "network_sections": list(network.keys()) if isinstance(network, dict) else [],
        "available_sections": list(data.keys())
    }