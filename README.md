# cuckoo-json-inspector
Ferramenta CLI em Python para análise e extração de informações de relatórios JSON gerados pelo Cuckoo Sandbox.

## Objetivo

O objetivo deste artefato é facilitar a leitura de relatórios JSON extensos produzidos pelo Cuckoo Sandbox, permitindo que analistas extraiam seções específicas, pesquisem palavras-chave e obtenham resumos básicos do comportamento observado.

## Problema de Cibersegurança

Relatórios de análise dinâmica de malware podem conter grande volume de dados, incluindo processos, chamadas de API, alterações em arquivos, registros, rede e assinaturas comportamentais. A inspeção manual desses dados pode ser lenta e sujeita a erros.

Esta ferramenta busca reduzir esse esforço por meio de uma interface de linha de comando simples e reprodutível.

## Funcionalidades

- Listar seções principais do relatório JSON.
- Extrair informações por caminho.
- Buscar palavras-chave em todo o relatório.
- Gerar resumo básico.
- Executar via Python local.
- Executar via Docker.

## Requisitos

- Python 3.11+
- Docker opcional

## Execução local

```bash
python main.py -f samples/sample_report.json --summary
