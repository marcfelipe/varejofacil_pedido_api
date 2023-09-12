
class Produto(object):

    #def __init__(self):

    def __init__(self, id_, idExterno, produtoDestinoId, subgrupoId, grupoId, secaoId,
                 naturezaDeImpostoFederalId, cest, quantidadeEtiqueta, diasDeSeguranca,
                 codigoInterno, descricao, descricaoReduzida, tributacaoId, unidadeDeTransferencia,
                 validade, controlaNumeroSerie, tabelaA, tipoBonificacao, controlaEstoque,
                 associacao, composicao, controlaValidade, enviaBalanca, mix,
                 descricaoVariavel, endereco, foraDeLinha, unidadeDeCompra,
                 unidadeDeReferencia, codigoANP, tipoIPI, tipoAgregacao, precoVariavel,
                 indiceAT, producao, nomenclaturaMercosulId, nomenclaturaMercosulExecaoId,
                 finalidadeProduto, modelo, identificadorDeOrigem, incentivoZonaFranca,
                 imagem, altura, largura, comprimento, unidadeDeVenda, naturezaId, textoDaReceita,
                 permiteDesconto, compoeTotalDaNota, ativoNoEcommerce, atualizaFamilia,
                 frenteLoja, itensEmbalagem, itensEmbalagemVenda, itensEmbalagemTransferencia,
                 custoMedio, qtdMaximaVenda, pesoBruto, pesoLiquido, fatorBonificacao,
                 medidaReferencial, ipi, valorAgregacao, percentualPerda,
                 fatorRendimentoUnidade, fatorRendimentoCusto, descontoMaximo1, descontoMaximo2,
                 descontoMaximo3, incidenciaIPI, dataInclusao, dataAlteracao, dataSaida,
                 tipoFatorkit, baixaNaVendaComposto, comissaoCapitacao, comissaoProducao,
                 comissaoVenda, pagaComissao, pesoVariavel, generoId, marcaId, situacaoFiscalId,
                 situacaoFiscalSaidaId, funcionarioId, fornecedorId, localDeImpressaoId, aplicacacoesIds,
                 caracteristicasIds, regimesDoProduto, lojaId, regimeEstadualId, itensImpostosFederais,
                 pautasDoProduto, estoquedoProduto):

        self.id_ = id_
        self.idExterno = idExterno
        self.produtoDestinoId = produtoDestinoId
        self.subgrupoId = subgrupoId
        self.grupoId = grupoId
        self.secaoId = secaoId
        self.naturezaDeImpostoFederalId = naturezaDeImpostoFederalId
        self.cest = cest
        self.quantidadeEtiqueta = quantidadeEtiqueta
        self.diasDeSeguranca = diasDeSeguranca
        self.codigoInterno = codigoInterno
        self.descricao = descricao
        self.descricaoReduzida = descricaoReduzida
        self.tributacaoId = tributacaoId
        self.unidadeDeTransferencia = unidadeDeTransferencia
        self.validade = validade
        self.controlaNumeroSerie = controlaNumeroSerie
        self.tabelaA = tabelaA
        self.tipoBonificacao = tipoBonificacao
        self.controlaEstoque = controlaEstoque
        self.associacao = associacao
        self.composicao = composicao
        self.controlaValidade = controlaValidade
        self.enviaBalanca = enviaBalanca
        self.mix = mix
        self.descricaoVariavel = descricaoVariavel
        self.endereco = endereco
        self.foraDeLinha = foraDeLinha
        self.unidadeDeCompra = unidadeDeCompra
        self.unidadeDeReferencia = unidadeDeReferencia
        self.codigoANP = codigoANP
        self.tipoIPI = tipoIPI
        self.tipoAgregacao = tipoAgregacao
        self.precoVariavel = precoVariavel
        self.indiceAT = indiceAT
        self.producao = producao
        self.nomenclaturaMercosulId = nomenclaturaMercosulId
        self.nomenclaturaMercosulExecaoId = nomenclaturaMercosulExecaoId
        self.finalidadeProduto = finalidadeProduto
        self.modelo = modelo
        self.identificadorDeOrigem = identificadorDeOrigem
        self.incentivoZonaFranca = incentivoZonaFranca
        self.imagem = imagem
        self.altura = altura
        self.largura = largura
        self.comprimento = comprimento
        self.unidadeDeVenda = unidadeDeVenda
        self.naturezaId = naturezaId
        self.textoDaReceita = textoDaReceita
        self.permiteDesconto = permiteDesconto
        self.compoeTotalDaNota = compoeTotalDaNota
        self.ativoNoEcommerce = ativoNoEcommerce
        self.atualizaFamilia = atualizaFamilia
        self.frenteLoja = frenteLoja
        self.itensEmbalagem = itensEmbalagem
        self.itensEmbalagemVenda = itensEmbalagemVenda
        self.itensEmbalagemTransferencia = itensEmbalagemTransferencia
        self.custoMedio = custoMedio
        self.qtdMaximaVenda = qtdMaximaVenda
        self.pesoBruto = pesoBruto
        self.pesoLiquido = pesoLiquido
        self.fatorBonificacao = fatorBonificacao
        self.medidaReferencial = medidaReferencial
        self.ipi = ipi
        self.valorAgregacao = valorAgregacao
        self.percentualPerda = percentualPerda
        self.fatorRendimentoUnidade = fatorRendimentoUnidade
        self.fatorRendimentoCusto = fatorRendimentoCusto
        self.descontoMaximo1 = descontoMaximo1
        self.descontoMaximo2 = descontoMaximo2
        self.descontoMaximo3 = descontoMaximo3
        self.incidenciaIPI = incidenciaIPI
        self.dataInclusao = dataInclusao
        self.dataAlteracao = dataAlteracao
        self.dataSaida = dataSaida
        self.tipoFatorkit = tipoFatorkit
        self.baixaNaVendaComposto = baixaNaVendaComposto
        self.comissaoCapitacao = comissaoCapitacao
        self.comissaoProducao = comissaoProducao
        self.comissaoVenda = comissaoVenda
        self.pagaComissao = pagaComissao
        self.pesoVariavel = pesoVariavel
        self.generoId = generoId
        self.marcaId = marcaId
        self.situacaoFiscalId = situacaoFiscalId
        self.situacaoFiscalSaidaId = situacaoFiscalSaidaId
        self.funcionarioId = funcionarioId
        self.fornecedorId = fornecedorId
        self.localDeImpressaoId = localDeImpressaoId
        self.aplicacacoesIds = aplicacacoesIds
        self.caracteristicasIds = caracteristicasIds
        self.regimesDoProduto = regimesDoProduto
        self.lojaId = lojaId
        self.regimeEstadualId = regimeEstadualId
        self.itensImpostosFederais = itensImpostosFederais
        self.pautasDoProduto = pautasDoProduto
        self.estoquedoProduto = estoquedoProduto

#Padrão pode ser em branco, então não irei gerar.
    def set_regimes_do_produto(self, lojaId, regimeEstadualId):
        self.regimeEstadualId.append(
            {
                "lojaId": lojaId,
                "regimeEstadualId": regimeEstadualId
            }
        )

    def set_estoque_do_produto(self, lojaId, estoqueMinimo, estoqueMaximo):
        self.estoquedoProduto.append(
            {
                "lojaId": lojaId,
                "estoqueMinimo": str(estoqueMinimo),
                "estoqueMaximo": str(estoqueMaximo)
            }
        )

    def to_string(self, resumido=True):
        imp1 = str(self.itensImpostosFederais[0])
        imp2 = str(self.itensImpostosFederais[1])
        if resumido == True:
            print('Id:', self.id_, '\nDescrição Produto: ', self.descricao, 'NCM:', str(self.nomenclaturaMercosulId))
        else:
            print('Id:', self.id_)
            print('Descrição Produto:', self.descricao)
            print('Descrição Reduzida:', self.descricaoReduzida)
            print('Seção:', str(self.secaoId))
            print('Genero', str(self.generoId))
            print('Unidade Compra:', self.unidadeDeCompra)
            print('Unidade de Venda:', self.unidadeDeVenda)
            print('Nomenclatura (NCM):', str(self.nomenclaturaMercosulId))
            print('Situação Fiscal:', str(self.situacaoFiscalId))
            print('Tabela A:', self.tabelaA)
            print('Impostos Federais:', imp1, imp2)


    def set_valor_padrao(self):
        self.idExterno = ""
        self.produtoDestinoId = 0
        self.subgrupoId = 0
        self.grupoId = 0
        #self.secaoId = secaoId
        self.naturezaDeImpostoFederalId = 0
        self.cest = 0
        self.quantidadeEtiqueta = 0
        self.diasDeSeguranca = 0
        self.codigoInterno = ""
        #self.descricao = ""
        #self.descricaoReduzida = ""
        #self.tributacaoId = "F00"
        self.unidadeDeTransferencia = "UN"
        self.validade = "0"
        self.controlaNumeroSerie = False
        self.tabelaA = "NACIONAL"
        self.tipoBonificacao = "NAO_GERA_PONTOS"
        self.controlaEstoque = True
        self.associacao = "NORMAL"
        self.composicao = "NORMAL"
        self.controlaValidade = False
        self.enviaBalanca = True
        self.mix = ""
        self.descricaoVariavel = False
        self.endereco = ""
        self.foraDeLinha = "N"
        self.unidadeDeCompra = "UN"
        self.unidadeDeReferencia = "UN"
        self.codigoANP = ""
        self.tipoIPI = "PERCENTUAL"
        self.tipoAgregacao = "PAUTA"
        self.precoVariavel = False
        self.indiceAT = "ARREDONDA"
        self.producao = "TERCEIROS"
        self.nomenclaturaMercosulId = ""    #AQUI É NCM
        self.nomenclaturaMercosulExecaoId = ""  #AQUI NCM EXCEÇÃO
        self.finalidadeProduto = "COMERCIALIZACAO"
        self.modelo = ""
        self.identificadorDeOrigem = ""
        self.incentivoZonaFranca = "S"
        self.imagem = ""
        self.altura = ""
        self.largura = ""
        self.comprimento = ""
        self.unidadeDeVenda = "UN"
        self.naturezaId = ""
        self.textoDaReceita = ""
        self.permiteDesconto = True
        self.compoeTotalDaNota = True
        self.ativoNoEcommerce = False
        self.atualizaFamilia = False
        self.frenteLoja = False
        self.itensEmbalagem = 0
        self.itensEmbalagemVenda = 0
        self.itensEmbalagemTransferencia = 0
        self.custoMedio = 0
        self.qtdMaximaVenda = 0
        self.pesoBruto = 0
        self.pesoLiquido = 0
        self.fatorBonificacao = 0
        self.medidaReferencial = 0
        self.ipi = 0
        self.valorAgregacao = 0
        self.percentualPerda = 0
        self.fatorRendimentoUnidade = 0
        self.fatorRendimentoCusto = 0
        self.descontoMaximo1 = 0
        self.descontoMaximo2 = 0
        self.descontoMaximo3 = 0
        self.incidenciaIPI = "COMPRA"
        self.dataInclusao = "01/01/2019"
        self.dataAlteracao = "01/01/2019"
        self.dataSaida = "01/01/2019"
        self.tipoFatorkit = "PRECO"
        self.baixaNaVendaComposto = False
        self.comissaoCapitacao = 0
        self.comissaoProducao = 0
        self.comissaoVenda = 0
        self.pagaComissao = True
        self.pesoVariavel = "SIM"
        self.generoId = 0
        self.marcaId = 0
        self.situacaoFiscalId = 0
        self.situacaoFiscalSaidaId = 0
        self.funcionarioId = 0
        self.fornecedorId = 0
        self.localDeImpressaoId = 0
        self.aplicacacoesIds = [0]
        self.caracteristicasIds = [0]
        self.regimesDoProduto = [
            {
                "lojaId": 0,
                "regimeEstadualId": 0
            }
        ]
        self.lojaId = 1
        self.regimesDoProduto = []
        self.itensImpostosFederais = [
            {
                "id": "01"
            },
            {
                "id": "02"
            }
        ]
        self.pautasDoProduto = [
            {
                "uf": "string",
                "tipoDePauta": "FIXA",
                "valorDePauta": 0
            }
        ]
        self.estoquedoProduto = [{
            "lojaId": 0,
            "estoqueMinimo": 0,
            "estoqueMaximo": 0
        }]

    def to_json_resumido(self):
        if not self.itensImpostosFederais:
            self.itensImpostosFederais.append('01')
            self.itensImpostosFederais.append('02')

        ret_json = {
            "secaoId": int(self.secaoId),
            "naturezaDeImpostoFederalId": self.naturezaDeImpostoFederalId,
            "diasDeSeguranca": self.diasDeSeguranca,
            "descricao": self.descricao,
            "descricaoReduzida": self.descricaoReduzida,
            "controlaNumeroSerie": self.controlaNumeroSerie,
            "tabelaA": self.tabelaA,
            "tipoBonificacao": self.tipoBonificacao,
            "controlaEstoque": self.controlaEstoque,
            "associacao": self.associacao,
            "composicao": self.composicao,
            "fatorRendimentoUnidade": "0",
            "fatorRendimentoCusto": "0",
            "controlaValidade": self.controlaValidade,
            "enviaBalanca": self.enviaBalanca,
            "foraDeLinha": self.foraDeLinha,
            "unidadeDeCompra": self.unidadeDeCompra,
            "tipoIPI": self.tipoIPI,
            "precoVariavel": self.precoVariavel,
            "indiceAT": self.indiceAT,
            "producao": self.producao,
            "nomeclaturaMercosulId": self.nomenclaturaMercosulId,
            "nomeclaturaMercosulExcecaoId": self.nomenclaturaMercosulExecaoId,
            "finalidadeProduto": self.finalidadeProduto,
            "incentivoZonaFranca": self.incentivoZonaFranca,
            "altura": "",
            "largura": "",
            "comprimento": "",
            "unidadeDeVenda": str(self.unidadeDeVenda),
            "permiteDesconto": self.permiteDesconto,
            "compoeTotalDaNota": self.compoeTotalDaNota,
            "ativoNoEcommerce": self.ativoNoEcommerce,
            "atualizaFamilia": self.atualizaFamilia,
            "frenteLoja": self.frenteLoja,
            "itensEmbalagem": int(round(self.itensEmbalagem, 0)),
            "itensEmbalagemVenda": int(round(self.itensEmbalagemVenda, 0)),
            "itensEmbalagemTransferencia": int(round(self.itensEmbalagemTransferencia, 0)),
            "dataInclusao": "2018-07-25T03:00:00.000+0000",
            "dataAlteracao": "2018-07-25T03:00:00.000+0000",
            "pagaComissao": self.pagaComissao,
            "pesoVariavel": self.pesoVariavel,
            "generoId": int(self.generoId),
            "situacaoFiscalId": self.situacaoFiscalId,
            "situacaoFiscalSaidaId": self.situacaoFiscalSaidaId,
            "localDeImpressaoId": self.localDeImpressaoId,
            "aplicacoesIds": self.aplicacacoesIds,
            "caracteristicasIds": self.caracteristicasIds,
            "regimesDoProduto": self.regimesDoProduto,
            "itensImpostosFederais": [
                {
                    "id": str(self.itensImpostosFederais[0])
                },
                {
                    "id": str(self.itensImpostosFederais[1])
                }
            ],
            "pautasDoProduto": self.pautasDoProduto,
            "estoqueDoProduto": self.estoquedoProduto
        }
        if self.id_ != 0:
            #ret_json["id"] = int(self.id_)
            ret_json.setdefault("id", self.id_)
        return ret_json

    def to_json_resumido_validacao(self):
        if not self.itensImpostosFederais:
            self.itensImpostosFederais.append('01')
            self.itensImpostosFederais.append('02')

        ret_json = {
            "id": int(self.id_),
            "secaoId": int(self.secaoId),
            "naturezaDeImpostoFederalId": self.naturezaDeImpostoFederalId,
            "diasDeSeguranca": 0,
            "descricao": self.descricao,
            "descricaoReduzida": self.descricaoReduzida,
            "controlaNumeroSerie": self.controlaNumeroSerie,
            "tabelaA": self.tabelaA,
            "tipoBonificacao": self.tipoBonificacao,
            "controlaEstoque": "true",
            "associacao": self.associacao,
            "composicao": self.composicao,
            "fatorRendimentoUnidade": "1",
            "fatorRendimentoCusto": "1",
            "controlaValidade": self.controlaValidade,
            "enviaBalanca": self.enviaBalanca,
            "foraDeLinha": self.foraDeLinha,
            "unidadeDeCompra": self.unidadeDeCompra,
            "tipoIPI": self.tipoIPI,
            "precoVariavel": self.precoVariavel,
            "indiceAT": self.indiceAT,
            "producao": self.producao,
            "nomeclaturaMercosulId": self.nomenclaturaMercosulId,
            "nomeclaturaMercosulExcecaoId": self.nomenclaturaMercosulExecaoId,
            "finalidadeProduto": self.finalidadeProduto,
            "incentivoZonaFranca": self.incentivoZonaFranca,
            "altura": "",
            "largura": "",
            "comprimento": "",
            "unidadeDeVenda": self.unidadeDeVenda,
            "permiteDesconto": True,
            "compoeTotalDaNota": True,
            "ativoNoEcommerce": False,
            "atualizaFamilia": False,
            "frenteLoja": False,
            "itensEmbalagem": int(round(self.itensEmbalagem, 0)),
            "itensEmbalagemVenda": int(round(self.itensEmbalagemVenda, 0)),
            "itensEmbalagemTransferencia": int(round(self.itensEmbalagemTransferencia, 0)),
            "dataInclusao": "2018-07-25T03:00:00.000+0000",
            "dataAlteracao": "2018-07-25T03:00:00.000+0000",
            "pagaComissao": self.pagaComissao,
            "pesoVariavel": self.pesoVariavel,
            "generoId": int(self.generoId),
            "situacaoFiscalId": self.situacaoFiscalId,
            "situacaoFiscalSaidaId": self.situacaoFiscalSaidaId,
            "localDeImpressaoId": self.localDeImpressaoId,
            "aplicacoesIds": self.aplicacacoesIds,
            "caracteristicasIds": self.caracteristicasIds,
            "regimesDoProduto": self.regimesDoProduto,
            "itensImpostosFederais": [
                {
                    "id": str(self.itensImpostosFederais[0])
                },
                {
                    "id": str(self.itensImpostosFederais[1])
                }
            ],
            "pautasDoProduto": self.pautasDoProduto,
            "estoqueDoProduto": self.estoquedoProduto
        }
        return ret_json

    def to_json_resumido2(self):
        if not self.itensImpostosFederais:
            self.itensImpostosFederais.append('01')
            self.itensImpostosFederais.append('02')

        ret_json = {
            "id": int(self.id_),
            "secaoId": int(self.secaoId),
            "naturezaDeImpostoFederalId": self.naturezaDeImpostoFederalId,
            "diasDeSeguranca": self.diasDeSeguranca,
            "descricao": self.descricao,
            "descricaoReduzida": self.descricaoReduzida,
            "controlaNumeroSerie": self.controlaNumeroSerie,
            "tabelaA": self.tabelaA,
            "tipoBonificacao": self.tipoBonificacao,
            "controlaEstoque": self.controlaEstoque,
            "associacao": self.associacao,
            "composicao": self.composicao,
            "fatorRendimentoUnidade": "0",
            "fatorRendimentoCusto": "0",
            "controlaValidade": self.controlaValidade,
            "enviaBalanca": self.enviaBalanca,
            "foraDeLinha": self.foraDeLinha,
            "unidadeDeCompra": self.unidadeDeCompra,
            "tipoIPI": self.tipoIPI,
            "precoVariavel": self.precoVariavel,
            "indiceAT": self.indiceAT,
            "producao": self.producao,
            "nomeclaturaMercosulId": self.nomenclaturaMercosulId,
            "nomeclaturaMercosulExcecaoId": self.nomenclaturaMercosulExecaoId,
            "finalidadeProduto": self.finalidadeProduto,
            "incentivoZonaFranca": self.incentivoZonaFranca,
            "altura": "",
            "largura": "",
            "comprimento": "",
            "unidadeDeVenda": str(self.unidadeDeVenda),
            "permiteDesconto": self.permiteDesconto,
            "compoeTotalDaNota": self.compoeTotalDaNota,
            "ativoNoEcommerce": self.ativoNoEcommerce,
            "atualizaFamilia": self.atualizaFamilia,
            "frenteLoja": self.frenteLoja,
            "itensEmbalagem": int(round(self.itensEmbalagem, 0)),
            "itensEmbalagemVenda": int(round(self.itensEmbalagemVenda, 0)),
            "itensEmbalagemTransferencia": int(round(self.itensEmbalagemTransferencia, 0)),
            "dataInclusao": "2018-07-25T03:00:00.000+0000",
            "dataAlteracao": "2018-07-25T03:00:00.000+0000",
            "pagaComissao": self.pagaComissao,
            "pesoVariavel": self.pesoVariavel,
            "generoId": int(self.generoId),
            "situacaoFiscalId": self.situacaoFiscalId,
            "situacaoFiscalSaidaId": self.situacaoFiscalSaidaId,
            "localDeImpressaoId": self.localDeImpressaoId,
            "aplicacoesIds": self.aplicacacoesIds,
            "caracteristicasIds": self.caracteristicasIds,
            "regimesDoProduto": self.regimesDoProduto,
            "itensImpostosFederais": [
                {
                    "id": "01"
                },
                {
                    "id": "02"
                }
            ],
            "pautasDoProduto": self.pautasDoProduto,
            "estoqueDoProduto": self.estoquedoProduto
        }
        return ret_json

    def set_valor_padrao_api(self):
        pass



class Preco(object):
    def __init__(self, id_, idExterno, lojaId, produtoId, precoVenda1, precoOferta1, margemPreco1,
                 precoVenda2, precoOferta2, margemPreco2, quantidadeMinimaPreco2, precoVenda3,
                 precoOferta3, margemPreco3, quantidadeMinimaPreco3, descontoMaximo, permiteDesconto,
                 custoProduto=0, precoMedioDeReposicao='', precoFiscalDeReposicao='', incentivoEmZonaFranca=''):
        self.id_ = id_
        self.idExterno = idExterno
        self.lojaId = lojaId
        self.produtoId = produtoId
        self.precoVenda1 = precoVenda1
        self.precoOferta1 = precoOferta1
        self.margemPreco1 = margemPreco1
        self.precoVenda2 = precoVenda2
        self.precoOferta2 = precoOferta2
        self.margemPreco2 = margemPreco2
        self.quantidadeMinimaPreco2 = quantidadeMinimaPreco2
        self.precoVenda3 = precoVenda3
        self.precoOferta3 = precoOferta3
        self.margemPreco3 = margemPreco3
        self.quantidadeMinimaPreco3 = quantidadeMinimaPreco3
        self.descontoMaximo = descontoMaximo
        self.permiteDesconto = permiteDesconto
        self.custoProduto = custoProduto
        self.precoMedioDeReposicao = precoMedioDeReposicao
        self.precoFiscalDeReposicao = precoFiscalDeReposicao
        self.incentivoEmZonaFranca = incentivoEmZonaFranca


    def get_preco_venda_1(self):
        return self.precoVenda1

    def set_preco_venda_1(self, novo_preco):
        self.precoVenda1 = novo_preco

    def get_preco_venda_2(self):
        return self.precoVenda2

    def set_preco_venda_2(self, novo_preco):
        self.precoVenda2 = novo_preco

    def get_preco_venda_3(self):
        return self.precoVenda3

    def set_preco_venda_3(self, novo_preco):
        self.precoVenda3 = novo_preco

    def get_preco_oferta_1(self):
        return self.precoOferta1

    def set_preco_oferta_1(self, novo_preco):
        self.precoOferta1 = novo_preco

    def get_preco_oferta_2(self):
        return self.precoOferta2

    def set_preco_oferta_2(self, novo_preco):
        self.precoOferta2 = novo_preco

    def get_preco_oferta_3(self):
        return self.precoOferta3

    def set_preco_oferta_3(self, novo_preco):
        self.precoOferta3 = novo_preco

    def get_preco_margem_1(self):
        return self.margemPreco1

    def set_preco_margem_1(self, nova_margem):
        self.margemPreco1 = nova_margem

    def get_preco_margem_2(self):
        return self.margemPreco2

    def set_preco_margem_2(self, nova_margem):
        self.margemPreco2 = nova_margem

    def get_preco_margem_3(self):
        return self.margemPreco3

    def set_preco_margem_3(self, nova_margem):
        self.margemPreco3 = nova_margem

    def get_custo_produto(self):
        return self.custoProduto

    def set_custo_produto(self, novo_custo):
        self.custoProduto = novo_custo

    def to_string(self):
        print('Id: ', self.id_)
        print('ProdutoId: ', self.produtoId)
        print('LojaId: ', self.lojaId)
        print('Preço Venda 1: ', self.precoVenda1)
        print('Preço Oferta 1: ', self.precoOferta1)
        print('Preço Venda 2: ', self.precoVenda2)
        print('Preço Oferta 2: ', self.precoOferta2)
        print('Preço Venda 3: ', self.precoVenda3)
        print('Preço Oferta 3: ', self.precoOferta3)

    def to_json(self):
        ret_json = {
            "id": self.id_,
            "lojaId": self.lojaId,
            "produtoId": self.produtoId,
            "precoVenda1": str(self.precoVenda1),
            "precoOferta1": str(self.precoOferta1),
            "margemPreco1": str(self.margemPreco1),
            "precoVenda2": str(self.precoVenda2),
            "precoOferta2": str(self.precoOferta2),
            "margemPreco2": str(self.margemPreco2),
            "quantidadeMinimaPreco2": str(self.quantidadeMinimaPreco2),
            "precoVenda3": str(self.precoVenda3),
            "precoOferta3": str(self.precoOferta3),
            "margemPreco3": str(self.margemPreco3),
            "quantidadeMinimaPreco3": str(self.quantidadeMinimaPreco3),
            "dedscontoMaximo": str(self.descontoMaximo),
            "permiteDesconto": self.permiteDesconto
        }

        return ret_json


class CodigoAuxiliar():
    """
        id: int, PORÉM É O CÓDIGO AUXILIAR
        tipo: "LITERAL" OU "EAN"
        fator: fator multiplicador int
        produtoId: int, código do produto. PROCOD no syspdv.
    """
    def __init__(self, id_, idExterno, tipo, fator, produtoId):
        self.id_ = id_
        self.idExterno = idExterno
        self.tipo = tipo
        self.fator = fator
        self.produtoId = produtoId

    def to_json_full(self):

        ret_json = {
            "entity": {
                "id": str(self.id_),
                "idExterno": self.idExterno,
                "tipo": str(self.tipo),
                "fator": int(round(self.fator)),
                "produtoId": self.produtoId
                }
        }

        return ret_json

    def to_json(self):

        ret_json = {
            "entity": {
                "id": str(self.id_),
                "tipo": str(self.tipo),
                "fator": int(round(self.fator)),
                "produtoId": self.produtoId
                }
        }

        return ret_json

    def to_string(self):
        print('id_ (PROCODAUX):', self.id_)
        print('produtoId:', self.produtoId)
        print('fator: ', self.fator)
        print('tipo:', self.tipo)


class Secao():
    def __init__(self, id_, idExterno, descricao):
        self.id_ = id_
        self.idExterno = idExterno
        self.descricao = descricao

    def to_string(self):
        print('ID: ', self.id_)
        print('Descrição: ', self.descricao)

    def to_json(self):

        ret_json = {
            "id": str(self.id_),
            "descricao": str(self.descricao)
        }

        return ret_json

class Grupo():
    def __init__(self, id_, idExterno, descricao, secaoId):
        self.id_ = id_
        self.idExterno = idExterno
        self.descricao = descricao
        self.secaoId = secaoId

    def to_string(self):
        print('Id:', self.id_)
        print('descricao:', self.descricao)
        print('secaoId:', self.secaoId)

    def to_json(self):
        ret_json = {
            "id": str(self.id_),
            "descricao": str(self.descricao),
            "secaoId": str(self.secaoId)
        }
        return ret_json

class SubGrupo():
    def __init__(self, id_, idExterno, descricao, secaoId, grupoId):
        self.id_ = id_
        self.idExterno = idExterno
        self.descricao = descricao
        self.secaoId = secaoId
        self.grupoId = grupoId

    def to_string(self):
        print('Id:', self.id_)
        print('descricao:', self.descricao)
        print('secaoId:', self.secaoId)
        print('grupoId:', self.grupoId)

    def to_json(self):
        ret_json = {
            "id": str(self.id_),
            "descricao": str(self.descricao),
            "secaoId": str(self.secaoId),
            "grupoId": str(self.grupoId)
        }
        return ret_json



class ProdutoFornecedor():
    def __init__(self, id_, idExterno, fornecedorId, produtoId, referencia, unidade, quantidade, nivel):
        self.id_ = id_
        self.idExterno = idExterno
        self.fornecedorId = fornecedorId
        self.produtoId = produtoId
        self.referencia = referencia
        self.unidade = unidade
        self.quantidade = quantidade
        self.nivel = nivel

    def to_string(self):
        print('Id: ', self.id_)
        print('ProdutoId:', self.produtoId)
        print('Fornecedor Id:', self.fornecedorId)
        print('Referencia fornecedor:', self.referencia)
        print('Unidade:', self.unidade)
        print('Quantidade', self.quantidade)
        print('Nível:', self.nivel)

    def to_json(self, com_id=False):
        if com_id == True:
            ret_json = {
                "id": str(self.id_),
                "fornecedorId": str(self.fornecedorId),
                "produtoId": str(self.produtoId),
                "referencia": str(self.referencia),
                "unidade": str(self.unidade),
                "quantidade": str(self.quantidade),
                "nivel": str(self.nivel)
            }
        else:
            ret_json = {
                "fornecedorId": str(self.fornecedorId),
                "produtoId": str(self.produtoId),
                "referencia": str(self.referencia),
                "unidade": str(self.unidade),
                "quantidade": str(self.quantidade),
                "nivel": str(self.nivel)
            }

        return ret_json



