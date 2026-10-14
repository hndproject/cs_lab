//Use static analysis tools to find how an executable can be analyzed

#include <stdio.h>

const char *global_flag = "LAB_SECRET_KEY_9921";

void helper_function(void) {
    puts("[+] Inside helper_function()");
}

int main(void) {
    const char *message = "Static analysis lab sample";

    printf("%s\n", message);
    helper_function();

    return 0;
}
