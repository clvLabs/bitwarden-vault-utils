import requests
import hashlib


class PWNED:

  @staticmethod
  def is_password_pnwed(password):
      """Returns number of times password was seen in pwned database."""
      sha1pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
      head, tail = sha1pwd[:5], sha1pwd[5:]
      url = 'https://api.pwnedpasswords.com/range/' + head
      res = requests.get(url)

      if res.status_code != 200:
          raise RuntimeError('Error fetching "{}": {}'.format(url, res.status_code))

      hashes = (line.split(':') for line in res.text.splitlines())
      foundcount = next((int(foundcount) for t, foundcount in hashes if t == tail), 0)

      return foundcount
