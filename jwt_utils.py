import jwt
import settings
from jwt_utils import decode_jwt

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


