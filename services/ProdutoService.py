import requests, json

class ProdutoService(object):
    '''    def __init__(self, url_client, access_token):
            self.url_client = url_client
            self.access_token = access_token'''

    @classmethod
    def get_produtos(cls, url, access_token, inicio = 0, contador = 0):
        '''

        :param url:
        :param access_token:
        :param inicio:
        :param contador:
        :return:
        '''
        headers = {'authorization': access_token}
        params = {'sort': 'id', 'start': inicio, 'count': contador}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/produto/produtos"
        url_api = url + url_funcao
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers, params=params)
        print(req.status_code)
        if req.status_code == 200:
            resultado = json.loads(req.text)
            print('lista dos itens!\n')
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
    def get_produto_id(cls,  url, access_token, id_produto):
        headers = {'authorization': access_token}
        #params = {'id': id_produto}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/produto/produtos/consulta/"   #aceita auxiliar
#        url_funcao = "/api/v1/produto/produtos/"           #somente pelo ID.
        url_api = url + url_funcao + str(id_produto).zfill(14)
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers)
        print(req.status_code)
        if req.status_code == 200:
            resultado = json.loads(req.text)
            print('lista dos itens!\n')
            return resultado
        else:
            return None


class CodigosAuxiliaresService(object):
    def __init__(self):
        pass

    @classmethod
    def get_auxiliares(cls, url, access_token, inicio=0, contador=0):
        '''

        :param url:
        :param access_token:
        :param inicio:
        :param contador:
        :return:
        '''
        headers = {'authorization': access_token}
        params = {'sort': 'id', 'start': inicio, 'count': contador}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/produto/codigos-auxiliares"
        url_api = url + url_funcao
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers, params=params)
        print(req.status_code)
        if req.status_code == 200:
            resultado = json.loads(req.text)
            print('lista dos itens!\n')
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
    def get_auxiliar_id(cls,  url, access_token, id_produto):
        headers = {'authorization': access_token}
        #params = {'id': id_produto}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/produto/produtos/{}/codigos-auxiliares".format(id_produto)
        url_api = url + url_funcao
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
    def post_add_auxiliar(cls, url, access_token, id_produto, auxiliar_json):
        headers = {'authorization': access_token, 'content-type': 'application/json'}
        data_sent = json.dumps(auxiliar_json)
        url_funcao = "/api/v1/produto/produtos/{}/codigos-auxiliares".format(id_produto)
        url_api = url + url_funcao
        print('Iniciando inclusão, executando post na url:\n', url_api)
        #print('produto_json:\n', produto_json)
        req = requests.post(url_api, data=data_sent, headers=headers)
        print("Resultado: ", req.status_code)
        if req.status_code != 201:
            print('retorno:\n')
            print(req.text)
        ret = req
        req.close()
        return ret

class SecaoService(object):
    def __init__(self):
        pass

    @classmethod
    def get_secoes(cls, url, access_token, inicio=0, contador=0):
        '''

        :param url:
        :param access_token:
        :param inicio:
        :param contador:
        :return:
        '''
        headers = {'authorization': access_token}
        params = {'sort': 'id', 'start': inicio, 'count': contador}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/produto/secoes"
        url_api = url + url_funcao
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers, params=params)
        print(req.status_code)
        if req.status_code == 200:
            resultado = json.loads(req.text)
            print('lista de seções!\n')
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
    def get_secao_id(cls, url, access_token, id_secao):
        headers = {'authorization': access_token}
        #params = {'id': id_produto}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/produto/secoes/{}".format(id_secao)
        url_api = url + url_funcao
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
    def post_add_secao(cls, url, access_token, auxiliar_json):
        headers = {'authorization': access_token, 'content-type': 'application/json'}
        data_sent = json.dumps(auxiliar_json)
        url_funcao = "/api/v1/produto/secoes"
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

class PrecoService(object):

    @classmethod
    def get_precos(cls, url, access_token, inicio=0, contador=0):
        headers = {'authorization': access_token}
        params = {'sort': 'id', 'start': inicio, 'count': contador}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/produto/precos"
        url_api = url + url_funcao
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers, params=params)
        print(req.status_code)
        if req.status_code == 200:
            resultado = json.loads(req.text)
            print('lista dos itens!\n')
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

#verificar ainda o método abaixo, apenas escrito, realizar edições.
    @classmethod
    def get_preco_id(cls, url, access_token, id_produto, id_loja):
        seq_tabela_retorno = id_loja - 1 #feito pq json começa de 0, ordem do json mesma das lojas
        headers = {'authorization': access_token}
        lista_resultado = []
        #print('headers:\n', headers)
        url_funcao = "/api/v1/produto/produtos/{}/precos".format(id_produto)
        url_api = url + url_funcao
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers)
        print(req.status_code)
        if req.status_code == 200:
            print(req.text)
            resultado = json.loads(req.text)
            #print('lista dos itens!\n')        #Apenas para verificar se era nulo o retorno da requisição
            return resultado[seq_tabela_retorno].get('id'), 200
        else:
            return -1, req.status_code

    def get_preco_by_id(self):
        pass

class ProdutoFornecedorService(object):
    def __init__(self):
        pass

    @classmethod
    def get_produto_fornecedor(self, url, access_token, id_produto):
        headers = {'authorization': access_token}
        print('headers:\n', headers)
        url_funcao = "/api/v1/produto/produtos/{}/fornecedores".format(id_produto)
        url_api = url + url_funcao
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
    def post_add_produto_fornecedor(self, url, access_token, id_produto, auxiliar_json):
        headers = {'authorization': access_token, 'content-type': 'application/json'}
        data_sent = json.dumps(auxiliar_json)
        url_funcao = "/api/v1/produto/produtos/{}/fornecedores".format(id_produto)
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

class GrupoService(object):
    def __init__(self):
        pass

    @classmethod
    def get_grupos(cls, url, access_token, id_secao, inicio=0, contador=0):
        '''

        :param url:
        :param access_token:
        :param inicio:
        :param contador:
        :return:
        '''
        headers = {'authorization': access_token}
        params = {'sort': 'id', 'start': inicio, 'count': contador}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/produto/secoes/{}/grupos".format(id_secao)
        url_api = url + url_funcao
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers, params=params)
        print(req.status_code)
        if req.status_code == 200:
            resultado = json.loads(req.text)
            print('lista de grupos!\n')
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
    def post_add_grupo(cls, url, access_token, id_secao, auxiliar_json):
        headers = {'authorization': access_token, 'content-type': 'application/json'}
        data_sent = json.dumps(auxiliar_json)
        url_funcao = "/api/v1/produto/secoes/{}/grupos".format(id_secao)
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

class SubGrupoService(object):
    def __init__(self):
        pass

    @classmethod
    def get_subgrupos(cls, url, access_token, id_secao, id_grupo, inicio=0, contador=0):
        '''

        :param url:
        :param access_token:
        :param inicio:
        :param contador:
        :return:
        '''
        headers = {'authorization': access_token}
        params = {'sort': 'id', 'start': inicio, 'count': contador}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/produto/secoes/{}/grupos/{}/subgrupos".format(id_secao, id_grupo)
        url_api = url + url_funcao
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers, params=params)
        print(req.status_code)
        if req.status_code == 200:
            resultado = json.loads(req.text)
            print('lista de subgrupos!\n')
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
    def post_add_subgrupo(cls, url, access_token, id_secao, id_grupo, auxiliar_json):
        headers = {'authorization': access_token, 'content-type': 'application/json'}
        data_sent = json.dumps(auxiliar_json)
        url_funcao = "/api/v1/produto/secoes/{}/grupos/{}/subgrupos".format(id_secao, id_grupo)
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




