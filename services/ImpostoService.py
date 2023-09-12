import requests, json


class SituacaoService(object):
    def __init__(self):
        pass

    @classmethod
    def get_situacoes(cls, url, access_token, inicio=0, contador=0):
        headers = {'authorization': access_token}
        params = {'sort': 'id', 'start': inicio, 'count': contador}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/fiscal/situacoes"
        url_api = url + url_funcao
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers, params=params)
        print(req.status_code)
        if req.status_code == 200:
            resultado = json.loads(req.text)
            print('lista de situacoes!\n')
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
    def post_add_situacao(cls, url, access_token, auxiliar_json):
        headers = {'authorization': access_token, 'content-type': 'application/json'}
        data_sent = json.dumps(auxiliar_json)
        url_funcao = "/api/v1/fiscal/situacoes"
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

class TabelaTributariaService():
    def __init__(self):
        pass

    @classmethod
    def get_tabelas_tributarias(cls, url, access_token, inicio=0, contador=0):
        headers = {'authorization': access_token}
        params = {'sort': 'id', 'start': inicio, 'count': contador}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/fiscal/tabelas-tributarias"
        url_api = url + url_funcao
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers, params=params)
        print(req.status_code)
        if req.status_code == 200:
            resultado = json.loads(req.text)
            print('lista de tabelas tributarias!\n')
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
    def post_add_tabela_tributaria(cls, url, access_token, auxiliar_json):
        headers = {'authorization': access_token, 'content-type': 'application/json'}
        data_sent = json.dumps(auxiliar_json)
        url_funcao = "/api/v1/fiscal/tabelas-tributarias"
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


class FederalService(object):
    def __init__(self):
        pass

    @classmethod
    def get_impostos_federais(cls, url, access_token, inicio=0, contador=0):
        headers = {'authorization': access_token}
        params = {'sort': 'id', 'start': inicio, 'count': contador}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/fiscal/impostos-federais"
        url_api = url + url_funcao
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers, params=params)
        print(req.status_code)
        if req.status_code == 200:
            resultado = json.loads(req.text)
            print('lista de impostos federais!\n')
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
    def post_add_imposto_federal(cls, url, access_token, auxiliar_json):
        headers = {'authorization': access_token, 'content-type': 'application/json'}
        data_sent = json.dumps(auxiliar_json)
        url_funcao = "/api/v1/fiscal/impostos-federais"
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


