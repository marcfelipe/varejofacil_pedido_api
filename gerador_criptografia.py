import criptografia

senha_bd = input('Digite a senha do banco:\n')
senha_link = input('Digite a senha do usuário no link:\n')

senha_bd_cript = criptografia.encrypt(5, senha_bd)
senha_link_cript = criptografia.encrypt(5, senha_link)


print('Senha banco gravar no toml.\n', senha_bd_cript)
print('Senha link gravar no toml.\n', senha_link_cript)

input('Pressione enter para encerrar...')