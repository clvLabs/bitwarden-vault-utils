from .item import Item


class SecureNote(Item):

    def __init__(self):
      super().__init__()


    def __str__(self):
      return f"<bitwarden.SecureNote name=\"{self.name}\">"


    def __repr__(self):
      return self.__str__()


    @staticmethod
    def from_obj(obj):
      new_obj = SecureNote()
      return new_obj
