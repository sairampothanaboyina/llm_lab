class Website:

    title: str
    description: str
    url: str

    def __init__(self, url):
        if not url or not url.strip():
            raise ValueError("url cannot be empty")
        self.url = url

    def __str__(self):
        return self.url
