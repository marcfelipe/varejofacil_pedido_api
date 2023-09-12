import requests, json


class EspecieDocumentoService(object):
    def __init__(self):
        pass

    @classmethod
    def get_especies_documento(cls, url, access_token, inicio=0, contador=0):
        headers = {'authorization': access_token}
        params = {'sort': 'id', 'start': inicio, 'count': contador}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/financeiro/especies-documentos"
        url_api = url + url_funcao
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers, params=params)
        print(req.status_code)
        if req.status_code == 200:
            resultado = json.loads(req.text)
            print('lista de especies!\n')
            contagem = 0
            for item in resultado['items']:
                # print(item['id'], '\n')
                # print(item)
                lista_resultado.append(item)
                contagem += 1
            print('total de itens: ', str(contagem))
            return lista_resultado
        else:
            return None

    @classmethod
    def post_add_especie_documento(cls, url, access_token, auxiliar_json):
        headers = {'authorization': access_token, 'content-type': 'application/json'}
        data_sent = json.dumps(auxiliar_json)
        url_funcao = "/api/v1/financeiro/especies-documentos"
        url_api = url + url_funcao
        print('Iniciando inclusão, executando post na url:\n', url_api)
        req = requests.post(url_api, data=data_sent, headers=headers)
        print("Resultado: ", req.status_code)
        if req.status_code != 201:
            print('retorno:\n')
            print(req.text)
        ret = req
        req.close()
        return ret

class FormaPagamentoService(object):
    def __init__(self):
        pass

    @classmethod
    def get_formas_de_pagamento(cls, url, access_token, inicio=0, contador=0):
        headers = {'authorization': access_token}
        params = {'sort': 'id', 'start': inicio, 'count': contador}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/financeiro/formas-pagamento"
        url_api = url + url_funcao
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers, params=params)
        print(req.status_code)
        if req.status_code == 200:
            resultado = json.loads(req.text)
            print('lista das formas de pagamento!\n')
            contagem = 0
            for item in resultado['items']:
                # print(item['id'], '\n')
                # print(item)
                lista_resultado.append(item)
                contagem += 1
            print('total de itens: ', str(contagem))
            return lista_resultado
        else:
            return None

    @classmethod
    def post_add_forma_de_pagamento(cls, url, access_token, auxiliar_json):
        headers = {'authorization': access_token, 'content-type': 'application/json'}
        data_sent = json.dumps(auxiliar_json)
        url_funcao = "/api/v1/financeiro/formas-pagamento"
        url_api = url + url_funcao
        print('Iniciando inclusão, executando post na url:\n', url_api)
        req = requests.post(url_api, data=data_sent, headers=headers)
        print("Resultado: ", req.status_code)
        if req.status_code != 201:
            print('retorno:\n')
            print(req.text)
        ret = req
        req.close()
        return ret

