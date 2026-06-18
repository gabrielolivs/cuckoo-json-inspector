import json
from pathlib import Path

def load_json(file_path: str) -> dict:
    """
    Carrega um arquivo JSON e retorna seu conteúdo como dicionário Python.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    if not path.is_file():
        raise ValueError(f"O caminho informado não é um arquivo: {file_path}")

    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError as error:
        raise ValueError(f"Arquivo JSON inválido: {error}") from error