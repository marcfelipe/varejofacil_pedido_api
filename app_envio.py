from models.Client import Client
from models.Venda import Pedido, Despesas, EnderecoEntrega, Pagamento, ItemPedido
from controllers.VendaDAO import PedidoVendaDAO
from utils.common_functions import valida_none
import datetime
import pprint
import tomli

with open("config.toml", mode="rb") as fp:
    config = tomli.load(fp)

nome_servidor = config['nome_servidor']
local_banco = config['local_banco']
url_cliente = config['url_cliente']
client = Client(url_cliente, config['client_user'], config['client_pwd'])

client.get_token_API()

numero_pedido = input('Digite o número do pedido (digitar -1 encerra sem envio):\n')

while(int(numero_pedido)!= -1):
    arq_log = open('log_envio_pedidos.txt', 'w')
    pedido_dao = PedidoVendaDAO()
    pedido_bd = pedido_dao.listar_pedido_bd(numero_pedido, nome_servidor, local_banco)
    if pedido_bd is not None and len(pedido_bd)>0:
        lista_itens_envio = []
        pagamentos = []
        cep = pedido_bd[26]
        uf = pedido_bd[23]
        municipio = pedido_bd[22]
        logradouro = pedido_bd[20]
        numeroEndereco = valida_none(pedido_bd[24], '')
        bairro = pedido_bd[21]
        complemento =  valida_none(pedido_bd[25], '')
        pontoDeReferencia = ''
        endereco_entrega = EnderecoEntrega(cep, uf, municipio, logradouro, numeroEndereco,
                                           bairro, complemento, pontoDeReferencia)
        prefnz_bd = pedido_dao.listar_pre_finalizacao_pedido_bd(numero_pedido, nome_servidor, local_banco)
        if prefnz_bd is not None:
            formapagamentoId = int(prefnz_bd[1])
            dataVencimento = datetime.datetime.now().strftime('%Y-%m-%d')+"T04:00:00.000+0000"
            valor_pagamento = float(prefnz_bd[2])
            numeroParcelas = 1
            pago = False
            pagamento_pedido = Pagamento(formapagamentoId, dataVencimento, valor_pagamento, numeroParcelas, pago)
            pagamentos.append(pagamento_pedido.serialize(False))
        else:
            dataVencimento = datetime.datetime.now().strftime('%Y-%m-%d') + "T04:00:00.000+0000"
            valor_pagamento = float(pedido_bd[12])
            pagamento_pedido = Pagamento(1, dataVencimento, valor_pagamento, 1, False)
            pagamentos.append(pagamento_pedido.serialize(False))

#Criando a lista do objeto Item Pedido de Venda.
        lista_itens_bd = pedido_dao.listar_itens_pedido_bd(numero_pedido, nome_servidor, local_banco)
        if lista_itens_bd is not None:
            for item_pedido_bd in lista_itens_bd:
                produtoId = item_pedido_bd[3]
                unidade = str(item_pedido_bd[18]).strip()
                descricaoprodutoEcommerce = item_pedido_bd[16]
                quantidadeDeEmbalagem = float(item_pedido_bd[4])
                quantidadeDeItemEmbalagem = float(item_pedido_bd[14])
                quantidadeDeEmbalagemAtendida = float(item_pedido_bd[4])
                valorEmbalagem = float(item_pedido_bd[5])
                compoeValorTotal = True
                valor_total_item = float(quantidadeDeEmbalagem)*float(valorEmbalagem)
                valorDesconto = float(item_pedido_bd[6])
                if item_pedido_bd[7] == 'P':
                    tipoDesconto = 'PERCENTUAL'
                else:
                    tipoDesconto = 'VALOR'
                item_pedido_envio = ItemPedido(produtoId, unidade, descricaoprodutoEcommerce, quantidadeDeEmbalagem,
                                               quantidadeDeItemEmbalagem, quantidadeDeEmbalagemAtendida, valorEmbalagem,
                                               compoeValorTotal, valor_total_item, valorDesconto, tipoDesconto)
                lista_itens_envio.append(item_pedido_envio.serialize(False))
        lojaId = input('Digite o código da loja que irá entregar: \n')
        dataEmissao = pedido_bd[6].strftime('%Y-%m-%d')+"T04:00:00.000+0000"
        dataFaturamento = pedido_bd[6].strftime('%Y-%m-%d')+"T04:00:00.000+0000"
        dataEntrega = pedido_bd[33].strftime('%Y-%m-%d')+"T04:00:00.000+0000"
        dataPrevisao = pedido_bd[33].strftime('%Y-%m-%d')+"T04:00:00.000+0000"
        clienteId = int(pedido_bd[2])
        vendedorId = int(pedido_bd[1])
        pessoaAutorizadaRecebimento = ""
        retiradaNaLoja = False
        cpfNoCupom = False
        observacao = valida_none(pedido_bd[42], '')
        valorTotal = float(pedido_bd[12])
        valorLiquido = float(pedido_bd[12])
        status = 'ABERTO'
        if pedido_bd[32] is None:
            tipoDeFrete = 'SEM_FRETE'
        else:
            if pedido_bd[32] == 'CIF':
                tipoDeFrete = 'EMITENTE'
            else:
                tipoDeFrete = 'DESTINATARIO'
        if pedido_bd[29] == '2':
            tipoFaturamento = 'NOTA_FISCAL'
        else:
            tipoFaturamento = 'CUPOM_FISCAL'
        totalOutrasDespesas = float(pedido_bd[14])
        despesas = None
        enderecoEntrega = endereco_entrega      #facilitar a inicialização do objeto
        itens = lista_itens_envio               #facilitar a inicialização do objeto
        print('TIPO DE FATURAMENTO: ', tipoFaturamento)
        obj_pedido_envio = Pedido(numero_pedido, numero_pedido, lojaId, dataEmissao, dataFaturamento, dataEntrega,
                                  dataPrevisao, clienteId, vendedorId, pessoaAutorizadaRecebimento, retiradaNaLoja,
                                  cpfNoCupom, observacao, valorTotal, valorLiquido, status, tipoDeFrete,
                                  tipoFaturamento, totalOutrasDespesas, despesas, endereco_entrega.serialize(False),
                                  itens, pagamentos)
        ret_add_pedido = pedido_dao.salva_pedido_api(url_cliente, client.access_token, obj_pedido_envio.serialize())
        if ret_add_pedido == 401:
            client.get_token_API()
            pedido_dao.salva_pedido_api(url_cliente, client.access_token, obj_pedido_envio.serialize())
        elif ret_add_pedido.status_code == 409:
            arq_log.write('Erro 409 ocorrido para o produto: \n' + numero_pedido)
            arq_log.write('\n' + ret_add_pedido.text)
            arq_log.write('\n\n' + pprint.pformat(obj_pedido_envio.serialize(json_=False)) + '\n\n')
        elif ret_add_pedido.status_code == 422:
            arq_log.write('Erro 422 ocorrido para o produto: \n' + numero_pedido)
            arq_log.write('\n' + ret_add_pedido.text)
            arq_log.write('\n\n' + pprint.pformat(obj_pedido_envio.serialize(json_=False)) + '\n\n')
        elif ret_add_pedido.status_code == 400:
            arq_log.write('Erro 400 ocorrido para o produto: \n' + numero_pedido)
            arq_log.write('\n' + ret_add_pedido.text)
            arq_log.write('\n\n' + pprint.pformat(obj_pedido_envio.serialize(json_=False)) + '\n\n')
        elif ret_add_pedido.status_code == 500:
            arq_log.write('Erro 500 ocorrido para o produto: \n' + numero_pedido)
            arq_log.write('\n' + ret_add_pedido.text)
            arq_log.write('\n\n' + pprint.pformat(obj_pedido_envio.serialize()) + '\n\n')
        elif ret_add_pedido.status_code != 201:
            print('Envio do pedido {} concluído'.format(numero_pedido))
            print('Pedido enviado com sucesso!\n')

    else:
        print('Número de pedido inválido\n')
    arq_log.close()
    numero_pedido = input('Digite o número do pedido (digitar -1 encerra sem envio):\n')

