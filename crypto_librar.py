
import hashlib

from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(value: str) -> str:
    hash = context.hash(value)
    print(hash)
    return hash


def verify_password(plain_password: str, hashed_password: str) -> bool:
    result = context.verify(plain_password, hashed_password)
    print(result)
    return result


data = get_password_hash("password")
verification = verify_password("password", data)


def encode_md5(value: str) -> str:
    hash = hashlib.md5(value.encode()).hexdigest()
    return hash
