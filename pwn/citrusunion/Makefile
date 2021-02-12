all:
	gcc -s -fno-stack-protector -no-pie main.S -o citrusunion -nostdlib -masm=intel -z noexecstack
	strip citrusunion --remove-section=.got.plt --remove-section=.eh_frame_hdr --remove-section=.eh_frame --remove-section=.note.gnu.gold-version --remove-section=.comment --remove-section=.note --remove-section=.note.gnu.build-id --remove-section=.note.ABI-tag --strip-all
	sstrip citrusunion
