# bitwarden-vault-utils

Utilities to manage [bitwarden](https://bitwarden.com/) `json` vault data.

## Setup
* Create a `local` folder in the project folder.
* Copy a `JSON` export file in the `local` folder (e.g. `vault.json`)

## Reviewing vault info
```
$ python3 app/parse.py -h
usage: parse.py [-h] file

positional arguments:
  file        File to parse

optional arguments:
  -h, --help  show this help message and exit
```

Sample:
```
$ python3 app/parse.py local/vault.json
Loading vault

Found 161 items:
- 156 logins
-   1 secure_notes
-   2 cards
-   2 identities

Found 14 folders:

- ---[  1 (no folder)         ] --------------------------------------------------
- [xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx] [(no folder)         ] [SecureNote] test-secure-note

- ---[ 10 Business            ] --------------------------------------------------
- [xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx] [Business            ] [Login     ] [someone@gmail.com                       ] openexchangerates.org
...

- ---[ 18 Develop             ] --------------------------------------------------
- [xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx] [Develop             ] [Login     ] [someone@gmail.com                       ] developer.adobe.com
- [xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx] [Develop             ] [Login     ] [someone@gmail.com                       ] docker.com
- [xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx] [Develop             ] [Login     ] [someone@gmail.com                       ] github.com
...

- ---[  6 Email               ] --------------------------------------------------
- [xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx] [Email               ] [Login     ] [someone@gmail.com                       ] GMail
...
```

## Checking for pwned passwords
This is done using [haveibeenpwned](https://haveibeenpwned.com/)'s API.

This **does NOT** send any of your passwords anywhere. Check code/API docs to make sure if you wish.


```
$ python3 app/check-pwned-passwords.py -h
usage: check-pwned-passwords.py [-h] file

positional arguments:
  file        File to parse

optional arguments:
  -h, --help  show this help message and exit
```

Sample:
```
$ python3 app/check-pwned-passwords.py local/vault.json
Loading vault

Found 155 logins.

OOOOPS !!! 1 pwned passwords:
- [Sample web login                        ] [1234abcd]
```

## Cleaning vault secrets
If you want to keep a vault file in your computer but don't need to keep the secret data in it, you can clean a vault's secrets with this script. It allows saving the _clean_ version in a different file if needed.

```
$ python3 app/clean-secrets.py -h
usage: clean-secrets.py [-h] infile outfile

positional arguments:
  infile      File to parse
  outfile     File to write

optional arguments:
  -h, --help  show this help message and exit
```

Sample:
```
$ python3 app/clean-secrets.py local/vault.json local/vault.json
Loading vault

Found 160 items:
- 156 logins
-   0 secure_notes
-   2 cards
-   2 identities

Cleaning secrets
Saving clean vault
```

## Development

### Creating temporary/personal scripts without altering the repo
From the project folder:
* Create a folder for local scripts:
  ```
  $ mkdir -p local/scripts/src
  ```
* Symlink the `app/src` folder into your local scripts folder:
  ```
  $ ln -s $(pwd)/app/src $(pwd)/local/scripts/src
  ```
* Copy a sample script into your local scripts folder:
  ```
  $ cp app/parse.py local/scripts/sample.py
  ```
* Edit the new local script and modify as needed.
* Run from the project folder:
  ```
  $ python3 local/scripts/sample.py
  ```
