## 🍽️ Kitchen Service

Aplicação web desenvolvida em **Django** para gerenciamento de uma cozinha, permitindo o cadastro, visualização e organização de **dishes**, **dish types** e **cooks**, com autenticação padrão do Django e relacionamento entre as entidades.

O sistema foi criado com foco em **organização de dados**, **CRUD completo**, **navegação clara** e **boas práticas de desenvolvimento back-end**.

---

## 📦 Instalação e execução local

Clone o repositório:

```bash
git clone https://github.com/EduardoMoen/kitchen-service
cd kitchen-service
```
Instale as dependências:

```bash
pip install -r requirements.txt
```
Aplique as migrations:

```bash
python manage.py migrate
```
Crie um superusuário:

```bash
python manage.py createsuperuser
```
Execute o servidor:

```bash
python manage.py runserver
```

## 🔐 Autenticação
O projeto utiliza a autenticação padrão do Django.
O acesso às funcionalidades é feito por usuários cadastrados no sistema.
