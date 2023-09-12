import requests, json

class ClienteService(object):



    @classmethod
    def get_clientes(cls, url, access_token, inicio = 0, contador = 0):
        headers = {'authorization': access_token}
        params = {'sort': 'id', 'start': inicio, 'count': contador}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/pessoa/clientes"
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
    def get_cliente_id(cls,  url, access_token, id_cliente):
        headers = {'authorization': access_token}
        #params = {'id': id_produto}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/pessoa/clientes/"
        url_api = url + url_funcao + str(id_cliente)
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers)
        print(req.status_code)
        if req.status_code == 200:
            resultado = json.loads(req.text)
            print('lista de clientes!\n')
            return resultado
        else:
            return None


    @classmethod
    def post_add_cliente(cls, url, access_token, cliente_json):
        headers = {'authorization': access_token, 'content-type': 'application/json'}
        data_sent = json.dumps(cliente_json)
        url_funcao = "/api/v1/pessoa/clientes"
        url_api = url + url_funcao
        print('Iniciando inclusão, executando post na url:\n', url_api)
        #print('cliente_json_metodo post_add_cliente:\n', cliente_json)
        req = requests.post(url_api, data=data_sent, headers=headers)
        print("Resultado: ", req.status_code)
        ret = req
        req.close()
        return ret


    @classmethod
    def delete_cliente(cls, url, access_token, id_):
        pass


class FornecedorService(object):
    @classmethod
    def get_fornecedores(cls, url, access_token, inicio=0, contador=0):
        headers = {'authorization': access_token}
        params = {'sort': 'id', 'start': inicio, 'count': contador}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/pessoa/fornecedores"
        url_api = url + url_funcao
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers, params=params)
        print(req.status_code)
        if req.status_code == 200:
            resultado = json.loads(req.text)
            print('lista dos fornecedores!\n')
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
    def get_fornecedor_id(cls, url, access_token, id_fornecedor):
        headers = {'authorization': access_token}
        # params = {'id': id_produto}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/pessoa/fornecedores/"
        url_api = url + url_funcao + str(id_fornecedor)
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers)
        print(req.status_code)
        if req.status_code == 200:
            resultado = json.loads(req.text)
            print('lista de fornecedores!\n')
            return resultado
        else:
            return None

    @classmethod
    def post_add_fornecedor(cls, url, access_token, fornecedor_json):
        headers = {'authorization': access_token, 'content-type': 'application/json'}
        data_sent = json.dumps(fornecedor_json)
        url_funcao = "/api/v1/pessoa/fornecedores"
        url_api = url + url_funcao
        print('Iniciando inclusão, executando post na url:\n', url_api)
        # print('cliente_json_metodo post_add_cliente:\n', cliente_json)
        req = requests.post(url_api, data=data_sent, headers=headers)
        print("Resultado: ", req.status_code)
        ret = req
        req.close()
        return ret

    @classmethod
    def delete_fornecedor(cls, url, access_token, id_):
        pass

class FuncionarioService(object):
    @classmethod
    def get_funcionarios(cls, url, access_token, inicio=0, contador=0):
        headers = {'authorization': access_token}
        params = {'sort': 'id', 'start': inicio, 'count': contador}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/pessoa/funcionarios"
        url_api = url + url_funcao
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers, params=params)
        print(req.status_code)
        if req.status_code == 200:
            resultado = json.loads(req.text)
            print('lista dos funcionarios!\n')
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
    def get_funcionario_id(cls, url, access_token, id_funcionario):
        headers = {'authorization': access_token}
        # params = {'id': id_produto}
        lista_resultado = []
        print('headers:\n', headers)
        url_funcao = "/api/v1/pessoa/funcionarios/"
        url_api = url + url_funcao + str(id_funcionario)
        print('url_api: \n', url_api)
        req = requests.get(url_api, headers=headers)
        print(req.status_code)
        if req.status_code == 200:
            resultado = json.loads(req.text)
            print('lista de funcionarios!\n')
            return resultado
        else:
            return None

    @classmethod
    def post_add_funcionario(cls, url, access_token, funcionario_json):
        headers = {'authorization': access_token, 'content-type': 'application/json'}
        data_sent = json.dumps(funcionario_json)
        url_funcao = "/api/v1/pessoa/funcionarios"
        url_api = url + url_funcao
        print('Iniciando inclusão, executando post na url:\n', url_api)
        req = requests.post(url_api, data=data_sent, headers=headers)
        print("Resultado: ", req.status_code)
        ret = req
        req.close()
        return ret

    @classmethod
    def delete_funcionario(cls, url, access_token, id_):
        pass
