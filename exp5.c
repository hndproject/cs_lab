//Buffer overflow, integer overflow and format string vulnerability testing in vulnerable applications.

// gcc exp5.c -o exp5.exe
// .\exp5.exe

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

void buffer_demo(void) {
    char buf[16];

    printf("\n--- 1. Bounded Buffer Overflow Mitigation ---\n");
    printf("Enter input text (max 15 chars): ");

    if (fgets(buf, sizeof(buf), stdin) != NULL) {
        buf[strcspn(buf, "\n")] = '\0';

        printf("[+] Bounded Buffer Content: %s\n", buf);
        printf("[+] String Length: %zu bytes (Safe from stack overflow)\n",
               strlen(buf));
    }
}

void integer_demo(void) {
    printf("\n--- 2. Integer Overflow & Wrap-Around ---\n");

    unsigned int max_uint = UINT_MAX;

    printf("[+] Max Unsigned Int (UINT_MAX) : %u\n", max_uint);
    printf("[+] UINT_MAX + 1 (Wrap-around)  : %u\n", max_uint + 1u);

    unsigned short short_val = USHRT_MAX;

    printf("[+] Max Unsigned Short (USHRT_MAX): %u\n",
           (unsigned int)short_val);

    printf("[+] USHRT_MAX + 1 (Wrap-around) : %u\n",
           (unsigned short)(short_val + 1u));
}

void format_demo(void) {
    char input[64];

    printf("\n--- 3. Format String Vulnerability Testing ---\n");
    printf("Enter string with format specifiers (e.g., hello %%x %%p): ");

    if (fgets(input, sizeof(input), stdin) != NULL) {
        input[strcspn(input, "\n")] = '\0';

        printf("\n[!] UNSAFE PATTERN: printf(input);\n");
        printf("    -> Risk: User-controlled format specifiers can cause undefined behavior.\n");

        printf("[+] SAFE PATTERN  : printf(\"%%s\\n\", input);\n");
        printf("    -> Safe Output: %s\n", input);
    }
}

int main(void) {
    puts("==================================================");
    puts("=== Memory & Input Vulnerability Demonstration ===");
    puts("==================================================");

    buffer_demo();
    integer_demo();
    format_demo();

    puts("\n==================================================");

    return 0;
}