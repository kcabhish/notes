# Cryptography

Encryptd information is difficult to break and anlyze by attackers. Cryptography comes in three catagories:
- Storing sensetive data
- algorithims
- protecting keys.

## Data

If possible, don;t store sensitive data.

If data must be stored, never store it in lain text. Alos, disable caching and encrypt the data.

If you are using one-way hashes, add a salt to the data to prevent automated attacks. Strong functions include: Argon2, scrypt, bcrypt and PBKDF2.

## Algorithms

Make sure you don;t use algorithms that have known weaknesses. Use cryptographically strong APIs provided by your programming language.

| Algorithm | Status | Best Practice |
|-----------|--------|---------------|
|MD5/SHA1   | Weak/Broken| Don't use|
|Data Encryption Standard (DES)| Weak/Broken|Don't use|
|Advanced Encryption Standard (AES) | Strong Standard | >=128-bits |
|SHA256 | Strong Standard | >256-bits |

## Keys

Use Cryptographically Secure PseudoRandom Number Generators (CSPRNG) to create your private keys.
Avoid weaj gebratirs because they might b unscrambled by attackers.