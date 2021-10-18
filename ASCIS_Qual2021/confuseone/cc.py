from base64 import urlsafe_b64decode
from Crypto.Util.number import bytes_to_long, long_to_bytes
import gmpy2
from hashlib import sha256

def pkcs1_v1_5_encode(msg: bytes, n_len: int):
    SHA256_Digest_Info = b'\x30\x31\x30\x0D\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x01\x05\x00\x04\x20'
    T = SHA256_Digest_Info + sha256(msg).digest()
    PS = b'\xFF' * (n_len - len(T) - 3)
    return b'\x00\x01' + PS + b'\x00' + T

def get_magic(jwt):
    header, payload, signature = jwt.split(".")

    raw_signature = urlsafe_b64decode(f"{signature}==")
    raw_signature_int = gmpy2.mpz(bytes_to_long(raw_signature))

    # In RS256 we sign the base64 encoded header and payload padded using PKCS1 v1.5:
    padded_msg = pkcs1_v1_5_encode(f"{header}.{payload}".encode(), len(raw_signature))
    padded_int = gmpy2.mpz(bytes_to_long(padded_msg))

    return gmpy2.mpz(pow(raw_signature_int, e) - padded_int)

jwt0 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2MzQzNzM1NTAsIm5iZiI6MTYzNDM3NDU1MCwiZXhwIjoxNjM0Mzc5NTUwLCJkYXRhIjp7ImlkIjoiMTk5IiwidXNlcm5hbWUiOiJkdHJvMSIsImVtYWlsIjoiZHRyb0BnbWFpbC5jb20ifX0.Nthv83lruxdpQdqiGyD7RvSv8uVREp8a4_4wbYQ5Ecu-nfncONhYY2gHd_nQPeYcEO9U1ZfDVap4SSxn8ys9ZcyKNHGaxuv-sb37dN3YHGYM1XXZpFpZ7ijzUJb47-rXOOVNJk8fB0AHVDR2tnzkHwR4ytj6ILhgwlu29D6li6fU8C-WA4GN0vpInrIL2Ww4jEkQA_PzQxGSZAc60mFXSnyoMtDXHmFFtcCJm1y4auwcDK3Ph7qPjpF9lE4ueaSzDaD4HXcsiuq-ZrSgWGXcWJAiuxplfsnv7TnZ84GUTAGkl8sPFkd6iKElFMJegKqHx5JSjS2Uozf4eUaI7t58HA'
jwt1 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2MzQzNzQ1ODEsIm5iZiI6MTYzNDM3NTU4MSwiZXhwIjoxNjM0MzgwNTgxLCJkYXRhIjp7ImlkIjoiMTk5IiwidXNlcm5hbWUiOiJkdHJvMSIsImVtYWlsIjoiZHRyb0BnbWFpbC5jb20ifX0.mZXPVry2B29fxU7iQB_iluniWWEIG7OCpEwPiYmgqrlEAciZlg1GP-L4tHSDiK4k2tBjQSugSQ6K0KPwHqi1qrRwpm_Iu51kHu27Puw9DwbS3ZFZ1oo00K3mVqTTKLti0bOQNc_AjOba2RAOATChVxxJfh82lKcj5Zs8lBeOhDsq0sN6qVArSyC7UqqwBUecJhXWSHLbOqbUJC8d-qKhKpNq8rZ2klGJcNvVQCt__Zea90umDyFfYFhwIIU3aPnD02k2vdwRekZznonbPTy3n_vSdkq3yeznKOiaBNHkr7W79xECwymCF7dLc3s8b27F7ju2weH1BiogOmDybJoXdQ'

jwt0 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2MzQzNzgzNDgsIm5iZiI6MTYzNDM3OTM0OCwiZXhwIjoxNjM0Mzg0MzQ4LCJkYXRhIjp7ImlkIjoiNjYiLCJ1c2VybmFtZSI6ImdudWRuYW9kIiwiZW1haWwiOiJnbnVkbmFvZEBnbWFpbC5jb20ifX0.M8o3alD1URK_vrndiFhKRNs_ZrKBLb3iqzKvBHDrVnQ4a1O5TLHYLYCVlThxXX_far6xYI_aAjkyoQMiJzyhZyaHmmCq0zNx2hY3tY1MO9mq-D3j0bGhQRIQppuEWBDjnKOApkH5BKFaf404xxuCuD3sJz-SywZEwbMY60L93A3taozoeJmRPvqJrD_RUdmPtRI0FuS3dg8eWbEl1jLhLnD8Oa--LPi6YuQ1FLvTZtQADfqvoF_3FXq0h6S6R_HlmzNy4kMQu9t04QPnuCHK9ko_mSq4BGjMzEuxKKLEHlDr1-bfBglIqGmvEnBB_bJDZ7bC7lWripvt0SMaY5VyYA'
jwt1 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2MzQzNzg3MzksIm5iZiI6MTYzNDM3OTczOSwiZXhwIjoxNjM0Mzg0NzM5LCJkYXRhIjp7ImlkIjoiNjYiLCJ1c2VybmFtZSI6ImdudWRuYW9kIiwiZW1haWwiOiJnbnVkbmFvZEBnbWFpbC5jb20ifX0.nzy_G8kixpMT9WU8U2A2uiw83gZazka2AFrMZ3-m146Gij07L-efH3qphcqCqWEi_ZQ3hdjGqEj7FdahaV5GWrILuz_Ze_VeM5FYqYurvXCSbzGJ5aoJU6kIHNyZTsomO32Y1HgKkgSliIZll1GfqR3LXbOYegOB0OfXl1I2tUbMxnNp7J5tghTLsH4MjP0K4c9pB4-jPF0b4zbFW6HQBFhOmJRe6639VfSU_hryvgDspmgmhDMFcO5DV_60OKLTOpPfRB4VDPsRZ-l3Vgmu-gKFr1BlqvYgVYfZ07DtGfpIANkADToaJx7zVSsgrTWDfW33P0xftI9rQZDln5gBvA'
e = gmpy2.mpz(65537)

magic0 = get_magic(jwt0)
magic1 = get_magic(jwt1)
N = gmpy2.gcd(magic0, magic1)
assert N != 1
print(e)
print(hex(N))
