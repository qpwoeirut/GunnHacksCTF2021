#include "syscalls.h"
char* lemon = "\xff\xe1";

void vuln() {
char buf[32];
read(0, buf, 48);
}

int main() {
vuln();
}
