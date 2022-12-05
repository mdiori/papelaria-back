# Backend - Aplicação de controle de comissões de uma papelaria

## 1 - Requisitos

- Python versão >= 3.
- Docker ou banco Postgres instalado.

## 2 - DER

![der](./documentation/der_V3.png)

## 3 - Rodar o servidor em modo de desenvolvimento

1. Clonar o repositório.
2. Renomear o arquivo `.env.example` para `.env`.
3. Configurar um banco com os dados existentes no `.env` ou caso prefira rodar
   o seguinte comando para criar um container com o postgres:

   ```
   docker run --name amcom-database -e POSTGRES_PASSWORD=password -p 5432:5432 -d --restart=always postgres
   ```

4. Acessar o folder do repositório clonado pelo terminal.
5. Criar um environment com o seguinte comando:

   ```
   python -m venv .
   ```

6. Instalar os requisitos do requirements.txt com o seguinte comando:

   ```
   pip install -r .
   ```

7. Rodar o seguinte script para criar o usuário admin e alimentar o banco com os
   seeds de exemplo:

   ```
   sh scripts/entrypoint
   ```

8. E por fim rodar o seguinte comando para iniciar o servidor:

   ```
   python manage.py runserver
   ```

## 4 - Acesso ao admin

URL: localhost:8000/admin/

E a senha e o usuário são as presentes no arquivo `.env`.

## 5 - Implementações Futuras

- Autentição de requests.
- Documentação com swagger.

## 6 - Testes unitários

```
python manage.py test
```
