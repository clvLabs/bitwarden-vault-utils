from .item import Item
import src.bitwarden.helpers as helpers


class SecureNote(Item):

    def __init__(self):
      super().__init__()

      self.note_type = None


    def __str__(self):
      return f"<bitwarden.SecureNote name=\"{self.name}\">"


    def __repr__(self):
      return self.__str__()


    def to_obj(self):
      obj = super().to_obj()
      obj.update({
        "secureNote": {
          "type": helpers.nullblank(self.note_type),
        }
      })
      return obj


    @staticmethod
    def from_obj(obj):
      if "secureNote" not in obj:
        raise Exception("Item has no 'secureNote' field")

      inner_obj = obj["secureNote"]

      new_obj = SecureNote()
      new_obj._parse_item_fields(obj)
      if "type" in inner_obj:    new_obj.note_type = helpers.nonull(inner_obj["type"])
      return new_obj
