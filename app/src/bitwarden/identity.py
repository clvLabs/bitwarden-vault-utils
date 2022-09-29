from .item import Item


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


    @staticmethod
    def from_obj(obj):
      if "identity" not in obj:
        raise Exception("Item has no 'identity' field")

      inner_obj = obj["identity"]

      new_obj = Identity()
      new_obj._parse_item_fields(obj)
      if "title" in inner_obj:           new_obj.title = inner_obj["title"]
      if "firstName" in inner_obj:       new_obj.first_name = inner_obj["firstName"]
      if "middleName" in inner_obj:      new_obj.middle_name = inner_obj["middleName"]
      if "lastName" in inner_obj:        new_obj.last_name = inner_obj["lastName"]
      if "address1" in inner_obj:        new_obj.address1 = inner_obj["address1"]
      if "address2" in inner_obj:        new_obj.address2 = inner_obj["address2"]
      if "address3" in inner_obj:        new_obj.address3 = inner_obj["address3"]
      if "city" in inner_obj:            new_obj.city = inner_obj["city"]
      if "state" in inner_obj:           new_obj.state = inner_obj["state"]
      if "postalCode" in inner_obj:      new_obj.postal_code = inner_obj["postalCode"]
      if "country" in inner_obj:         new_obj.country = inner_obj["country"]
      if "company" in inner_obj:         new_obj.company = inner_obj["company"]
      if "email" in inner_obj:           new_obj.email = inner_obj["email"]
      if "phone" in inner_obj:           new_obj.phone = inner_obj["phone"]
      if "ssn" in inner_obj:             new_obj.ssn = inner_obj["ssn"]
      if "username" in inner_obj:        new_obj.username = inner_obj["username"]
      if "passportNumber" in inner_obj:  new_obj.passport_number = inner_obj["passportNumber"]
      if "licenseNumber" in inner_obj:   new_obj.license_number = inner_obj["licenseNumber"]
      return new_obj
