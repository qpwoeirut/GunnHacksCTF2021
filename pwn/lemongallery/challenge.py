from hacksport.problem import Compiled, Remote, ProtectedFile

class Problem(Compiled, Remote):
   def generate_flag(self, random):
      hexdigits = hex(random.randrange(16 ** 8))[2:]
      return "gunnHacks{m0p_ch0p_plop_y0ur_w@y_t0_th3_bergam0t_" + hexdigits + '}'

   makefile = "Makefile"
   program_name = "lemongallery"
   aslr = False
   remote = True
   files = [ProtectedFile("flag.txt")]
