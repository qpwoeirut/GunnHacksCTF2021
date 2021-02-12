from hacksport.problem import Remote

class Problem(Remote):
    program_name = "intro_to_netcat.py"

    def generate_flag(self, random):
        hexdigits = hex(random.randrange(16 ** 8))[2:]
        return "gunnHacks{int3rn3t_c4t$_" + hexdigits + '}'
