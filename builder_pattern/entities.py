class HTTPRequest:
    def __init__(self):
        self.method = None
        self.url = None
        self.headers = {}
        self.body = None

    def __str__(self):
        return f"Method: {self.method}, URL: {self.url}, Headers: {self.headers}, Body: {self.body}"
