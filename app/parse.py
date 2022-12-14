#!/usr/bin/python3
import argparse
import src.bitwarden as bitwarden


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('file', type=str, help='File to parse')
  args = parser.parse_args()

  vault = bitwarden.Vault()
  print("Loading vault")
  vault.load(args.file)
  print()

  print(f"Found {len(vault.items)} items:")
  print(f"- {len(vault.logins):3} logins")
  print(f"- {len(vault.secure_notes):3} secure_notes")
  print(f"- {len(vault.cards):3} cards")
  print(f"- {len(vault.identities):3} identities")
  print()

  print(f"Found {len(vault.folders)} folders:")
  for folder in vault.folders.values():
    print()
    print(f"- ---[{len(folder.items):3} {folder.name:20}] {'-'*50}")
    for item in folder.items:
      _classname = bitwarden.helpers.get_item_class_name(item.type)

      extrainfo = ""
      if type(item) is bitwarden.Login:
        extrainfo = f"[{item.username:40}] "

      print(f"- [{item.id}] [{folder.name:20}] [{_classname:10}] {extrainfo}{item.name}")

  print()


if __name__ == "__main__":
  main()
