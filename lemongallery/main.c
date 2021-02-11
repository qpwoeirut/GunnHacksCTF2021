#include <unistd.h>

char* fuckyougcc = "pepega";
char* lemon = "\xff\xe1";

void vuln() {
char buf[32];
read(STDIN_FILENO, buf, 256);
}

int main() {
vuln();
}
