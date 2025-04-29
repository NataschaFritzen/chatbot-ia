# Chatbot IA

Este é um chatbot inteligente que responde a perguntas relacionadas ao conteúdo de um PDF. O chatbot é capaz de processar perguntas sobre temas como cuidados com cachorros, gatos, vacinação, alimentação e outros, utilizando uma técnica simples de **busca por palavras-chave** para gerar respostas baseadas nas informações extraídas do arquivo PDF.

## Tecnologias Utilizadas

- **Python 3.x**
- **PyMuPDF (fitz)**: Para leitura de PDFs e extração de texto.
- **Busca por palavras-chave**: Técnica simples de busca por palavras-chave para gerar respostas no chatbot.

## Funcionalidades

- Leitura de um arquivo PDF e extração de seu conteúdo
- Resposta a perguntas com base no conteúdo do PDF utilizando correspondência por palavras-chave
- Respostas relacionadas a temas como cuidados com cachorros, gatos, alimentação, vacinas, entre outros

## Instalação

### 1. Clonar o repositório

Clone este repositório para o seu ambiente local:

```

https://github.com/NataschaFritzen/chatbot-ia
```

## 2. Criar um ambiente virtual (opcional, mas recomendado)

```

python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```

## 3. Instalar as dependências

```

pip install -r requirements.txt
```

## 4. Arquivo PDF

Coloque o seu arquivo PDF de referência (por exemplo, Document_pets.pdf) na pasta docs/ do projeto.

## Como Rodar o Chatbot

1. Execute o script chatbot.py para iniciar o chatbot.

```

python main.py
```

2. O chatbot vai solicitar perguntas no terminal. Você pode perguntar sobre o conteúdo do PDF, como cuidados com animais, vacinação, alimentação, etc. Para encerrar, basta digitar "sair".

## Licença

Este projeto foi desenvolvido como parte **Criando um Chatbot** da plataforma Dio.
