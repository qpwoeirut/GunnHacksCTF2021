from hacksport.problem import PHPApp, ProtectedFile, files_from_directory


class Problem(PHPApp):
  def generate_flag(self, random):
      hexdigits = hex(random.randrange(16 ** 8))[2:]
      return "gunnHacks{sti1l_b3tter_than_n0de_" + hexdigits + '}'
  files = files_from_directory("webroot/") + [ProtectedFile("flag.txt")]
  php_root = "webroot/"
