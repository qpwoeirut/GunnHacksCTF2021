from hacksport.problem import Remote, File, ProtectedFile

class Problem(Remote):
    program_name = "rsa5.py"
    files = [File("rsa5.py"), ProtectedFile("flag.txt")]

    def generate_flag(self, random):
        hexdigits = hex(random.randrange(16 ** 8))[2:]
        return "gunnHacks{sm0l_e_strikes_again_" + hexdigits + '}'
