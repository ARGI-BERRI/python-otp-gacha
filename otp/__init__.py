"""Simple HOTP (based on RFC 4226) and TOTP (based on RFC 6238) generators.

For HOTP, see: https://datatracker.ietf.org/doc/html/rfc4226/.
For TOTP, see: https://datatracker.ietf.org/doc/html/rfc6238/.
"""

import base64
import hashlib
import hmac
import secrets
import time


def get_secret_key(secret: str | None = None, key_length: int = 20) -> bytes:
    """Get a secret key for OTP generation.

    Args:
        secret (str | None, optional): The base32-encoded secret key. Defaults to None.
        key_length (int, optional): The length of the generated key in bytes. Defaults to 20.

    Returns:
        bytes: The decoded or newly generated secret key.

    Raises:
        binascii.Error: If the `secret` is not valid base32.
    """
    if secret:
        if (missing_padding := len(secret) % 8) != 0:
            return base64.b32decode(f"{secret}{'=' * (8 - missing_padding)}", casefold=True)

        return base64.b32decode(secret, casefold=True)

    return base64.b32encode(secrets.token_bytes(key_length))


def get_hmac_based_otp(secret_key: bytes, counter: int, *, digit: int = 6) -> str:
    """Generate an HMAC-based OTP.

    Args:
        secret_key (bytes): The secret key used for HMAC.
        counter (int): The counter value (e.g., time step).
        digit (int, optional): The number of digits in the OTP. Defaults to 6.

    Returns:
        str: The generated OTP.
    """
    digest = hmac.new(secret_key, counter.to_bytes(8, byteorder="big"), hashlib.sha1).digest()
    offset = digest[-1] & 0xF
    otp_full = int.from_bytes(digest[offset : offset + 4], byteorder="big") & 0x7FFFFFFF

    return str(otp_full % (10**digit)).zfill(digit)


def get_time_based_otp(
    secret_key: bytes,
    *,
    unix_time: float | None = None,
    time_step: int = 30,
    digit: int = 6,
) -> str:
    """Generate a time-based OTP.

    Args:
        secret_key (bytes): The secret key used for HMAC.
        unix_time (float | None, optional): The Unix time to use. Defaults to None.
        time_step (int, optional): The time step in seconds. Defaults to otp_config.time_step.
        digit (int, optional): The number of digits in the OTP. Defaults to 6.

    Returns:
        str: The generated OTP.
    """
    step = int(unix_time if unix_time is not None else time.time()) // time_step
    return get_hmac_based_otp(secret_key, step, digit=digit)
