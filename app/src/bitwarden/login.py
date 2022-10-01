from .item import Item
import src.bitwarden.helpers as helpers


class URI:

    def __init__(self):
      self.match = None
      self.uri = None


    def __str__(self):
      return f"<bitwarden.URI uri=\"{self.uri}\">"


    def __repr__(self):
      return self.__str__()


    def to_obj(self):
      return {
        "match": helpers.nullblank(self.match),
        "uri": helpers.nullblank(self.uri),
      }


    @staticmethod
    def from_obj(obj):
      new_obj = URI()
      if "match" in obj:  new_obj.match = helpers.nonull(obj["match"])
      if "uri" in obj:    new_obj.uri = helpers.nonull(obj["uri"])
      return new_obj


class Login(Item):

    def __init__(self):
      super().__init__()

      self.uris = []
      self.username = None
      self.password = None
      self.totp = None


    def clean_secrets(self):
      super().clean_secrets()
      self.password = None
      self.totp = None


    def __str__(self):
      return f"<bitwarden.Login name=\"{self.name}\">"


    def __repr__(self):
      return self.__str__()


    def to_obj(self):
      obj = super().to_obj()
      obj.update({
        "login": {
          "uris": [uri.to_obj() for uri in self.uris],
          "username": helpers.nullblank(self.username),
          "password": helpers.nullblank(self.password),
          "totp": helpers.nullblank(self.totp),
        }
      })
      return obj


    @staticmethod
    def from_obj(obj):
      if "login" not in obj:
        raise Exception("Item has no 'login' field")

      inner_obj = obj["login"]

      new_obj = Login()
      new_obj._parse_item_fields(obj)
      if "uris" in inner_obj:      new_obj.uris = [URI.from_obj(_uri_obj) for _uri_obj in inner_obj["uris"]]
      if "username" in inner_obj:  new_obj.username = helpers.nonull(inner_obj["username"])
      if "password" in inner_obj:  new_obj.password = helpers.nonull(inner_obj["password"])
      if "totp" in inner_obj:      new_obj.totp = helpers.nonull(inner_obj["totp"])
      return new_obj
