from .item import Item
import src.bitwarden.helpers as helpers


class Identity(Item):

    def __init__(self):
      super().__init__()
      self.title = None
      self.first_name = None
      self.middle_name = None
      self.last_name = None
      self.address1 = None
      self.address2 = None
      self.address3 = None
      self.city = None
      self.state = None
      self.postal_code = None
      self.country = None
      self.company = None
      self.email = None
      self.phone = None
      self.ssn = None
      self.username = None
      self.passport_number = None
      self.license_number = None


    def __str__(self):
      return f"<bitwarden.Identity name=\"{self.name}\">"


    def __repr__(self):
      return self.__str__()


    def to_obj(self):
      obj = super().to_obj()
      obj.update({
        "identity": {
          "title": helpers.nullblank(self.title),
          "firstName": helpers.nullblank(self.first_name),
          "middleName": helpers.nullblank(self.middle_name),
          "lastName": helpers.nullblank(self.last_name),
          "address1": helpers.nullblank(self.address1),
          "address2": helpers.nullblank(self.address2),
          "address3": helpers.nullblank(self.address3),
          "city": helpers.nullblank(self.city),
          "state": helpers.nullblank(self.state),
          "postalCode": helpers.nullblank(self.postal_code),
          "country": helpers.nullblank(self.country),
          "company": helpers.nullblank(self.company),
          "email": helpers.nullblank(self.email),
          "phone": helpers.nullblank(self.phone),
          "ssn": helpers.nullblank(self.ssn),
          "username": helpers.nullblank(self.username),
          "passportNumber": helpers.nullblank(self.passport_number),
          "licenseNumber": helpers.nullblank(self.license_number),
        }
      })
      return obj


    @staticmethod
    def from_obj(obj):
      if "identity" not in obj:
        raise Exception("Item has no 'identity' field")

      inner_obj = obj["identity"]

      new_obj = Identity()
      new_obj._parse_item_fields(obj)
      if "title" in inner_obj:           new_obj.title = helpers.nonull(inner_obj["title"])
      if "firstName" in inner_obj:       new_obj.first_name = helpers.nonull(inner_obj["firstName"])
      if "middleName" in inner_obj:      new_obj.middle_name = helpers.nonull(inner_obj["middleName"])
      if "lastName" in inner_obj:        new_obj.last_name = helpers.nonull(inner_obj["lastName"])
      if "address1" in inner_obj:        new_obj.address1 = helpers.nonull(inner_obj["address1"])
      if "address2" in inner_obj:        new_obj.address2 = helpers.nonull(inner_obj["address2"])
      if "address3" in inner_obj:        new_obj.address3 = helpers.nonull(inner_obj["address3"])
      if "city" in inner_obj:            new_obj.city = helpers.nonull(inner_obj["city"])
      if "state" in inner_obj:           new_obj.state = helpers.nonull(inner_obj["state"])
      if "postalCode" in inner_obj:      new_obj.postal_code = helpers.nonull(inner_obj["postalCode"])
      if "country" in inner_obj:         new_obj.country = helpers.nonull(inner_obj["country"])
      if "company" in inner_obj:         new_obj.company = helpers.nonull(inner_obj["company"])
      if "email" in inner_obj:           new_obj.email = helpers.nonull(inner_obj["email"])
      if "phone" in inner_obj:           new_obj.phone = helpers.nonull(inner_obj["phone"])
      if "ssn" in inner_obj:             new_obj.ssn = helpers.nonull(inner_obj["ssn"])
      if "username" in inner_obj:        new_obj.username = helpers.nonull(inner_obj["username"])
      if "passportNumber" in inner_obj:  new_obj.passport_number = helpers.nonull(inner_obj["passportNumber"])
      if "licenseNumber" in inner_obj:   new_obj.license_number = helpers.nonull(inner_obj["licenseNumber"])
      return new_obj
