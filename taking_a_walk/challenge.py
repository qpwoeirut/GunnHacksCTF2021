from hacksport.problem import Challenge, File


class Problem(Challenge):
    files = [File("img.zip")]

    def generate_flag(self, random):
        return "gunnHacks{geotags}"
    def setup(self):
        print("pepega")
