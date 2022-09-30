import json
from .folder import Folder
from .item import Item
import src.bitwarden.helpers as helpers

class Vault:

  def __init__(self):
    no_folder = Folder()
    no_folder.name = "(no folder)"

    # Original exported data
    self.encrypted = False
    self.folders = {
      None: no_folder
    }
    self.items = {}

    # Processed data
    self.logins = {}
    self.secure_notes = {}
    self.cards = {}
    self.identities = {}


  def load(self, filename):
    with open(filename) as f:
      data = json.load(f)
      self._parse(data)
      self._update()


  def _parse(self, data):
    if "encrypted" in data:
      self.encrypted = data["encrypted"]

    if "folders" in data:
      for folder_obj in data["folders"]:
        folder = Folder.from_obj(folder_obj)
        self.folders[folder.id] = folder

    if "items" in data:
      for item_obj in data["items"]:
        item = Item.from_obj(item_obj)
        self.items[item.id] = item


  def _update(self):
    self.logins =       {obj.id: obj for obj in self.items.values() if obj.type == helpers.ItemType.LOGIN.value}
    self.secure_notes = {obj.id: obj for obj in self.items.values() if obj.type == helpers.ItemType.SECURE_NOTE.value}
    self.cards =        {obj.id: obj for obj in self.items.values() if obj.type == helpers.ItemType.CARD.value}
    self.identities =   {obj.id: obj for obj in self.items.values() if obj.type == helpers.ItemType.IDENTITY.value}

    for item in self.items.values():
      item.folder = self.folders[item.folder_id]
      self.folders[item.folder_id].items.append(item)
