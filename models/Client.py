from services.ClientService import ClientService

class Client:
    def __init__(self, url_client, user, password):
        self.access_token = ''
        self.authenticated = False
        self.url_client = url_client
        self.user = user
        self.password = password


    def set_url_client(self, url_client):
        self.url_client = url_client

    def get_token_API(self):
        temp = self.access_token = ClientService.authenticate(self.url_client, self.user, self.password)
        if temp is not None:
            self.access_token = temp
        else:
            self.access_token = ''

