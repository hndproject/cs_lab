#Exercise on privilege escalation example

class SystemUser:
    def __init__(self, username: str, role: str):
        self.username = username
        self.role = role

    def request_admin_action(self, action_name: str) -> bool:
        print(f"\n[+] User: '{self.username}' | Assigned Role: '{self.role}'")
        print(f"    Action Requested: {action_name}")

        if self.role == "labadmin":
            print("    [RESULT] Access Granted. Administrative privilege confirmed.")
            return True
        else:
            print("    [RESULT] Access Denied. Insufficient privileges.")
            print("    [NOTE] Privilege escalation requires authorized authentication.")
            return False

    def elevate_privileges(self, token: str) -> None:
        print(f"\n[*] Attempting privilege escalation for '{self.username}'...")

        if token == "AUTH_ADMIN_SECRET":
            self.role = "labadmin"
            print(f"    [SUCCESS] Valid token. Role successfully escalated to: '{self.role}'")
        else:
            print("    [FAILED] Invalid authorization token. Privilege escalation denied.")


def main():
    print("==================================================")
    print("=== Privilege Escalation Simulation (RBAC Lab) ===")
    print("==================================================")

    # Step 1: Standard user attempts admin operation
    user1 = SystemUser("student_user", "student")
    user1.request_admin_action("Update System Policy")

    # Step 2: Failed escalation attempt with invalid credentials
    user1.elevate_privileges("wrong_token")
    user1.request_admin_action("Update System Policy")

    # Step 3: Authorized privilege escalation
    user1.elevate_privileges("AUTH_ADMIN_SECRET")
    user1.request_admin_action("Update System Policy")

    # Step 4: Pre-authorized administrator access
    admin = SystemUser("labadmin_user", "labadmin")
    admin.request_admin_action("Restart Network Service")


if __name__ == "__main__":
    main()