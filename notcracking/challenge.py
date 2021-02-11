from hacksport.problem import PHPApp, ProtectedFile, files_from_directory


class Problem(PHPApp):
  files = files_from_directory("webroot/") + [ProtectedFile("flag.txt")]
  php_root = "webroot/"
