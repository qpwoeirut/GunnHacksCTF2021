from hacksport.problem import Remote, File, ProtectedFile

class Problem(Remote):
    program_name = "repeated_message.py"
    files = [File("repeated_message.py"), ProtectedFile("flag.txt")]

    def generate_flag(self, random):
        hexdigits = hex(random.randrange(16 ** 8))[2:]
        return "gunnHacks{sm0l_e_strikes_again_" + hexdigits + '}'
