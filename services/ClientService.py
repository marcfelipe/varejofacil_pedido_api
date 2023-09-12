import requests, json


class ClientService(object):
    @classmethod
    def authenticate(cls, url, user, password):
        headers_ = {'content-type': 'application/json'}
        payload = {'username': user,
                   'password': password}
        data_sent = json.dumps(payload)
        url_funcao = "/api/auth"
        url_serv = url + url_funcao
        print(url_serv)
        req = requests.post(url_serv, data=data_sent, headers=headers_)
        print(req.status_code)
        if req.status_code == 200:
            # print(req.text)
            resultado = json.loads(req.text)
            print('AccessToken:', resultado['accessToken'])
            return resultado['accessToken']
        else:
            return None
