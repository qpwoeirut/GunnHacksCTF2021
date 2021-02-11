all:
	gcc -s -z execstack -fno-stack-protector -no-pie -m32 main.c lemon.S -o lemongallery -nostdlib -masm=intel
	strip lemongallery -S --strip-unneeded --remove-section=.note.gnu.gold-version --remove-section=.comment --remove-section=.note --remove-section=.note.gnu.build-id --remove-section=.note.ABI-tag --strip-all
