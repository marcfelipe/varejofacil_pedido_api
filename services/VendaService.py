import requests
import json

class PedidoVendaService(object):
    @classmethod
    def get_pedidos(cls, url, access_token, inicio=0, contador=0):
        headers = {'authorization': access_token}
        params = {'sort': 'id', 'start': inicio, 'count': contador}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/venda/pedidos"
        url_api = url + url_funcao
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers, params=params)
        print(req.status_code)
        if req.status_code == 200:
            resultado = json.loads(req.text)
            print('lista dos pedidos!\n')
            contagem = 0
            for item in resultado['items']:
                #print(item['id'], '\n')
                #print(item)
                lista_resultado.append(item)
                contagem += 1
            print('total de itens: ', str(contagem))
            return lista_resultado
        else:
            return None

    @classmethod
    def get_pedido_por_id(cls, url, access_token, id_pedido):
        headers = {'authorization': access_token}
        # params = {'id': id_produto}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/venda/pedidos/"  # aceita auxiliar
        url_api = url + url_funcao + str(id_pedido)
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers)
        print(req.status_code)
        if req.status_code == 200:
            resultado = json.loads(req.text)
            print('lista dos itens!\n')
            return resultado
        else:
            return None

    @classmethod
    def get_atendimentos_pedido(cls):
        pass

    @classmethod
    def post_add_pedido(cls, url, access_token, pedido_json):
        headers = {'authorization': access_token, 'content-type': 'application/json'}
        #data_sent = json.dumps(pedido_json)   alterado, pois utilizo json.dumps em model.Pedido.to_json()
        data_sent = pedido_json
        url_funcao = "/api/v1/venda/pedidos"
        url_api = url + url_funcao
        print('Iniciando inclusão, executando post na url:\n', url_api)
        #print('pedido_json:\n', pedido_json)
        req = requests.post(url_api, data=data_sent, headers=headers)
        print("Resultado: ", req.status_code)
        if req.status_code != 201:
            print('retorno:\n')
            print(req.text)
        ret = req
        req.close()
        return ret


    @classmethod
    def post_cancela_pedido(cls):
        pass


