from .item import Item
import src.bitwarden.helpers as helpers


class Card(Item):

    def __init__(self):
      super().__init__()

      self.holder_name = None
      self.brand = None
      self.number = None
      self.exp_month = None
      self.exp_year = None
      self.code = None


    def __str__(self):
      return f"<bitwarden.Card name=\"{self.name}\">"


    def __repr__(self):
      return self.__str__()


    def to_obj(self):
      obj = super().to_obj()
      obj.update({
        "card": {
          "cardholderName": helpers.nullblank(self.holder_name),
          "brand": helpers.nullblank(self.brand),
          "number": helpers.nullblank(self.number),
          "expMonth": helpers.nullblank(self.exp_month),
          "expYear": helpers.nullblank(self.exp_year),
          "code": helpers.nullblank(self.code),
        }
      })
      return obj


    @staticmethod
    def from_obj(obj):
      if "card" not in obj:
        raise Exception("Item has no 'card' field")

      inner_obj = obj["card"]

      new_obj = Card()
      new_obj._parse_item_fields(obj)
      if "cardholderName" in inner_obj:  new_obj.holder_name = helpers.nonull(inner_obj["cardholderName"])
      if "brand" in inner_obj:           new_obj.brand = helpers.nonull(inner_obj["brand"])
      if "number" in inner_obj:          new_obj.number = helpers.nonull(inner_obj["number"])
      if "expMonth" in inner_obj:        new_obj.exp_month = helpers.nonull(inner_obj["expMonth"])
      if "expYear" in inner_obj:         new_obj.exp_year = helpers.nonull(inner_obj["expYear"])
      if "code" in inner_obj:            new_obj.code = helpers.nonull(inner_obj["code"])
      return new_obj
