from hacksport.problem import PHPApp, PreTemplatedFile, files_from_directory


class Problem(PHPApp):
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


