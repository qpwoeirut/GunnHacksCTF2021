from hacksport.problem import Challenge, File


class Problem(Challenge):
    files = [File("img1.jpg"), File("img2.jpg"), File("img3.jpg"), File("img4.jpg"), File("img5.jpg"), File("img6.jpg"), File("img7.jpg")]

    def generate_flag(self, random):
        return "gunnHacks{geotags}"
