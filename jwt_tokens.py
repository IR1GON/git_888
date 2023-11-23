import datetime
import jwt
import settings

def decode_jwt(encoded_token):
    try:
        decoded = jwt.decode(
            encoded_token,
            settings.JWT_SECRET,
            algorithms=["HS256"],
            # options={
            #     'verify_signature': False,
            # }
        )
        return decoded
    except jwt.ExpiredSignatureError:
        print("Expired token. Please generate a new one.")
        return None
    except jwt.InvalidTokenError:
        print("Invalid token. Unable to decode.")
        return None

def generate_and_decode_jwt():
    payload = {
        "my_name": "Vasyl",
        "age": 10,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60),
    }


    encode_jwt = jwt.encode(
        payload=payload,
        key=settings.JWT_SECRET,
        algorithm="HS256",
    )
    print("Encoded JWT:", encode_jwt)

    decoded_token = decode_jwt(encode_jwt)

    if decoded_token:
        print("Decoded JWT:", decoded_token)
    else:
        print("Token decoding failed.")


generate_and_decode_jwt()
