from abc import ABC, abstractclassmethod, abstractmethod, abstractstaticmethod

from builder_pattern.entities import HTTPRequest


class HouseBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass

    @abstractmethod
    def get_result(self):
        pass


class WoodenHouseBuilder(HouseBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.house = {"type": "Wooden House", "walls": [], "roof": None, "doors": []}

    def build_walls(self):
        self.house["walls"].append("Wooden Walls")

    def build_roof(self):
        self.house["roof"] = "Wooden Roof"

    def build_doors(self):
        self.house["doors"].append("Wooden Door")

    def get_result(self):
        return self.house


class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.house = {"type": "Concrete House", "walls": [], "roof": None, "doors": []}

    def build_walls(self):
        self.house["walls"].append("Concrete Walls")

    def build_roof(self):
        self.house["roof"] = "Concrete Roof"

    def build_doors(self):
        self.house["doors"].append("Steel Door")

    def get_result(self):
        return self.house


class HTTPRequestBuilder:
    def __init__(self):
        self.request = HTTPRequest()

    def set_method(self, method):
        self.request.method = method
        return self

    def set_url(self, url):
        self.request.url = url
        return self

    def add_header(self, key, value):
        self.request.headers[key] = value
        return self

    def set_body(self, body):
        self.request.body = body
        return self

    def build(self):
        return self.request
