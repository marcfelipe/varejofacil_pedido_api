
def gera_situacao_fiscal(trbid):
    if trbid == 'F00':
        situacaoFiscalId = 1
    elif trbid == 'I00':
        situacaoFiscalId = 2
    elif trbid == 'N00':
        situacaoFiscalId = 3
    elif trbid == 'T07':
        situacaoFiscalId = 4
    elif trbid == 'T08':
        situacaoFiscalId = 5
    elif trbid == 'T12':
        situacaoFiscalId = 6
    elif trbid == 'T17':
        situacaoFiscalId = 7
    elif trbid == 'T18':
        situacaoFiscalId = 8
    elif trbid == 'T25':
        situacaoFiscalId = 9
    elif trbid == 'T27':
        situacaoFiscalId = 10
    else:
        situacaoFiscalId = 1
    return situacaoFiscalId

def gera_situacao_fiscal_toyoda(trbid):
    if trbid == 'F00':
        situacaoFiscalId = 1
    elif trbid == 'F10':
        situacaoFiscalId = 2
    elif trbid == 'F61':
        situacaoFiscalId = 3
    elif trbid == 'I00':
        situacaoFiscalId = 4
    elif trbid == 'N00':
        situacaoFiscalId = 5
    elif trbid == 'N01':
        situacaoFiscalId = 6
    elif trbid == 'S01':
        situacaoFiscalId = 7
    elif trbid == 'T04':
        situacaoFiscalId = 8
    elif trbid == 'T05':
        situacaoFiscalId = 9
    elif trbid == 'T07':
        situacaoFiscalId = 10
    elif trbid == 'T08':
        situacaoFiscalId = 11
    elif trbid == 'T11':
        situacaoFiscalId = 12
    elif trbid == 'T12':
        situacaoFiscalId = 13
    elif trbid == 'T17':
        situacaoFiscalId = 14
    elif trbid == 'T18':
        situacaoFiscalId = 15
    elif trbid == 'T20':
        situacaoFiscalId = 16
    elif trbid == 'T21':
        situacaoFiscalId = 17
    elif trbid == 'T22':
        situacaoFiscalId = 18
    elif trbid == 'T25':
        situacaoFiscalId = 19
    elif trbid == 'T27':
        situacaoFiscalId = 20
    elif trbid == 'T50':
        situacaoFiscalId = 21
    elif trbid == 'T90':
        situacaoFiscalId = 22
    else:
        situacaoFiscalId = 1
    return situacaoFiscalId

def gera_situacao_fiscal_DOR(trbid):
    if trbid == 'F00':
        situacaoFiscalId = 1
    elif trbid == 'I00':
        situacaoFiscalId = 2
    elif trbid == 'N00':
        situacaoFiscalId = 5
    elif trbid == 'T07':
        situacaoFiscalId = 3
    elif trbid == 'T18':
        situacaoFiscalId = 4
    else:
        situacaoFiscalId = 1
    return situacaoFiscalId

def gera_situacao_fiscal_frigoum(trbid):
    if trbid == 'F00':
        situacaoFiscalId = 1
    elif trbid == 'T18':
        situacaoFiscalId = 2
    elif trbid == 'T30':
        situacaoFiscalId = 3
    elif trbid == 'T07':
        situacaoFiscalId = 4
    elif trbid == 'I00':
        situacaoFiscalId = 5
    else:
        situacaoFiscalId = 1
    return situacaoFiscalId

def list_to_string(list_content):
    ret_string = ""
    for line in list_content:
        if line == list_content[-1]:
            ret_string = ret_string+line
        else:
            ret_string = ret_string+line+','
    return ret_string

def valida_none(var_analise, valor_default):
    if var_analise is not None:
        return var_analise
    else:
        return valor_default
def valida_preenchido(var_analise, valor_default):
    if var_analise is not None:
        if valor_default == '' and var_analise.strip() == '':
            return valor_default
        elif var_analise.strip() == '' and valor_default != '':
            return valor_default
        else:
            return var_analise
    else:
        return valor_default

def valida_telefone(var_analise, valor_default):
    if var_analise is not None:
        if valor_default == '' and var_analise.strip() == '':
            valor_resultado = valor_default
        elif var_analise.strip() == '' and valor_default != '':
            valor_resultado = valor_default
        else:
            valor_resultado = var_analise
            if len(valor_resultado)>11:
                valor_resultado = valor_resultado[:10]
    else:
        valor_resultado = valor_default
    return str(valor_resultado).replace(' ','').replace('(', '').replace(')', '').replace('-', '').zfill(11)


def set_default(var_analise, valor_esperado, retorno_esperado, retorno_padrao):
    if var_analise == valor_esperado:
        return retorno_esperado
    else:
        return retorno_padrao

def evita_vazio(var_analise, valor_padrao):
    if var_analise.strip() == '':
        return valor_padrao
    else:
        return var_analise

false = False
true = True

json_produto_teste ={
    "id": 100000,
    "secaoId": 1,
    "naturezaDeImpostoFederalId": 999,
    "diasDeSeguranca": 0,
    "descricao": "BOBINA DE PAPEL KG",
    "descricaoReduzida": "BOBINA DE PAPEL KG",
    "controlaNumeroSerie": false,
    "tabelaA": "NACIONAL",
    "tipoBonificacao": "NAO_GERA_PONTOS",
    "controlaEstoque": true,
    "associacao": "NORMAL",
    "composicao": "NORMAL",
    "controlaValidade": false,
    "enviaBalanca": false,
    "foraDeLinha": "N",
    "unidadeDeCompra": "KG",
    "tipoIPI": "PERCENTUAL",
    "precoVariavel": false,
    "indiceAT": "ARREDONDA",
    "producao": "TERCEIROS",
    "nomeclaturaMercosulId": "84393010",
    "nomeclaturaMercosulExcecaoId": "00",
    "finalidadeProduto": "MATERIA_PRIMA",
    "incentivoZonaFranca": "S",
    "altura": "",
    "largura": "",
    "comprimento": "",
    "unidadeDeVenda": "KG",
    "permiteDesconto": false,
    "compoeTotalDaNota": true,
    "ativoNoEcommerce": false,
    "atualizaFamilia": false,
    "frenteLoja": false,
    "itensEmbalagem": 1,
    "itensEmbalagemVenda": 1,
    "itensEmbalagemTransferencia": 1,
    "dataInclusao": "2018-07-25T03:00:00.000+0000",
    "dataAlteracao": "2018-07-25T10:51:13.831+0000",
    "pagaComissao": false,
    "pesoVariavel": "NAO",
    "generoId": 84,
    "situacaoFiscalId": 2,
    "situacaoFiscalSaidaId": 2,
    "localDeImpressaoId": 0,
    "aplicacoesIds": [],
    "caracteristicasIds": [],
    "regimesDoProduto": [],
    "itensImpostosFederais": [
        {
            "id": "01"
        },
        {
            "id": "02"
        }
    ],
    "pautasDoProduto": [],
    "estoqueDoProduto": []
}

json_auxiliar2 = {"items": [{"entity": {"fator": 1,
                       "id": "07891000071700",
                       "idExterno": "",
                       "produtoId": "00000000003317",
                       "tipo": "LITERAL"}},
           {"entity": {"fator": 1,
                       "id": "07891000011447",
                       "idExterno": "",
                       "produtoId": "00000000003317",
                       "tipo": "EAN"}}]}

json_auxiliar =  {"items": [{"entity": {"fator": 1,
                       "id": "07891000071700",
                       "idExterno": "",
                       "produtoId": "00000000003317",
                       "tipo": "LITERAL"}}]}


json_fornecedor_rtorno = {
            "id": 4,
            "tipoDeFornecedor": "DISTRIBUIDORA",
            "prazoDeEntrega": 0,
            "tipoDeFrete": "EMITENTE",
            "servico": false,
            "regimeEstadualTributarioId": 1,
            "produtorRural": false,
            "numeroDoDocumento": "59717553000617",
            "numeroDeIdentificacao": "2513474170045",
            "tipoContribuinte": "CONTRIBUINTE",
            "nome": "MULTILASER INDUSTRIAL S.A.",
            "fantasia": "MULTILASER ",
            "telefone1": "55353435750",
            "telefone2": "",
            "email": "gislaine.santos@multilaser.com.br",
            "endereco": {
                "codigoIbge": 3125101,
                "municipio": "EXTREMA",
                "cep": "37640-000",
                "uf": "MG",
                "logradouro": "RUA JOSEFA GOMES DE SOUZA",
                "numero": "382",
                "bairro": "BAIRRO DOS PIRES",
                "tipoDeEndereco": "PRINCIPAL",
                "codigoDoPais": 1058
            },
            "tipoDePessoa": "JURIDICA",
            "holdingId": 1
        },

envio_sjson = {}

sql_correcao_telefone = """update fornecedor 
                        set fortel= replace(replace(replace(fortel,'(','0'), ')',''),'-','')"""

