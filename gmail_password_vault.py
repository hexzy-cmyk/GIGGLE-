#!/usr/bin/env python3
"""Store and load a Gmail app password without ever typing it in plain text."""

from __future__ import annotations

import argparse
import getpass
import sys

SERVICE_NAME = "giggle-gmail"


def _require_keyring():
    try:
        import keyring
    except ImportError as exc:  # pragma: no cover - runtime guidance
        raise SystemExit(
            "Missing dependency: keyring. Install it with `pip install keyring`."
        ) from exc
    return keyring


def save_password(email: str) -> None:
    keyring = _require_keyring()

    password = getpass.getpass("Enter Gmail app password (input is hidden): ")
    if not password:
        raise SystemExit("Password cannot be empty.")

    confirm = getpass.getpass("Confirm Gmail app password: ")
    if password != confirm:
        raise SystemExit("Passwords do not match.")

    keyring.set_password(SERVICE_NAME, email, password)
    print(f"Saved app password for {email} in your OS keychain.")


def load_password(email: str) -> str:
    keyring = _require_keyring()
    password = keyring.get_password(SERVICE_NAME, email)
    if password is None:
        raise SystemExit(
            "No saved app password found for this email. Run `save` first."
        )
    return password


def clear_password(email: str) -> None:
    keyring = _require_keyring()
    try:
        keyring.delete_password(SERVICE_NAME, email)
    except keyring.errors.PasswordDeleteError:
        raise SystemExit("No saved app password found to clear.")
    print(f"Removed saved app password for {email}.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Save Gmail app passwords securely in your OS keychain."
    )
    parser.add_argument("action", choices=["save", "load", "clear"])
    parser.add_argument("email", help="Gmail address (example: yourname@gmail.com)")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.action == "save":
        save_password(args.email)
        return 0

    if args.action == "load":
        password = load_password(args.email)
        sys.stdout.write(password)
        return 0

    clear_password(args.email)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
