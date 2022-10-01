#!/usr/bin/python3
import argparse
import src.bitwarden as bitwarden


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('infile', type=str, help='File to parse')
  parser.add_argument('outfile', type=str, help='File to write')
  args = parser.parse_args()

  vault = bitwarden.Vault()
  print("Loading vault")
  vault.load(args.infile)
  print()

  print(f"Found {len(vault.items)} items:")
  print(f"- {len(vault.logins):3} logins")
  print(f"- {len(vault.secure_notes):3} secure_notes")
  print(f"- {len(vault.cards):3} cards")
  print(f"- {len(vault.identities):3} identities")
  print()

  print(f"Cleaning secrets")
  vault.clean_secrets()

  print(f"Saving clean vault")
  vault.save(args.outfile)


if __name__ == "__main__":
  main()
