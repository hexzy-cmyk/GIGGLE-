# GIGGLE-

A tiny helper for storing a Gmail app password in your OS keychain so you do not need to type it in plain text anymore.

## Why this exists

Google no longer allows most accounts to use the normal Gmail account password for apps.
Use a **Gmail App Password** and store it securely.

## Setup

```bash
python3 -m pip install keyring
```

## Usage

Save a Gmail app password (input is hidden):

```bash
python3 gmail_password_vault.py save yourname@gmail.com
```

Load the password for use in scripts (do not print it unless needed):

```bash
python3 gmail_password_vault.py load yourname@gmail.com
```

Clear a saved password:

```bash
python3 gmail_password_vault.py clear yourname@gmail.com
```

## Note

This stores secrets in the OS keychain through `keyring` instead of hardcoding credentials in code or text files.
