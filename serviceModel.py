class ServiceModel(object):
    def __init__(self, url: str, data, headers):
        self.url = url
        self.data = data
        self.headers = headers
