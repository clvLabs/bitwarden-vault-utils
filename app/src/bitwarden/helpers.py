from enum import Enum
import src.bitwarden.login as login
import src.bitwarden.securenote as securenote
import src.bitwarden.card as card
import src.bitwarden.identity as identity


class ItemType(Enum):
  LOGIN = 1
  SECURE_NOTE = 2
  CARD = 3
  IDENTITY = 4


def get_item_class(item_type):
  if type(item_type) is not ItemType:
    item_type = ItemType(item_type)

  if item_type == ItemType.LOGIN:
    return login.Login
  elif item_type == ItemType.SECURE_NOTE:
    return securenote.SecureNote
  elif item_type == ItemType.CARD:
    return card.Card
  elif item_type == ItemType.IDENTITY:
    return identity.Identity
  else:
    raise Exception(f"Item has a wrong 'type' field ({item_type})")


def get_item_class_name(item_type):
  if type(item_type) is not ItemType:
    item_type = ItemType(item_type)

  if item_type == ItemType.LOGIN:
    return "Login"
  elif item_type == ItemType.SECURE_NOTE:
    return "SecureNote"
  elif item_type == ItemType.CARD:
    return "Card"
  elif item_type == ItemType.IDENTITY:
    return "Identity"
  else:
    raise Exception(f"Item has a wrong 'type' field ({item_type})")


def nonull(data):
  return "" if data is None else data


def nullblank(data):
  return None if data == "" else data
