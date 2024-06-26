# Instruções para Executar o Projeto:

## Instalação das Dependências:

Antes de instalar as dependências, é recomendável criar e ativar um ambiente virtual do Python para isolar as bibliotecas deste projeto das bibliotecas do sistema. Siga as etapas abaixo para criar e ativar um ambiente virtual:

1. **Instale o Virtualenv (opcional):**
   Se você ainda não tiver o virtualenv instalado, pode instalá-lo via pip:
   ```bash
   pip install virtualenv
   ```

2. **Crie o Ambiente Virtual:**
   Na raiz do projeto, execute o seguinte comando para criar um ambiente virtual chamado `venv`:
   ```bash
   python -m venv venv
   ```

3. **Ative o Ambiente Virtual:**
   Depois de criar o ambiente virtual, ative-o usando o seguinte comando (no Windows):
   ```bash
   venv\Scripts\activate
   ```
   Ou este comando (no macOS/Linux):
   ```bash
   source venv/bin/activate
   ```

   Após ativar o ambiente virtual, o prompt do terminal deve mudar para indicar que o ambiente virtual está ativo.

4. **Instale as Dependências:**
   Com o ambiente virtual ativado, você pode instalar as dependências do projeto executando o seguinte comando:
   ```bash
   pip install -r requirements.txt
   ```

   Isso garantirá que todas as bibliotecas necessárias sejam instaladas no ambiente virtual recém-criado.


Isso garantirá que todas as bibliotecas necessárias sejam instaladas corretamente em seu ambiente.

## Execução do Docker Compose:

Utilize o Docker Compose para configurar e iniciar os serviços necessários para o projeto. Execute o seguinte comando na raiz do projeto:

```
docker-compose up -d
```

Isso iniciará os serviços definidos no arquivo docker-compose.yml em segundo plano (-d), permitindo que o projeto seja executado.

## Migration do Banco de Dados com Alembic:

Antes de iniciar os aplicativos, certifique-se de rodar a Migration de Banco para garantir que o banco de dados esteja configurado corretamente. Execute o seguinte comando na raiz do projeto:

```
alembic upgrade head
```

## Execução dos Aplicativos:

Após iniciar os serviços com o Docker Compose e executar a Migration de Banco, você pode executar os aplicativos fornecidos. Certifique-se de que os seguintes scripts Python estejam disponíveis e execute-os conforme necessário:

- `sc_site.py`: Este é o aplicativo do site.
- `sc_server.py`: Este é o aplicativo do servidor.