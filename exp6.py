#6. DVWA based command injection. SQL injection, XSS and CSRF

import html
import shlex
import subprocess


def test_command_injection(user_input: str) -> None:
    print("\n--- 1. Command Injection Testing ---")
    print(f"Input: '{user_input}'")

    # Vulnerable pattern (display only)
    vulnerable_cmd = f"ping -c 1 {user_input}"
    print(f"[UNSAFE Execution Command]: {vulnerable_cmd}")

    # Safer demonstration: use an argument list without a shell
    safe_target = user_input.split()[0]
    safe_cmd = ["ping", "-c", "1", safe_target]

    print(f"[SAFE Execution Command]  : {safe_cmd}")


def test_sql_injection(user_input: str) -> None:
    print("\n--- 2. SQL Injection Testing ---")
    print(f"Input: '{user_input}'")

    # Vulnerable dynamic SQL (display only)
    unsafe_query = (
        f"SELECT * FROM users WHERE user_id = '{user_input}';"
    )
    print(f"[UNSAFE Dynamic Query]: {unsafe_query}")

    # Remediation: parameterized query
    print("[SAFE Parameterized Query]: SELECT * FROM users WHERE user_id = ?;")


def test_xss(user_input: str) -> None:
    print("\n--- 3. Reflected Cross-Site Scripting (XSS) ---")
    print(f"Raw Input: {user_input}")

    # Vulnerable output (display only)
    print(f"[UNSAFE HTML Render]: <div>Hello {user_input}</div>")

    # Remediation: HTML entity encoding
    safe_output = html.escape(user_input)
    print(f"[SAFE Encoded Output]: <div>Hello {safe_output}</div>")


def test_csrf(token_provided: bool) -> None:
    print("\n--- 4. Cross-Site Request Forgery (CSRF) ---")

    if token_provided:
        print("[+] Request contains valid Anti-CSRF Token.")
        print("[+] Action: Password change accepted.")
    else:
        print("[!] Missing Anti-CSRF Token!")
        print("[!] Action: Request rejected (403 Forbidden).")


def main():
    print("=== DVWA Vulnerability Analysis Simulation ===")

    test_command_injection("127.0.0.1; cat /etc/passwd")
    test_sql_injection("' OR '1'='1")
    test_xss("<script>alert('XSS')</script>")
    test_csrf(token_provided=False)
    test_csrf(token_provided=True)


if __name__ == "__main__":
    main()
