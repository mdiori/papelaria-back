# Backend - Aplicação de controle de comissões de uma papelaria

## 1 - Requisitos

- Python versão 3.9.
- Docker ou banco Postgres instalado.

## 2 - DER

![der](./documentation/der_V3.png)

## 3 - Rodar o servidor em modo de desenvolvimento

1. Clonar o repositório.
2. Acessar o folder do repositório clonado pelo terminal.
3. Criar um arquivo `.env`.
4. Copiar os dados do arquivo `.env.example` para `.env`.
5. Configurar um banco com os dados existentes no `.env` ou caso prefira rodar
   o seguinte comando para criar um container com o postgres:

   ```
   docker run --name papelaria-database -e POSTGRES_PASSWORD=password -p 5432:5432 -d --restart=always postgres
   ```

6. Criar um environment com o seguinte comando:

   ```
   python -m venv papelaria-env
   ```

   Iniciar o environment com o comando:
   
   ```
   source papelaria-env/bin/activate
   ```
7.  instala os arquivos de desenvolvimento necessários para compilar e construir módulos Python que dependem de bibliotecas C para o Python 3.9: 
   ```
   sudo apt-get install python3.9-dev
   ```
  
8. Instalar os requisitos do requirements.txt com o seguinte comando:

   ```
   pip install -r requirements.txt
   ```

9. Rodar o seguinte script para criar o usuário admin e alimentar o banco com os
   seeds de exemplo:

   ```
   sh scripts/entrypoint.sh
   ```

9. E por fim rodar o seguinte comando para iniciar o servidor:

   ```
   python manage.py runserver
   ```

10. Acesso ao admin

URL: localhost:8000/admin/

E a senha e o usuário são as presentes no arquivo `.env`.

## 4 - Implementações Futuras

- Autentição de requests.
- Documentação com swagger.

## 5 - Testes unitários

```
python manage.py test
```
