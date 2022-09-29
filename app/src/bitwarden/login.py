from .item import Item


class URI:

    def __init__(self):
      self.match = None
      self.uri = None


    @staticmethod
    def from_obj(obj):
      new_obj = URI()
      if "match" in obj:  new_obj.match = obj["match"]
      if "uri" in obj:    new_obj.uri = obj["uri"]
      return new_obj


class Login(Item):

    def __init__(self):
      super().__init__()

      self.uris = []
      self.username = None
      self.password = None
      self.totp = None


    def __str__(self):
      return f"<bitwarden.Login name=\"{self.name}\">"


    def __repr__(self):
      return self.__str__()


    @staticmethod
    def from_obj(obj):
      if "login" not in obj:
        raise Exception("Item has no 'login' field")

      inner_obj = obj["login"]

      new_obj = Login()
      new_obj._parse_item_fields(obj)
      if "uris" in inner_obj:      new_obj.uris = [URI.from_obj(_uri_obj) for _uri_obj in inner_obj["uris"]]
      if "username" in inner_obj:  new_obj.username = inner_obj["username"]
      if "password" in inner_obj:  new_obj.password = inner_obj["password"]
      if "totp" in inner_obj:      new_obj.totp = inner_obj["totp"]
      return new_obj
