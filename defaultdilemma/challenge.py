from hacksport.problem import PHPApp, PreTemplatedFile, files_from_directory


class Problem(PHPApp):
  def generate_flag(self, random):
      hexdigits = hex(random.randrange(16 ** 8))[2:]
      return "gunnHacks{f0und_it_" + hexdigits + '}'
  files = files_from_directory("webroot/")
  PreTemplatedFile("assets/img/portfolio/safe.png")
  PreTemplatedFile("assets/img/portfolio/game.png")
  PreTemplatedFile("assets/img/portfolio/cabin.png")
  PreTemplatedFile("assets/img/portfolio/submarine.png")
  PreTemplatedFile("assets/bootstrap/css/bootstrap.min.css")
  PreTemplatedFile("assets/fonts/fontawesome-webfont.eot")
  PreTemplatedFile("assets/fonts/fontawesome-webfont.woff2")
  PreTemplatedFile("assets/fonts/fontawesome-webfont.woff")
  PreTemplatedFile("assets/fonts/fontawesome-webfont.ttf")
  php_root = "webroot/"


