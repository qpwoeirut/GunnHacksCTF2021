all:
	gcc -s -z execstack -fno-stack-protector -no-pie -m32 main.c lemon.S -o lemongallery -nostdlib -masm=intel
	strip lemongallery
