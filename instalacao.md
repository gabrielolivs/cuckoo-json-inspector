## Execução com Docker

Esta seção apresenta o passo a passo para executar a ferramenta **Cuckoo JSON Inspector** utilizando Docker.

O uso do Docker facilita a execução do artefato, pois o usuário não precisa instalar Python, bibliotecas ou configurar ambiente localmente. Basta ter o Docker instalado e executar os comandos abaixo.

---

## 1. Pré-requisitos

Antes de executar a ferramenta, é necessário ter o Docker instalado na máquina.

Para verificar se o Docker está instalado corretamente, execute:

```bash
docker --version
```

Saída esperada:

```bash
Docker version XX.XX.X
```

Caso o comando não seja reconhecido, instale o Docker Desktop:

* Windows/macOS: https://www.docker.com/products/docker-desktop/
* Linux: utilize o gerenciador de pacotes da sua distribuição.

---

## 2. Estrutura esperada do projeto

A ferramenta espera que exista uma pasta chamada `samples` contendo o arquivo JSON gerado pelo Cuckoo Sandbox.

A estrutura recomendada é:

```text
cuckoo-json-inspector/
│
├── app/
│   ├── __init__.py
│   ├── cli.py
│   ├── extractor.py
│   ├── formatter.py
│   └── json_loader.py
│
├── samples/
│   └── report.json
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── main.py
```

O arquivo principal do relatório deve estar em:

```text
samples/report.json
```

Esse arquivo representa o relatório JSON exportado pelo Cuckoo Sandbox.

---

## 3. Preparar o arquivo JSON

Coloque o relatório do Cuckoo dentro da pasta `samples`.

Exemplo:

```text
samples/report.json
```

Caso o arquivo tenha outro nome, por exemplo:

```text
samples/cuckoo_report.json
```

será necessário informar esse nome no comando de execução.

---

## 4. Construir a imagem Docker

Na raiz do projeto, onde está localizado o arquivo `Dockerfile`, execute:

```bash
docker build -t cuckoo-json-inspector .
```

Explicação do comando:

```bash
docker build
```

Cria uma imagem Docker a partir do `Dockerfile`.

```bash
-t cuckoo-json-inspector
```

Define o nome da imagem como `cuckoo-json-inspector`.

```bash
.
```

Indica que o Dockerfile está no diretório atual.

Após a execução, a imagem estará disponível localmente.

Para verificar se a imagem foi criada, execute:

```bash
docker images
```

A imagem `cuckoo-json-inspector` deve aparecer na lista.

---

## 5. Executar a ferramenta no Linux ou macOS

Com o arquivo `samples/report.json` disponível, execute:

```bash
docker run --rm -it -v "$PWD/samples:/data" cuckoo-json-inspector
```

Esse comando inicia a ferramenta diretamente no modo de menu interativo.

---

## 6. Executar a ferramenta no Windows PowerShell

No Windows PowerShell, utilize:

```powershell
docker run --rm -it -v "${PWD}/samples:/data" cuckoo-json-inspector
```

Esse comando monta a pasta `samples` do projeto dentro do container no caminho `/data`.

---

## 7. O que acontece ao executar

Ao executar o comando, a ferramenta abrirá o menu interativo:

```text
=== Cuckoo JSON Inspector ===
Arquivo carregado: /data/report.json
1 - Listar seções principais
2 - Extrair por caminho
3 - Buscar palavra-chave
4 - Mostrar resumo
0 - Sair
Escolha uma opção:
```

A partir desse menu, o usuário poderá:

* Listar as seções principais do relatório JSON.
* Extrair informações usando caminhos como `behavior`, `behavior.processes` ou `network`.
* Buscar palavras-chave dentro do relatório.
* Gerar um resumo básico do conteúdo analisado.

---

## 8. Executar usando outro nome de arquivo

Caso o relatório tenha outro nome, por exemplo:

```text
samples/cuckoo_report.json
```

execute no Linux/macOS:

```bash
docker run --rm -it -v "$PWD/samples:/data" cuckoo-json-inspector -f /data/cuckoo_report.json --menu
```

No Windows PowerShell:

```powershell
docker run --rm -it -v "${PWD}/samples:/data" cuckoo-json-inspector -f /data/cuckoo_report.json --menu
```

---

## 9. Exemplos de execução direta sem menu

Além do menu interativo, também é possível executar comandos específicos diretamente.

### Listar seções principais

Linux/macOS:

```bash
docker run --rm -it -v "$PWD/samples:/data" cuckoo-json-inspector -f /data/report.json --keys
```

Windows PowerShell:

```powershell
docker run --rm -it -v "${PWD}/samples:/data" cuckoo-json-inspector -f /data/report.json --keys
```

---

### Extrair a seção `behavior`

Linux/macOS:

```bash
docker run --rm -it -v "$PWD/samples:/data" cuckoo-json-inspector -f /data/report.json --path behavior
```

Windows PowerShell:

```powershell
docker run --rm -it -v "${PWD}/samples:/data" cuckoo-json-inspector -f /data/report.json --path behavior
```

---

### Extrair os processos analisados

Linux/macOS:

```bash
docker run --rm -it -v "$PWD/samples:/data" cuckoo-json-inspector -f /data/report.json --path behavior.processes
```

Windows PowerShell:

```powershell
docker run --rm -it -v "${PWD}/samples:/data" cuckoo-json-inspector -f /data/report.json --path behavior.processes
```

---

### Buscar uma palavra-chave

Exemplo buscando por `CreateFile`:

Linux/macOS:

```bash
docker run --rm -it -v "$PWD/samples:/data" cuckoo-json-inspector -f /data/report.json --search CreateFile
```

Windows PowerShell:

```powershell
docker run --rm -it -v "${PWD}/samples:/data" cuckoo-json-inspector -f /data/report.json --search CreateFile
```

---

### Gerar resumo do relatório

Linux/macOS:

```bash
docker run --rm -it -v "$PWD/samples:/data" cuckoo-json-inspector -f /data/report.json --summary
```

Windows PowerShell:

```powershell
docker run --rm -it -v "${PWD}/samples:/data" cuckoo-json-inspector -f /data/report.json --summary
```

---

## 10. Executar com Docker Compose

Também é possível executar a ferramenta usando Docker Compose.

Primeiro, verifique se existe um arquivo `docker-compose.yml` na raiz do projeto com o seguinte conteúdo:

```yaml
services:
  cuckoo-json-inspector:
    build: .
    image: cuckoo-json-inspector
    container_name: cuckoo-json-inspector
    volumes:
      - ./samples:/data
    stdin_open: true
    tty: true
```

Depois, execute:

```bash
docker compose run --rm cuckoo-json-inspector
```

Esse comando também abrirá a ferramenta diretamente no menu interativo.

---

## 11. Possíveis erros

### Erro: Arquivo não encontrado: /data/report.json

Esse erro ocorre quando o container não encontra o arquivo padrão esperado.

Verifique se o arquivo existe em:

```text
samples/report.json
```

A estrutura correta deve ser:

```text
samples/
└── report.json
```

Caso o arquivo esteja com outro nome, informe o nome correto:

```powershell
docker run --rm -it -v "${PWD}/samples:/data" cuckoo-json-inspector -f /data/nome_do_arquivo.json --menu
```

---

### Erro relacionado ao volume no Windows

Caso o Docker não consiga montar a pasta corretamente no Windows, verifique:

1. Se o Docker Desktop está aberto.
2. Se você está executando o comando na raiz do projeto.
3. Se a pasta `samples` existe.
4. Se o arquivo `report.json` está dentro da pasta `samples`.

Também é possível testar se a pasta foi montada corretamente com:

```powershell
docker run --rm -it -v "${PWD}/samples:/data" --entrypoint sh cuckoo-json-inspector
```

Dentro do container, execute:

```sh
ls -la /data
```

Se o arquivo `report.json` aparecer, o volume está funcionando corretamente.

---

## 12. Remover a imagem Docker

Caso queira remover a imagem criada, execute:

```bash
docker rmi cuckoo-json-inspector
```

---

## 13. Benefício do Docker para o artefato

A execução via Docker melhora a reprodutibilidade do artefato, pois padroniza o ambiente de execução. Dessa forma, avaliadores e usuários conseguem executar a ferramenta sem depender da configuração local de Python, versão de sistema operacional ou instalação manual de dependências.
