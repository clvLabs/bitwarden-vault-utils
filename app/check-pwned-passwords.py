#!/usr/bin/python3
import argparse
import src.bitwarden as bitwarden
import src.pwned as pwned
import src.threadize as threadize


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

  empty_passwords = []
  pwned_passwords = []
  login_count = len(vault.logins)
  current_login_index = 0


  # - - - - - - - - - - - - - - - - - - - - - - - - - -
  # Inner method (has access to local vars)
  def check_password(chunk, chunkid, _log):
    nonlocal current_login_index, login_count \
      , pwned_passwords, empty_passwords

    for login in chunk:
      current_login_index += 1

      _log("\r" \
        "Checking password:" \
        f" {current_login_index:3}/{login_count:3}" \
        f" {len(pwned_passwords):3} pwned" \
        f" {len(empty_passwords):3} empty" \
        "   ")

      if not(login.password):
        empty_passwords.append(login)
      elif pwned.PWNED.is_password_pnwed(login.password):
        pwned_passwords.append(login)

  # - - - - - - - - - - - - - - - - - - - - - - - - - -

  login_list = list(vault.logins.values())
  threadize.threadize(login_list, check_password, lambda msg: print(msg, end=""))

  print("\r" + " "*80, end="\r")

  if empty_passwords:
    print(f"WARNING: {len(empty_passwords)} empty passwords found !")

  if not pwned_passwords:
    print("All good !!! No pwned passwords :)")
  else:
    print(f"OOOOPS !!! {len(pwned_passwords)} pwned passwords:")
    for login in pwned_passwords:
      print(f"- [{login.name:40}] [{login.password}]")

  print()


if __name__ == "__main__":
  main()
