from .item import Item


class SecureNote(Item):

    def __init__(self):
      super().__init__()

      self.note_type = None


    def __str__(self):
      return f"<bitwarden.SecureNote name=\"{self.name}\">"


    def __repr__(self):
      return self.__str__()


    @staticmethod
    def from_obj(obj):
      if "secureNote" not in obj:
        raise Exception("Item has no 'secureNote' field")

      inner_obj = obj["secureNote"]

      new_obj = SecureNote()
      new_obj._parse_item_fields(obj)
      if "type" in inner_obj:    new_obj.note_type = inner_obj["type"]
      return new_obj
