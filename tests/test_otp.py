"""Test cases for the otp module."""

import binascii

import pytest

from otp import get_hmac_based_otp, get_secret_key, get_time_based_otp


def test_get_secret_key() -> None:
    """Test the generation of a secret key."""
    key = get_secret_key()
    assert len(key) == 32

    assert get_secret_key("abcdefgh") == b"\x00D2\x14\xc7"

    for secret in ["a", "1"]:
        with pytest.raises(binascii.Error):
            get_secret_key(secret)


def test_get_hmac_based_otp() -> None:
    """Test the generation of HMAC-based OTPs against RFC 4226 test vectors."""
    secret = b"12345678901234567890"
    test_vectors = [
        (0, "755224"),
        (1, "287082"),
        (2, "359152"),
        (3, "969429"),
        (4, "338314"),
        (5, "254676"),
        (6, "287922"),
        (7, "162583"),
        (8, "399871"),
        (9, "520489"),
    ]

    for counter, expected_otp in test_vectors:
        assert get_hmac_based_otp(secret, counter) == expected_otp


def test_get_time_based_otp() -> None:
    """Test the generation of time-based OTPs against RFC 6238 test vectors."""
    secret = b"12345678901234567890"
    test_vectors = [
        (59, "94287082"),
        (1111111109, "07081804"),
        (1111111111, "14050471"),
        (1234567890, "89005924"),
        (2000000000, "69279037"),
        (20000000000, "65353130"),
    ]

    for unix_time, expected_otp in test_vectors:
        result = get_time_based_otp(secret, unix_time=unix_time, digit=8)
        assert result == expected_otp
