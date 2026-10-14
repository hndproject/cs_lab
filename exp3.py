#Exercise on 2 factor authentication

import hmac
import hashlib
import time
import struct


def generate_totp(secret, time_step=30, digits=6):
    key = secret.encode()
    counter = int(time.time() // time_step)

    msg = struct.pack(">Q", counter)
    hmac_digest = hmac.new(key, msg, hashlib.sha1).digest()

    offset = hmac_digest[-1] & 0x0F

    binary_code = (
        ((hmac_digest[offset] & 0x7F) << 24)
        | ((hmac_digest[offset + 1] & 0xFF) << 16)
        | ((hmac_digest[offset + 2] & 0xFF) << 8)
        | (hmac_digest[offset + 3] & 0xFF)
    )

    otp = binary_code % (10 ** digits)

    return str(otp).zfill(digits)


if __name__ == "__main__":
    secret_key = "JBSWY3DPEHPK3PXP"

    totp = generate_totp(secret_key)

    print(f"Secret Key: {secret_key}")
    print(f"Generated 2FA Code (TOTP): {totp}")

    user_input = input("Enter OTP for Verification: ")

    if user_input == totp:
        print("[SUCCESS] 2FA Authentication Successful!")
    else:
        print("[FAILED] Invalid OTP Code.")