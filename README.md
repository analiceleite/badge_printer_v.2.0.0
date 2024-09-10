<h1>Badge Printer v.2.0.0</h1>

## Sobre o Projeto

O **Badge Printer** é uma aplicação desenvolvida para simplificar o processo de impressão de crachás para colaboradores. A aplicação recebe uma planilha com as informações dos funcionários e outra contendo suas fotos, processa as imagens, insere-as no layout personalizado da empresa e, em seguida, envia os crachás finalizados diretamente para impressão, otimizando todo o fluxo de trabalho.

## Estrutura de Pastas

- /badge_printer: Contém o código-fonte principal da aplicação Django.
- /static: Diretório para arquivos estáticos, como imagens e folhas de estilo.
- /templates: Diretório para os templates HTML utilizados pela aplicação.
- /scripts: Diretório para scripts Python adicionais, se necessário.
- /media: Armazenamento das imagens processadas e layouts de crachás.
- /documents: Local para upload das planilhas de informações e imagens.

## Tecnologias Utilizadas

- **Django**: Framework web de alto nível em Python para desenvolvimento rápido e limpo.
- **Sass**: Linguagem de folha de estilo CSS pré-processada que estende a sintaxe do CSS.
- **Openpyxl**: Biblioteca Python para leitura e escrita de arquivos Excel.
- **Pandas**: Biblioteca Python para manipulação e análise de dados.
- **Pillow**: Biblioteca Python para manipulação de imagens.
- **Pypdf2**: Biblioteca para trabalhar com arquivos PDF, como leitura, combinação e divisão de páginas.
- **Rembg**: Ferramenta para remover o fundo de imagens automaticamente.
- **Pdfkit**: Biblioteca Python para renderizar HTML em PDF.
- **Django-wkhtmltopdf**: Integrador do wkhtmltopdf com Django para geração de PDFs.
- **Opencv-python**: Ferramenta para processamento de imagens e visão computacional, amplamente usada em reconhecimento de padrões.
- **Python-dotenv**: Carrega variáveis de ambiente a partir de um arquivo `.env` para a configuração de aplicações.

## Rodando Localmente

Clone o repositório:

```bash
git clone https://github.com/analiceleite/badge-printer.git
```

Instale as dependências:

```bash
pip install -r main_libraries.txt
```

Execute as migrações do Django':

```bash
python manage.py migrate
```

Inicie o servidor local:

```bash
python manage.py runserver
```

Acesse a aplicação em seu navegador através de http://localhost:8000.

## Utilização

1. Faça o upload das planilhas de informações e imagens através da interface da aplicação.
2. A aplicação irá processar as imagens e inseri-las no layout de crachá definido pela empresa.
3. Após o processamento, os crachás prontos estarão disponíveis para visualização e impressão automaticamente.

## Contribuição

Contribuições são bem-vindas! Para sugestões, melhorias ou correções, por favor, abra uma issue ou envie um pull request.

## Autor

Esse projeto foi desenvolvido por:

- Analice Leite;
- João Trindade;

## Licença

Este projeto está licenciado sob a Licença MIT.

## Status

<img src= "https://img.shields.io/badge/Status-Concluded-green"/>
