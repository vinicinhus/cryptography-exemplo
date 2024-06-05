import hashlib


def hash_file(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


if __name__ == "__main__":
    file_name = r"src\hashing\sha256\arquivo_baixado.zip"
    hash_value = hash_file(file_name)
    print("Hash SHA-256 do arquivo:", hash_value)

    # Comparar com o hash fornecido pelo site
    expected_hash = "valor_do_hash_fornecido_pelo_site"
    if hash_value == expected_hash:
        print("O arquivo está íntegro.")
    else:
        print("O arquivo foi corrompido.")
