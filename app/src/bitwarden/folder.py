import src.bitwarden.helpers as helpers

class Folder:

    def __init__(self):
      self.id = None
      self.name = None

      self.items = []


    def to_obj(self):
      return {
        "id": helpers.nullblank(self.id),
        "name": helpers.nullblank(self.name),
      }


    @staticmethod
    def from_obj(obj):
      new_obj = Folder()
      if "id" in obj:    new_obj.id = helpers.nonull(obj["id"])
      if "name" in obj:  new_obj.name = helpers.nonull(obj["name"])
      return new_obj
