#!/usr/bin/python3
import time
import src.bitwarden as bitwarden

SAMPLE_FILE = "local/p.json"


def main():
  vault = bitwarden.Vault()
  print("Loading vault")
  vault.load(SAMPLE_FILE)
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
    print(f"- ---[{folder.name:20}: {len(folder.items):3}] {'-'*50}")
    for item in folder.items:
      _classname = bitwarden.helpers.get_item_class_name(item.type)
      print(f"  - [{_classname:10}] {item.name:20}")

  print()


if __name__ == "__main__":
  start_time = time.time()
  main()
  elapsed = time.time() - start_time
  print(f"Finished in {elapsed:.2f} seconds")
