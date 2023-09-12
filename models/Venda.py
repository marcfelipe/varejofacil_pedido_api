import json

class Despesas(object):
    def __init__(self, valorEntrega, valorDelivery, valorRetirada, valorConveniencia):
        self.valorEntrega = valorEntrega
        self.valorDelivery = valorDelivery
        self.valorRetirada = valorRetirada
        self.valorConveniencia = valorConveniencia

    def to_string(self):
        print('valorEntrega:', self.valorEntrega)
        print('valorDelivery:', self.valorDelivery)
        print('valorRetirada:', self.valorRetirada)
        print('valorConvenieencia:', self.valorConveniencia)

    def serialize(self, json_=True):
        dict_despesas = {}
        dict_despesas['valorEntrega'] = self.valorEntrega
        dict_despesas['valorDelivery'] = self.valorDelivery
        dict_despesas['valorRetirada'] = self.valorRetirada
        dict_despesas['valorConveniencia'] = self.valorConveniencia
        if json_:
            return json.dumps(dict_despesas)
        else:
            return dict_despesas


class EnderecoEntrega(object):
    def __init__(self, cep, uf, municipio, logradouro, numeroEndereco, bairro, complemento, pontoDeReferencia):
        self.cep = cep
        self.uf = uf
        self.municipio = municipio
        self.logradouro = logradouro
        self.numeroEndereco = numeroEndereco
        self.bairro = bairro
        self.complemento = complemento
        self.pontoDeReferencia = pontoDeReferencia

    def serialize(self, json_=True):
        dict_endereco = {}
        dict_endereco['cep'] = self.cep
        dict_endereco['uf'] = self.uf
        dict_endereco['municipio'] = self.municipio
        dict_endereco['logradouro'] = self.logradouro
        dict_endereco['numeroEndereco'] = self.numeroEndereco
        dict_endereco['bairro'] = self.bairro
        dict_endereco['complemento'] = self.complemento
        dict_endereco['pontoDeReferencia'] = self.pontoDeReferencia
        if json_:
            return json.dumps(dict_endereco)
        else:
            return dict_endereco



class ItemPedido(object):
    def __init__(self, produtoId, unidade, descricaoProdutoEcommerce, quantidadeDeEmbalagem, quantidadeDeItemEmbalagem,
                 quantidadeDeEmbalagemAtendida, valorEmbalagem, compoeValorTotal, valor,
                 valorDesconto, tipoDesconto):
        self.produtoId = produtoId
        self.unidade = unidade
        self.descricaoProdutoEcommerce = descricaoProdutoEcommerce
        self.quantidadeDeEmbalagem = quantidadeDeEmbalagem
        self.quantidadeDeItemEmbalagem = quantidadeDeItemEmbalagem
        self.quantidadeDeEmbalagemAtendida = quantidadeDeEmbalagemAtendida
        self.valorEmbalagem = valorEmbalagem
        self.compoeValorTotal = compoeValorTotal
        self.valor = valor
        self.valorDesconto = valorDesconto
        self.tipoDesconto = tipoDesconto

    def serialize(self, json_=True):
        dict_item = {}
        dict_item['produtoId'] = int(self.produtoId)
        dict_item['unidade'] = self.unidade
        dict_item['descricaoProdutoEcommerce'] = self.descricaoProdutoEcommerce
        dict_item['quantidadeDeEmbalagem'] = "{:.2f}".format(float(self.quantidadeDeEmbalagem))
        dict_item['quantidadeDeItemEmbalagem'] = "{:.2f}".format(float(self.quantidadeDeItemEmbalagem))
        dict_item['quantidadeDeEmbalagemAtendida'] = "{:.2f}".format(float(self.quantidadeDeEmbalagemAtendida))
        dict_item['valorEmbalagem'] = "{:.2f}".format(float(self.valorEmbalagem))
        dict_item['compoeValorTotal'] = self.compoeValorTotal
        dict_item['valor'] = "{:.2f}".format(float(self.valor))
        dict_item['valorDesconto'] = "{:.2f}".format(float(self.valorDesconto))
        dict_item['tipoDesconto'] = self.tipoDesconto
        if json_:
            return json.dumps(dict_item)
        else:
            return dict_item


class Pagamento(object):
    def __init__(self, formaPagamentoId, dataVencimento, valor, numeroParcelas, pago):
        self.formaPagamentoId = formaPagamentoId
        self.dataVencimento = dataVencimento
        self.valor = "{:.2f}".format(float(valor))
        self.numeroParcelas = numeroParcelas
        self.pago = pago

    def serialize(self, json_=True):
        dict_pagamento = {}
        dict_pagamento['formaPagamentoId'] = int(self.formaPagamentoId)
        dict_pagamento['dataVencimento'] = self.dataVencimento
        dict_pagamento['valor'] = "{:.2f}".format(float(self.valor))
        dict_pagamento['numeroParcelas'] = self.numeroParcelas
        dict_pagamento['pago'] = self.pago
        if json_:
            return json.dumps(dict_pagamento)
        else:
            return dict_pagamento

class Pedido(object):
    """
     id não deve ser enviado. O número do pedido deve ser enviado em idExterno
     status: [ ABERTO, ACEITE, RECUSADO, EM_FATURAMENTO, FATURADO, ENTREGUE, CANCELADO ]
     frete: [ EMITENTE, DESTINATARIO, TERCEIRO, EMITENTE_PROPRIO, DESTINATARIO_PROPRIO, SEM_FRETE ]
     tipoFrete: [ CUPOM_FISCAL, NOTA_FISCAL ]

    """
    def __init__(self, id, idExterno, lojaId, dataEmissao, dataFaturamento, dataEntrega, dataPrevisao, clienteId,
                 vendedorId, pessoaAutorizadaRecebimento, retiradaNaLoja, cpfNoCupom, observacao, valorTotal,
                 valorLiquido, status, tipoDeFrete, tipoFaturamento, totalOutrasDespesas, despesas,
                 enderecoEntrega, itens, pagamentos):
        self.id = id
        self.idExterno = idExterno
        self.lojaId = lojaId
        self.dataEmissao = dataEmissao
        self.dataFaturamento = dataFaturamento
        self.dataEntrega = dataEntrega
        self.dataPrevisao = dataPrevisao
        self.clienteId = clienteId
        self.vendedorId = vendedorId
        self.pessoaAutorizadaRecebimento = pessoaAutorizadaRecebimento
        self.retiradaNaLoja = retiradaNaLoja
        self.cpfNoCupom = cpfNoCupom
        self.observacao = observacao
        self.valorTotal = valorTotal
        self.valorLiquido = valorLiquido
        self.status = status
        self.tipoDeFrete = tipoDeFrete
        self.tipoFaturamento = tipoFaturamento
        self.totalOutrasDespesas = totalOutrasDespesas
        self.despesas = despesas
        self.enderecoEntrega = enderecoEntrega
        self.itens = itens
        self.pagamentos = pagamentos

    def to_string(self):
        print('Número Pedido:', self.idExterno)
        print('Cliente:', self.clienteId)
        print('Valor do Pedido:', self.valorTotal)

    def serialize(self, json_=True, envia_despesa=False):
        pedido = {}
        #pedido['idExterno'] = self.idExterno
        pedido['lojaId'] = self.lojaId
        pedido['dataEmissao'] = self.dataEmissao
        pedido['dataFaturamento'] = self.dataFaturamento
        pedido['dataEntrega'] = self.dataEntrega
        pedido['dataPrevisao'] = self.dataEntrega
        pedido['clienteId'] = self.clienteId
        pedido['vendedorId'] = self.vendedorId
        pedido['pessoaAutorizadaRecebimento'] = self.pessoaAutorizadaRecebimento
        pedido['retiradaNaLoja'] = self.retiradaNaLoja
        pedido['cpfNoCupom'] = self.cpfNoCupom
        pedido['observacao'] = self.observacao
        pedido['valorTotal'] = "{:.2f}".format(float(self.valorTotal))
#        pedido['valorLiquido'] = "{:.2f}".format(float(self.valorLiquido))
        pedido['status'] = self.status
        pedido['tipoDeFrete'] = self.tipoDeFrete
        pedido['tipoFaturamento'] = self.tipoFaturamento
        pedido['totalOutrasDespesas'] = "{:.2f}".format(float(self.totalOutrasDespesas))
        if envia_despesa:
            pedido['despesas'] = self.despesas
        pedido['enderecoEntrega'] = self.enderecoEntrega
        pedido['itens'] = self.itens
        pedido['pagamentos'] = self.pagamentos
        if json_:
            return json.dumps(pedido)
        else:
            return pedido


"""

########copiado do site, modificar
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = Pedidofromdict(json.loads(json_string))

from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Despesas:
    valorEntrega: int
    valorDelivery: int
    valorRetirada: int
    valorConveniencia: int

    def __init__(self, valorEntrega: int, valorDelivery: int, valorRetirada: int, valorConveniencia: int) -> None:
        self.valorEntrega = valorEntrega
        self.valorDelivery = valorDelivery
        self.valorRetirada = valorRetirada
        self.valorConveniencia = valorConveniencia

    @staticmethod
    def from_dict(obj: Any) -> 'Despesas':
        assert isinstance(obj, dict)
        valorEntrega = from_int(obj.get("valorEntrega"))
        valorDelivery = from_int(obj.get("valorDelivery"))
        valorRetirada = from_int(obj.get("valorRetirada"))
        valorConveniencia = from_int(obj.get("valorConveniencia"))
        return Despesas(valorEntrega, valorDelivery, valorRetirada, valorConveniencia)

    def to_dict(self) -> dict:
        result: dict = {}
        result["valorEntrega"] = from_int(self.valorEntrega)
        result["valorDelivery"] = from_int(self.valorDelivery)
        result["valorRetirada"] = from_int(self.valorRetirada)
        result["valorConveniencia"] = from_int(self.valorConveniencia)
        return result


class EnderecoEntrega:
    cep: str
    uf: str
    municipio: str
    logradouro: str
    numeroEndereco: str
    bairro: str
    complemento: str
    pontoDeReferencia: str

    def __init__(self, cep: str, uf: str, municipio: str, logradouro: str, numeroEndereco: str, bairro: str, complemento: str, pontoDeReferencia: str) -> None:
        self.cep = cep
        self.uf = uf
        self.municipio = municipio
        self.logradouro = logradouro
        self.numeroEndereco = numeroEndereco
        self.bairro = bairro
        self.complemento = complemento
        self.pontoDeReferencia = pontoDeReferencia

    @staticmethod
    def from_dict(obj: Any) -> 'EnderecoEntrega':
        assert isinstance(obj, dict)
        cep = from_str(obj.get("cep"))
        uf = from_str(obj.get("uf"))
        municipio = from_str(obj.get("municipio"))
        logradouro = from_str(obj.get("logradouro"))
        numeroEndereco = from_str(obj.get("numeroEndereco"))
        bairro = from_str(obj.get("bairro"))
        complemento = from_str(obj.get("complemento"))
        pontoDeReferencia = from_str(obj.get("pontoDeReferencia"))
        return EnderecoEntrega(cep, uf, municipio, logradouro, numeroEndereco, bairro, complemento, pontoDeReferencia)

    def to_dict(self) -> dict:
        result: dict = {}
        result["cep"] = from_str(self.cep)
        result["uf"] = from_str(self.uf)
        result["municipio"] = from_str(self.municipio)
        result["logradouro"] = from_str(self.logradouro)
        result["numeroEndereco"] = from_str(self.numeroEndereco)
        result["bairro"] = from_str(self.bairro)
        result["complemento"] = from_str(self.complemento)
        result["pontoDeReferencia"] = from_str(self.pontoDeReferencia)
        return result


class Iten:
    produtoId: int
    unidade: str
    descricaoProdutoEcommerce: str
    quantidadeDeEmbalagem: int
    quantidadeDeItemEmbalagem: int
    quantidadeDeEmbalagemAtendida: int
    valorEmbalagem: int
    compoeValorTotal: bool
    valor: int
    valorDesconto: int
    tipoDesconto: str

    def __init__(self, produtoId: int, unidade: str, descricaoProdutoEcommerce: str, quantidadeDeEmbalagem: int, quantidadeDeItemEmbalagem: int, quantidadeDeEmbalagemAtendida: int, valorEmbalagem: int, compoeValorTotal: bool, valor: int, valorDesconto: int, tipoDesconto: str) -> None:
        self.produtoId = produtoId
        self.unidade = unidade
        self.descricaoProdutoEcommerce = descricaoProdutoEcommerce
        self.quantidadeDeEmbalagem = quantidadeDeEmbalagem
        self.quantidadeDeItemEmbalagem = quantidadeDeItemEmbalagem
        self.quantidadeDeEmbalagemAtendida = quantidadeDeEmbalagemAtendida
        self.valorEmbalagem = valorEmbalagem
        self.compoeValorTotal = compoeValorTotal
        self.valor = valor
        self.valorDesconto = valorDesconto
        self.tipoDesconto = tipoDesconto

    @staticmethod
    def from_dict(obj: Any) -> 'Iten':
        assert isinstance(obj, dict)
        produtoId = from_int(obj.get("produtoId"))
        unidade = from_str(obj.get("unidade"))
        descricaoProdutoEcommerce = from_str(obj.get("descricaoProdutoEcommerce"))
        quantidadeDeEmbalagem = from_int(obj.get("quantidadeDeEmbalagem"))
        quantidadeDeItemEmbalagem = from_int(obj.get("quantidadeDeItemEmbalagem"))
        quantidadeDeEmbalagemAtendida = from_int(obj.get("quantidadeDeEmbalagemAtendida"))
        valorEmbalagem = from_int(obj.get("valorEmbalagem"))
        compoeValorTotal = from_bool(obj.get("compoeValorTotal"))
        valor = from_int(obj.get("valor"))
        valorDesconto = from_int(obj.get("valorDesconto"))
        tipoDesconto = from_str(obj.get("tipoDesconto"))
        return Iten(produtoId, unidade, descricaoProdutoEcommerce, quantidadeDeEmbalagem, quantidadeDeItemEmbalagem, quantidadeDeEmbalagemAtendida, valorEmbalagem, compoeValorTotal, valor, valorDesconto, tipoDesconto)

    def to_dict(self) -> dict:
        result: dict = {}
        result["produtoId"] = from_int(self.produtoId)
        result["unidade"] = from_str(self.unidade)
        result["descricaoProdutoEcommerce"] = from_str(self.descricaoProdutoEcommerce)
        result["quantidadeDeEmbalagem"] = from_int(self.quantidadeDeEmbalagem)
        result["quantidadeDeItemEmbalagem"] = from_int(self.quantidadeDeItemEmbalagem)
        result["quantidadeDeEmbalagemAtendida"] = from_int(self.quantidadeDeEmbalagemAtendida)
        result["valorEmbalagem"] = from_int(self.valorEmbalagem)
        result["compoeValorTotal"] = from_bool(self.compoeValorTotal)
        result["valor"] = from_int(self.valor)
        result["valorDesconto"] = from_int(self.valorDesconto)
        result["tipoDesconto"] = from_str(self.tipoDesconto)
        return result


class Pagamento:
    formaPagamentoId: int
    dataVencimento: str
    valor: int
    numeroParcelas: int
    pago: bool

    def __init__(self, formaPagamentoId: int, dataVencimento: str, valor: int, numeroParcelas: int, pago: bool) -> None:
        self.formaPagamentoId = formaPagamentoId
        self.dataVencimento = dataVencimento
        self.valor = valor
        self.numeroParcelas = numeroParcelas
        self.pago = pago

    @staticmethod
    def from_dict(obj: Any) -> 'Pagamento':
        assert isinstance(obj, dict)
        formaPagamentoId = from_int(obj.get("formaPagamentoId"))
        dataVencimento = from_str(obj.get("dataVencimento"))
        valor = from_int(obj.get("valor"))
        numeroParcelas = from_int(obj.get("numeroParcelas"))
        pago = from_bool(obj.get("pago"))
        return Pagamento(formaPagamentoId, dataVencimento, valor, numeroParcelas, pago)

    def to_dict(self) -> dict:
        result: dict = {}
        result["formaPagamentoId"] = from_int(self.formaPagamentoId)
        result["dataVencimento"] = from_str(self.dataVencimento)
        result["valor"] = from_int(self.valor)
        result["numeroParcelas"] = from_int(self.numeroParcelas)
        result["pago"] = from_bool(self.pago)
        return result


class Pedido:
    id: int
    idExterno: str
    lojaId: int
    dataEmissao: str
    dataFaturamento: str
    dataEntrega: str
    dataPrevisao: str
    clienteId: int
    vendedorId: int
    pessoaAutorizadaRecebimento: str
    retiradaNaLoja: bool
    cpfNoCupom: bool
    observacao: str
    valorTotal: int
    valorLiquido: int
    status: str
    tipoDeFrete: str
    tipoFaturamento: str
    totalOutrasDespesas: int
    despesas: Despesas
    enderecoEntrega: EnderecoEntrega
    itens: List[Iten]
    pagamentos: List[Pagamento]

    def __init__(self, id: int, idExterno: str, lojaId: int, dataEmissao: str, dataFaturamento: str, dataEntrega: str, dataPrevisao: str, clienteId: int, vendedorId: int, pessoaAutorizadaRecebimento: str, retiradaNaLoja: bool, cpfNoCupom: bool, observacao: str, valorTotal: int, valorLiquido: int, status: str, tipoDeFrete: str, tipoFaturamento: str, totalOutrasDespesas: int, despesas: Despesas, enderecoEntrega: EnderecoEntrega, itens: List[Iten], pagamentos: List[Pagamento]) -> None:
        self.id = id
        self.idExterno = idExterno
        self.lojaId = lojaId
        self.dataEmissao = dataEmissao
        self.dataFaturamento = dataFaturamento
        self.dataEntrega = dataEntrega
        self.dataPrevisao = dataPrevisao
        self.clienteId = clienteId
        self.vendedorId = vendedorId
        self.pessoaAutorizadaRecebimento = pessoaAutorizadaRecebimento
        self.retiradaNaLoja = retiradaNaLoja
        self.cpfNoCupom = cpfNoCupom
        self.observacao = observacao
        self.valorTotal = valorTotal
        self.valorLiquido = valorLiquido
        self.status = status
        self.tipoDeFrete = tipoDeFrete
        self.tipoFaturamento = tipoFaturamento
        self.totalOutrasDespesas = totalOutrasDespesas
        self.despesas = despesas
        self.enderecoEntrega = enderecoEntrega
        self.itens = itens
        self.pagamentos = pagamentos

    @staticmethod
    def from_dict(obj: Any) -> 'Pedido':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        idExterno = from_str(obj.get("idExterno"))
        lojaId = from_int(obj.get("lojaId"))
        dataEmissao = from_str(obj.get("dataEmissao"))
        dataFaturamento = from_str(obj.get("dataFaturamento"))
        dataEntrega = from_str(obj.get("dataEntrega"))
        dataPrevisao = from_str(obj.get("dataPrevisao"))
        clienteId = from_int(obj.get("clienteId"))
        vendedorId = from_int(obj.get("vendedorId"))
        pessoaAutorizadaRecebimento = from_str(obj.get("pessoaAutorizadaRecebimento"))
        retiradaNaLoja = from_bool(obj.get("retiradaNaLoja"))
        cpfNoCupom = from_bool(obj.get("cpfNoCupom"))
        observacao = from_str(obj.get("observacao"))
        valorTotal = from_int(obj.get("valorTotal"))
        valorLiquido = from_int(obj.get("valorLiquido"))
        status = from_str(obj.get("status"))
        tipoDeFrete = from_str(obj.get("tipoDeFrete"))
        tipoFaturamento = from_str(obj.get("tipoFaturamento"))
        totalOutrasDespesas = from_int(obj.get("totalOutrasDespesas"))
        despesas = Despesas.from_dict(obj.get("despesas"))
        enderecoEntrega = EnderecoEntrega.from_dict(obj.get("enderecoEntrega"))
        itens = from_list(Iten.from_dict, obj.get("itens"))
        pagamentos = from_list(Pagamento.from_dict, obj.get("pagamentos"))
        return Pedido(id, idExterno, lojaId, dataEmissao, dataFaturamento, dataEntrega, dataPrevisao, clienteId, vendedorId, pessoaAutorizadaRecebimento, retiradaNaLoja, cpfNoCupom, observacao, valorTotal, valorLiquido, status, tipoDeFrete, tipoFaturamento, totalOutrasDespesas, despesas, enderecoEntrega, itens, pagamentos)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["idExterno"] = from_str(self.idExterno)
        result["lojaId"] = from_int(self.lojaId)
        result["dataEmissao"] = from_str(self.dataEmissao)
        result["dataFaturamento"] = from_str(self.dataFaturamento)
        result["dataEntrega"] = from_str(self.dataEntrega)
        result["dataPrevisao"] = from_str(self.dataPrevisao)
        result["clienteId"] = from_int(self.clienteId)
        result["vendedorId"] = from_int(self.vendedorId)
        result["pessoaAutorizadaRecebimento"] = from_str(self.pessoaAutorizadaRecebimento)
        result["retiradaNaLoja"] = from_bool(self.retiradaNaLoja)
        result["cpfNoCupom"] = from_bool(self.cpfNoCupom)
        result["observacao"] = from_str(self.observacao)
        result["valorTotal"] = from_int(self.valorTotal)
        result["valorLiquido"] = from_int(self.valorLiquido)
        result["status"] = from_str(self.status)
        result["tipoDeFrete"] = from_str(self.tipoDeFrete)
        result["tipoFaturamento"] = from_str(self.tipoFaturamento)
        result["totalOutrasDespesas"] = from_int(self.totalOutrasDespesas)
        result["despesas"] = to_class(Despesas, self.despesas)
        result["enderecoEntrega"] = to_class(EnderecoEntrega, self.enderecoEntrega)
        result["itens"] = from_list(lambda x: to_class(Iten, x), self.itens)
        result["pagamentos"] = from_list(lambda x: to_class(Pagamento, x), self.pagamentos)
        return result


def Pedidofromdict(s: Any) -> Pedido:
    return Pedido.from_dict(s)


def Pedidotodict(x: Pedido) -> Any:
    return to_class(Pedido, x)


"""