
class Folder:

    def __init__(self):
      self.id = None
      self.name = None

      self.items = []


    @staticmethod
    def from_obj(obj):
      new_obj = Folder()
      if "id" in obj:    new_obj.id = obj["id"]
      if "name" in obj:  new_obj.name = obj["name"]
      return new_obj
