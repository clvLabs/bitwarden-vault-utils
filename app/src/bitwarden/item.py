import src.bitwarden.helpers as helpers
import src.bitwarden.helpers as helpers


class Item:

    def __init__(self):
      self.id = None
      self.organization_id = None
      self.folder_id = None
      self.type = None
      self.reprompt = None
      self.name = None
      self.notes = None
      self.favorite = None
      self.collection_ids = None

      self.folder = None


    @staticmethod
    def from_obj(obj):
      if "type" not in obj:
        raise Exception("Item has no 'type' field")

      _class = helpers.get_item_class(obj["type"])

      return _class.from_obj(obj)


    def _parse_item_fields(self, obj):
      if "id" in obj:              self.id = helpers.nonull(obj["id"])
      if "organizationId" in obj:  self.organization_id = helpers.nonull(obj["organizationId"])
      if "folderId" in obj:        self.folder_id = helpers.nonull(obj["folderId"])
      if "type" in obj:            self.type = helpers.nonull(obj["type"])
      if "reprompt" in obj:        self.reprompt = helpers.nonull(obj["reprompt"])
      if "name" in obj:            self.name = helpers.nonull(obj["name"])
      if "notes" in obj:           self.notes = helpers.nonull(obj["notes"])
      if "favorite" in obj:        self.favorite = helpers.nonull(obj["favorite"])
      if "collectionIds" in obj:   self.collection_ids = helpers.nonull(obj["collectionIds"])
