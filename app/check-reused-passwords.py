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

  print(f"Found {len(vault.logins):3} logins.")
  print()

  passwords = {}

  for login in vault.logins.values():
    if login.password not in passwords:
      passwords[login.password] = []
    passwords[login.password].append(login)

  reused = {k:v for (k,v) in passwords.items() if len(v) > 1}

  if not reused:
    print("All good !!! No reused passwords :)")
  else:
    print(f"OOOOPS !!! {len(reused)} reused passwords:")
    for (password, login_list) in reused.items():
      print(f"- [{password}]")
      for login in login_list:
        print(f"    - [{login.name:40}]")


if __name__ == "__main__":
  main()
