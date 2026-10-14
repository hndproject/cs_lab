# Use static analysis tools to find how an executable can be analyzed

import dis

# Global variable
global_flag = "LAB_SECRET_KEY_9921"


def helper_function():
    print("[+] Inside helper_function()")


def main():
    message = "Static analysis lab sample"

    print(message)
    helper_function()


if __name__ == "__main__":
    main()

    print("\n=== Static Analysis: Global Variables ===")
    print("Global Flag:", global_flag)

    print("\n=== Static Analysis: Function Names ===")
    print(main.__name__)
    print(helper_function.__name__)

    print("\n=== Static Analysis: Main Function Bytecode ===")
    dis.dis(main)
