from .item import Item


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


    @staticmethod
    def from_obj(obj):
      if "card" not in obj:
        raise Exception("Item has no 'card' field")

      inner_obj = obj["card"]

      new_obj = Card()
      new_obj._parse_item_fields(obj)
      if "cardholderName" in inner_obj:  new_obj.holder_name = inner_obj["cardholderName"]
      if "brand" in inner_obj:           new_obj.brand = inner_obj["brand"]
      if "number" in inner_obj:          new_obj.number = inner_obj["number"]
      if "expMonth" in inner_obj:        new_obj.exp_month = inner_obj["expMonth"]
      if "expYear" in inner_obj:         new_obj.exp_year = inner_obj["expYear"]
      if "code" in inner_obj:            new_obj.code = inner_obj["code"]
      return new_obj
