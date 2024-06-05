import bcrypt


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed


def check_password(hashed, password):
    return bcrypt.checkpw(password.encode("utf-8"), hashed)


if __name__ == "__main__":
    password = "MinhaSenhaSegura123"
    hashed_password = hash_password(password)
    print("Senha Hasheada:", hashed_password)

    is_correct = check_password(hashed_password, password)
    print("Senha Correta?", is_correct)
