# Cloud Configuration Guide

## Criar um Database e alterar o config.py

### 1. Criar o Servidor SQL Server
**Serviço Gratuito:** SQL Server no Azure é gratuito para o primeiro ano de contas Azure  
**Limite de Armazenamento:** Contas gratuitas permitem apenas 250 GB de armazenamento gratuito com bancos de dados SQL  
**Localização:** Todos os recursos serão criados na região westus2

```bash
az sql server create --admin-user dbadmin --admin-password p#ssword1234 --name sql-server-jlv-39 --resource-group resource-group-flask --location westus2 --enable-public-network true --verbose
```

### 2. Permitir Acesso dos Serviços Azure

```bash
az sql server firewall-rule create -g resource-group-flask -s sql-server-jlv-39 -n azureaccess --start-ip-address 0.0.0.0 --end-ip-address 0.0.0.0 --verbose
```

### 3. Permitir Acesso do Seu IP Público

```bash
az sql server firewall-rule create -g resource-group-flask -s sql-server-jlv-39 -n clientip --start-ip-address 177.183.198.249  --end-ip-address 177.183.198.249  --verbose
```

### 4. Criar o Banco de Dados

```bash
az sql db create --name hello-world-db --resource-group resource-group-flask --server sql-server-jlv-39 --service-objective S0 --verbose
```

## Criar um Blob Storage e associar ao config.py

### 1. Criar a Conta de Armazenamento

```bash
az storage account create --name helloworld12345jlv --resource-group resource-group-flask --location westus2
```

### 2. Criar o Contêiner de Imagens

```bash
az storage container create --account-name helloworld12345jlv --name images --auth-mode login --public-access container
```

## Próximos Passos

Após executar os comandos acima, será necessário:

1. **Atualizar o config.py** com as informações de conexão do SQL Server
2. **Configurar as variáveis de ambiente** para o Blob Storage
3. **Testar as conexões** para garantir que tudo está funcionando corretamente

### Informações importantes:
- **SQL Server:** sql-server-jlv-39.database.windows.net
- **Database:** hello-world-db
- **Storage Account:** helloworld12345jlv
- **Container:** images
- **Região:** westus2
