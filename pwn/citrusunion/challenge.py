from hacksport.problem import Compiled, Remote, ProtectedFile

class Problem(Compiled, Remote):
   def generate_flag(self, random):
      hexdigits = hex(random.randrange(16 ** 8))[2:]
      return "gunnHacks{t0xic_r0p_t@mes_th3_lem0n_cr0p_" + hexdigits + '}'

   makefile = "Makefile"
   program_name = "citrusunion"
   aslr = False
   remote = True
   files = [ProtectedFile("flag.txt")]
