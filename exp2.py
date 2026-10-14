#Taking apart a digital certificate and show the various components and their significance.
#python -m pip install pyOpenSSL

import ssl
import OpenSSL
from datetime import datetime


def analyze_cert(hostname, port=443):
    cert_pem = ssl.get_server_certificate((hostname, port))

    x509 = OpenSSL.crypto.load_certificate(
        OpenSSL.crypto.FILETYPE_PEM, cert_pem
    )

    print("================ DIGITAL CERTIFICATE ANALYSIS ================")

    print(f"[+] Subject Name       : {dict(x509.get_subject().get_components())}")
    print(f"[+] Issuer Name        : {dict(x509.get_issuer().get_components())}")
    print(f"[+] Serial Number      : {x509.get_serial_number()}")
    print(f"[+] Version            : {x509.get_version() + 1}")
    print(f"[+] Signature Algo     : {x509.get_signature_algorithm().decode()}")
    print(f"[+] Valid From         : {x509.get_notBefore().decode()}")
    print(f"[+] Valid Until        : {x509.get_notAfter().decode()}")
    print(f"[+] Public Key Length  : {x509.get_pubkey().bits()} bits")

    print("===============================================================")


if __name__ == "__main__":
    analyze_cert("example.com")
