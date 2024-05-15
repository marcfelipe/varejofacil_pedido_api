Exemplo de uso da API do sistema varejofacil para envio de pedidos, com a possibilidade de escolher a loja.

# Instruções:

 - Renomeie arquivo config_modelo.toml para config.toml
 - Preencha com os dados corretos da sua conexão e seu banco.
 - Há um config_modelo equivalente para toml tanto para firebird quanto para MSSQL.
 - os campos bd_pwd e client_pwd são criptofrados e devem ser obtidos com o gerador_criptografia.py
 - instale os packages presentes no requirements.txt
 - A versão utilizada do Python utilizada: 3.12


Para executar, apenas execute:
python app_envio.py