# bitwarden-vault-parse

Parse exported [bitwarden](https://bitwarden.com/) `json` vault data.

## Setup
* Create a `local` folder in the project folder.
* Copy a `JSON` export file in the `local` folder (e.g. `vault.json`)

## Usage

### Reviewing vault info
```
$ python3 app/parse.py -h
usage: parse.py [-h] file

positional arguments:
  file        File to parse

optional arguments:
  -h, --help  show this help message and exi
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
- [xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx] [Business            ] [Login     ] openexchangerates.org
...

- ---[ 18 Develop             ] --------------------------------------------------
- [xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx] [Develop             ] [Login     ] developer.adobe.com
- [xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx] [Develop             ] [Login     ] docker.com
- [xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx] [Develop             ] [Login     ] github.com
...

- ---[  6 Email               ] --------------------------------------------------
- [xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx] [Email               ] [Login     ] GMail
...
```

### Cleaning vault secrets
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

### Creating temporary scripts without altering the repo
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
  $ local/scripts/sample.py
  ```
