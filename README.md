# bitwarden-vault-parse

Parse exported [bitwarden](https://bitwarden.com/) `json` vault data.

## Setup
* Create a `local` folder in the project folder.
* Copy a `JSON` export file in the `local` folder (e.g. `vault.json`)

## Usage
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
