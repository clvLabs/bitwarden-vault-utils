#!/usr/bin/python
import time
import src.bitwarden as bitwarden

SAMPLE_FILE = "local/p.json"


def main():
  vault = bitwarden.Vault()
  print("Loading vault")
  vault.load(SAMPLE_FILE)

  print("Vault loaded:")

  print(f"- logins ({len(vault.logins)})")
  for i in vault.logins.values():
    if not i.name.startswith("at"): continue    # Debug filter !
    # print(f"  - [{i.name:40}] {i.uris[0].uri if i.uris else ''}")
    print(f"  - [{i.name:40}] {i.folder.name}")

  print(f"- secure_notes ({len(vault.secure_notes)})")
  for i in vault.secure_notes.values():
    print(f"  - [{i.name:40}] {i.folder.name}")

  print(f"- cards ({len(vault.cards)})")
  for i in vault.cards.values():
    print(f"  - [{i.name:40}] {i.folder.name}")

  print(f"- identities ({len(vault.identities)})")
  for i in vault.identities.values():
    print(f"  - [{i.name:40}] {i.folder.name}")

  print(f"- folders ({len(vault.folders)})")
  for f in vault.folders.values():
    print(f"  - [{f.name:40}] ({len(f.items):3} items)")


if __name__ == "__main__":
  start_time = time.time()
  main()
  elapsed = time.time() - start_time
  print(f"Finished in {elapsed:.2f} seconds")
