import json

class Pessoa(object):
    pass


class Endereco(object):
    def __init__(self, cep, uf, codigoIbge, municipio, logradouro, numero, bairro, complemento,
                pontoDeReferencia, tipoDeEndereco, codigoDoPais, dataDeSuspensao, restricoes):

        self.cep = cep
        self.uf = uf
        self.codigoIbge = codigoIbge
        self.municipio = municipio
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.complemento = complemento
        self.pontoDeReferencia = pontoDeReferencia
        self.tipoDeEndereco = tipoDeEndereco
        self.codigoDoPais = codigoDoPais
        self.dataDeSuspensao = dataDeSuspensao
        self.restricoes = restricoes

    def get_cep(self):
        return self.cep

    def serialize(self, json_=False):
        dict_endereco = {}
        dict_endereco['cep'] = self.cep
        dict_endereco['uf'] = self.uf
        dict_endereco['codigoIbge'] = self.codigoIbge
        dict_endereco['municipio'] = self.municipio
        dict_endereco['logradouro'] = self.logradouro
        dict_endereco['numero'] = self.numero
        dict_endereco['bairro'] = self.bairro
        dict_endereco['complemento'] = self.complemento
        dict_endereco['pontoDeReferencia'] = self.pontoDeReferencia
        dict_endereco['tipoDeEndereco'] = self.tipoDeEndereco
        dict_endereco['codigoDoPais'] = self.codigoDoPais
        dict_endereco['dataDeSuspensao'] = self.dataDeSuspensao
        dict_endereco['restricoes'] = self.restricoes
        if json_:
            return json.dumps(dict_endereco)
        else:
            return dict_endereco


class Cliente(object):
    def __init__(self, id_, idExterno, senha, origemDeAlteracao, chaveDaRetaguarda, versaoDaRetaguarda,
                 tipoDeCliente, versao, enderecos, referencias, dependentes, numeroDoDocumento,
                 numeroDeIdentificacao, orgaoExpedidor, cei, inscricaoMunicipal, nome, fantasia,
                 telefone1, telefone2, fax, email, homePage, redeSocial, twitter, comunicadorDeMensagensInstantaneas,
                 suframa, tipoDePessoa, tipoContribuinte, holdingId, dataDeNascimento, estadoCivil,
                 sexo, orgaoPublico, clienteRetemISS, atividade, pessoaParaContato, naturalidade,
                 observacao, renda, outraRenda, tipoDeResidencia, tempoDeResidencia, tempoDeTrabalhoNaEmpresaAtual,
                 comprovanteDeRenda, comprovanteDeResidencia, situacaoDaAprovacao, tabelaPrazo, prazo,
                 tipoDePreco, dataDeBloqueio, tipoDeBloqueio, descontoConcedidoAoCliente, diaDeFechamento,
                 statusId, ramoId, lojaId, tipoAliquotasEspecificas):

        self.id_ = id_
        self.idExterno = idExterno
        self.senha = senha
        self.origemDeAlteracao = origemDeAlteracao
        self.chaveDaRetaguarda = chaveDaRetaguarda
        self.versaoDaRetaguarda = versaoDaRetaguarda
        self.tipoDeCliente = tipoDeCliente
        self.versao = versao
        self.enderecos = enderecos
        self.referencias = referencias
        self.dependentes = dependentes
        self.numeroDoDocumento = numeroDoDocumento
        self.numeroDeIdentificacao = numeroDeIdentificacao
        self.orgaoExpedidor = orgaoExpedidor
        self.cei = cei
        self.inscricaoMunicipal = inscricaoMunicipal
        self.nome = nome
        self.fantasia = fantasia
        self.telefone1 = telefone1
        self.telefone2 = telefone2
        self.fax = fax
        self.email = email
        self.homePage = homePage
        self.redeSocial = redeSocial
        self.twitter = twitter
        self.comunicadorDeMensagensInstantaneas = comunicadorDeMensagensInstantaneas
        self.suframa = suframa
        self.tipoDePessoa = tipoDePessoa
        self.tipoContribuinte = tipoContribuinte
        self.holdingId = holdingId
        self.dataDeNascimento = dataDeNascimento
        self.estadoCivil = estadoCivil
        self.sexo = sexo
        self.orgaoPublico = orgaoPublico
        self.clienteRetemISS = clienteRetemISS
        self.atividade = atividade
        self.pessoaParaContato = pessoaParaContato
        self.naturalidade = naturalidade
        self.observacao = observacao
        self.renda = renda
        self.outraRenda = outraRenda
        self.tipoDeResidencia = tipoDeResidencia
        self.tempoDeResidencia = tempoDeResidencia
        self.tempoDeTrabalhoNaEmpresaAtual = tempoDeTrabalhoNaEmpresaAtual
        self.comprovanteDeRenda = comprovanteDeRenda
        self.comprovanteDeResidencia = comprovanteDeResidencia
        self.situacaoDaAprovacao = situacaoDaAprovacao
        self.tabelaPrazo = tabelaPrazo
        self.prazo = prazo
        self.tipoDePreco = tipoDePreco
        self.dataDeBloqueio = dataDeBloqueio
        self.tipoDeBloqueio = tipoDeBloqueio
        self.descontoConcedidoAoCliente = descontoConcedidoAoCliente
        self.diaDeFechamento = diaDeFechamento
        self.statusId = statusId
        self.ramoId = ramoId
        self.lojaId = lojaId
        self.tipoAliquotasEspecificas = tipoAliquotasEspecificas

    def set_endereco_titular(self, endereco):
        self.endereco = endereco

    def get_nome(self):
        return self.nome

#    def add_endereco(self, endereco):
#        self.enderecos.appent(endereco)
    def to_string(self):
        print('id_:', self.id_, 'Nome:', self.nome, 'cpf: ', self.numeroDoDocumento)

    def to_json_resumido(self):
        ret_json = {
            "id": self.id_,
            "tipoDeCliente": self.tipoDeCliente,
            "versao": 0,
            "enderecos":[
                {
                    "codigoIbge": self.endereco.codigoIbge,
                    "municipio":self.endereco.municipio,
                    "cep": self.endereco.cep,
                    "uf": self.endereco.uf,
                    "logradouro": self.endereco.logradouro,
                    "numero": self.endereco.numero,
                    "bairro": self.endereco.bairro,
                    "tipoDeEndereco": self.endereco.tipoDeEndereco,
                    "codigoDoPais": self.endereco.codigoDoPais
                },
                {
                    "tipoDeEndereco": "COBRANCA"
                }
            ],
            "referencias": [],
            "numeroDoDocumento": self.numeroDoDocumento,
            "numeroDeIdentificacao": self.numeroDeIdentificacao,
            "nome": self.nome,
            "fantasia": self.fantasia,
            "telefone1": self.telefone1,
            "telefone2": self.telefone2,
            "email": self.email,
            "tipoDePessoa": self.tipoDePessoa,
            "tipoContribuinte": self.tipoContribuinte,
            "holdingId": 1,
            "descontoConcedidoAoCliente": 0,
            "statusId": 0,
            "lojaId": self.lojaId,
            "dependentes": []
        }
        return ret_json


class Fornecedor(object):

    def __init__(self, id_, idExterno, contato, observacao, tabelaPrazo, prazo, ehIsentoDePisCofins, tipoDeFornecedor,
                 prazoDeEntrega, tipoDeFrete, transportadora, servico, regimeEstadualTributarioId,
                 produtorRural, inscricaoEstadual, numeroDoDocumento, numeroDeIdentificacao, orgaoExpedidor,
                 cei, inscricaoMunicipal, nome, fantasia, telefone1, telefone2, fax, email, homePage,
                 redeSocial, twitter, comunicadorDeMensagensInstantaneas, suframa, tipoDePessoa, tipoContribuinte,
                 holdingId, tipoAliquotasEspecificas):
        self.id_ = id_
        self.idExterno = idExterno
        self.contato = contato
        self.observacao = observacao
        self.tabelaPrazo = tabelaPrazo
        self.prazo = prazo
        self.ehIsentoDePisCofins = ehIsentoDePisCofins
        self.tipoDeFornecedor = tipoDeFornecedor
        self.prazoDeEntrega = prazoDeEntrega
        self.tipoDeFrete = tipoDeFrete
        self.transportadora = transportadora
        self.servico = servico
        self.regimeEstadualTributarioId = regimeEstadualTributarioId
        self.produtorRural = produtorRural
        self.inscricaoEstadual = inscricaoEstadual
        self.numeroDoDocumento = numeroDoDocumento
        self.numeroDeIdentificacao = numeroDeIdentificacao
        self.orgaoExpedidor = orgaoExpedidor
        self.cei = cei
        self.inscricaoMunicipal = inscricaoMunicipal
        self.nome = nome
        self.fantasia = fantasia
        self.telefone1 = telefone1
        self.telefone2 = telefone2
        self.fax = fax
        self.email = email
        self.homePage = homePage
        self.redeSocial = redeSocial
        self.twitter = twitter
        self.comunicadorDeMensagensInstantaneas = comunicadorDeMensagensInstantaneas
        self.suframa = suframa
        self.tipoDePessoa = tipoDePessoa
        self.tipoContribuinte = tipoContribuinte
        self.holdingId = holdingId
        self.tipoAliquotasEspecificas = tipoAliquotasEspecificas

    def set_endereco_titular(self, endereco):
        self.endereco = endereco

    def to_string(self):
        print('id_:', self.id_, 'Nome:', self.nome, 'cpf ou cnpj: ', self.numeroDoDocumento)

    def to_json(self, resumido=True):
        if resumido:
            ret_json={
                "id": self.id_,
                "observacao": self.observacao,
                "tabelaPrazo": str(self.tabelaPrazo),
                "prazo": str(self.prazo),
                "ehIsentoDePisCofins": self.ehIsentoDePisCofins,
                "tipoDeFornecedor": self.tipoDeFornecedor,
                "prazoDeEntrega": self.prazoDeEntrega,
                "tipoDeFrete": self.tipoDeFrete,
                "transportadora": self.transportadora,
                "servico": self.servico,
                "regimeEstadualTributarioId": self.regimeEstadualTributarioId,
                "produtorRural": self.produtorRural,
                "inscricaoEstadual": str(self.inscricaoEstadual),
                "numeroDoDocumento": str(self.numeroDoDocumento),
                "numeroDeIdentificacao": str(self.numeroDeIdentificacao),
                "orgaoExpedidor": self.orgaoExpedidor,
                "inscricaoMunicipal": self.inscricaoMunicipal,
                "nome": self.nome,
                "fantasia": self.fantasia,
                "telefone1": str(self.telefone1),
                "fax": self.fax,
                "email": self.email,
                "suframa": self.suframa,
                "tipoDePessoa": self.tipoDePessoa,
                "tipoContribuinte": self.tipoContribuinte,
                "holdingId": self.holdingId,
                "tipoAliquotasEspecificas": self.tipoAliquotasEspecificas,
                "endereco": {
                    "codigoIbge": str(self.endereco.codigoIbge),
                    "municipio": self.endereco.municipio,
                    "cep": str(self.endereco.cep),
                    "uf": self.endereco.uf,
                    "logradouro": self.endereco.logradouro,
                    "numero": str(self.endereco.numero),
                    "bairro": self.endereco.bairro,
                    "tipoDeEndereco": self.endereco.tipoDeEndereco,
                    "codigoDoPais": self.endereco.codigoDoPais
                }
            }
        else:

            ret_json = {

                "id": self.id_,
                "contato": self.contato,
                "observacao": self.observacao,
                "tabelaPrazo": str(self.tabelaPrazo),
                "prazo": str(self.prazo),
                "ehIsentoDePisCofins": self.ehIsentoDePisCofins,
                "tipoDeFornecedor": self.tipoDeFornecedor,
                "prazoDeEntrega": self.prazoDeEntrega,
                "tipoDeFrete": self.tipoDeFrete,
                "transportadora": self.transportadora,
                "servico": self.servico,
                "regimeEstadualTributarioId": self.regimeEstadualTributarioId,
                "produtorRural": self.produtorRural,
                "inscricaoEstadual": str(self.inscricaoEstadual),
                "numeroDoDocumento": str(self.numeroDoDocumento),
                "numeroDeIdentificacao": str(self.numeroDeIdentificacao),
                "orgaoExpedidor": self.orgaoExpedidor,
                "cei": self.cei,
                "inscricaoMunicipal": self.inscricaoMunicipal,
                "nome": self.nome,
                "fantasia": self.fantasia,
                "telefone1": str(self.telefone1),
                "telefone2": str(self.telefone2),
                "fax": str(self.fax).zfill(11),
                "email": self.email,
                "homePage": self.homePage,
                "redeSocial": self.redeSocial,
                "twitter": self.twitter,
                "comunicadorDeMensagensInstantaneas": self.comunicadorDeMensagensInstantaneas,
                "suframa": self.suframa,
                "tipoDePessoa": self.tipoDePessoa,
                "tipoContribuinte": self.tipoContribuinte,
                "holdingId": self.holdingId,
                "tipoAliquotasEspecificas": self.tipoAliquotasEspecificas,
                "enderecos":{
                    "codigoIbge": str(self.endereco.codigoIbge),
                    "municipio": self.endereco.municipio,
                    "cep": str(self.endereco.cep),
                    "uf": self.endereco.uf,
                    "logradouro": self.endereco.logradouro,
                    "numero": str(self.endereco.numero),
                    "bairro": self.endereco.bairro,
                    "tipoDeEndereco": self.endereco.tipoDeEndereco,
                    "codigoDoPais": self.endereco.codigoDoPais
                    }
            }

        return ret_json


class Funcionario(object):
    def __init__(self, id_, idExterno, ramal, cargoSysPDVWeb, dataDeNascimento, cargoSysPDV, tipoDoPrecoPadrao,
                 limiteDeDesconto, percentualComissao1, percentualComissao2,percentualComissao3,
                 recebeComissaoPorMetas, inativo, hash, lojaId, ativo_loja, loja_principal, setorId,
                 numeroDoDocumento, numeroDeIdentificacao, orgaoExpedidor, cei, inscricaoMunicipal, nome,
                 fantasia, telefone1, telefone2, fax, email, homePage, redeSocial, twitter,
                 comunicadorDeMensagensInstantaneas, suframa, tipo, tipoContribuinte, holdingId, endereco):
        self.id_ = id_
        self.idExterno = idExterno
        self.ramal = ramal
        self.cargoSysPDVWeb = cargoSysPDVWeb
        self.dataDeNascimento = dataDeNascimento
        self.cargoSysPDV = cargoSysPDV
        self.tipoDoPrecoPadrao = tipoDoPrecoPadrao
        self.limiteDeDesconto = limiteDeDesconto
        self.percentualComissao1 = percentualComissao1
        self.percentualComissao2 = percentualComissao2
        self.percentualComissao3 = percentualComissao3
        self.recebeComissaoPorMetas = recebeComissaoPorMetas
        self.inativo = inativo
        self.hash = hash
        self.lojaId = inativo
        self.ativo_loja = ativo_loja
        self.loja_principal = loja_principal
        self.setorId = setorId
        self.numeroDoDocumento = numeroDoDocumento
        self.numeroDeIdentificacao = numeroDeIdentificacao
        self.orgaoExpedidor = orgaoExpedidor
        self.cei = cei
        self.inscricaoMunicipal = inscricaoMunicipal
        self.nome = nome
        self.fantasia = fantasia
        self.telefone1 = telefone1
        self.telefone2 = telefone2
        self.fax = fax
        self.email = email
        self.homePage = homePage
        self.redeSocial = redeSocial
        self.twitter = twitter
        self.comunicadorDeMensagensInstantaneas = comunicadorDeMensagensInstantaneas
        self.suframa = suframa
        self.tipo = tipo
        self.tipoContribuinte = tipoContribuinte
        self.holdingId = holdingId
        self.endereco = endereco


    def set_endereco_titular(self, endereco):
        self.endereco = endereco


    def to_string(self):
        print('id_:', self.id_, 'Nome:', self.nome, 'cpf ou cnpj: ', self.numeroDoDocumento)


    def to_json(self):
        ret_json = {
            "id": self.id_,
            "idExterno": self.idExterno,
            "ramal": self.ramal,
            "cargoSysPDVWeb": self.cargoSysPDVWeb,
            "dataDeNascimento": self.dataDeNascimento,
            "cargoSysPDV": self.cargoSysPDV,
            "tipoDoPrecoPadrao": self.tipoDoPrecoPadrao,
            "limiteDeDesconto": self.limiteDeDesconto,
            "percentualComissao1": self.percentualComissao1,
            "percentualComissao2": self.percentualComissao2,
            "percentualComissao3": self.percentualComissao3,
            "recebeComissaoPorMetas": self.recebeComissaoPorMetas,
            "inativo": self.inativo,
            "hash": self.hash,
            "lojasDoFuncionario": [
                {
                  "lojaId": self.lojaId,
#                  "idExterno": "",
                  "ativo": self.ativo_loja,
                  "principal": self.loja_principal
                }
            ],
            "setorId": self.setorId,
            "numeroDoDocumento": self.numeroDoDocumento,
            "numeroDeIdentificacao": self.numeroDeIdentificacao,
            "orgaoExpedidor": self.orgaoExpedidor,
            "cei": self.cei,
            "inscricaoMunicipal": self.inscricaoMunicipal,
            "nome": self.nome,
            "fantasia": self.fantasia,
            "telefone1": self.telefone1,
            "telefone2": self.telefone2,
            "fax": self.fax,
            "email": self.email,
            "homePage": self.homePage,
            "redeSocial": self.redeSocial,
            "twitter": self.twitter,
            "comunicadorDeMensagensInstantaneas": self.comunicadorDeMensagensInstantaneas,
            "suframa": self.suframa,
            "tipo": self.tipo,
            "tipoContribuinte": self.tipoContribuinte,
            "holdingId": self.holdingId,
            "endereco": {
                "cep": self.endereco.cep,
                "uf": self.endereco.uf,
                "codigoIbge": self.endereco.codigoIbge,
                "municipio": self.endereco.municipio,
                "logradouro": self.endereco.logradouro,
                "numero": self.endereco.numero,
                "bairro": self.endereco.bairro,
                "complemento": self.endereco.complemento,
                "pontoDeReferencia": self.endereco.pontoDeReferencia,
                "tipoDeEndereco": self.endereco.tipoDeEndereco,
                "codigoDoPais": self.endereco.codigoDoPais,
                "dataDeSuspensao": self.endereco.dataDeSuspensao,
                "restricoes": self.endereco.restricoes
                }
            }
        return ret_json


    def serialize(self, minimal=True):
        dict_funcionario = {}
        if minimal == True:
            dict_funcionario['id'] = self.id_
            dict_funcionario['nome'] = self.nome
            dict_funcionario['endereco'] = self.endereco
            return dict_funcionario
        else:
            return dict_funcionario