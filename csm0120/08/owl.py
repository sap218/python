class Owl:

    def __init__(self,common_name="owl",sound="hoot",location=None,ring_number=None,wing_span=None):
        self.common_name = common_name
        self.sound = sound
        self.location = location
        self.ring_number = ring_number
        self.wing_span = wing_span

    def get_info(self):
        if self.wing_span is None:
            text = "%s makes a %s sound" % (self.common_name, self.sound)
        else:
            text = "%s makes a %s sound and has wingspan of %f" % (self.common_name, self.sound, self.wing_span) 
        return text

    def has_ring(self):
        if self.ring_number == None:
            return False
        else:
            return True

    
if __name__ == "__main__":
    # make new objects of the Owl class
    ceri = Owl("tawny owl", "twit twoo", "tree", 123)
    dyfi = Owl("barn owl", "shriek", "barn", wing_span=5.332)
    cati = Owl("tawny owl", "hoohoo", ring_number=345)

    # access a variable
    print(ceri.ring_number)
    ceri.ring_number = 53
    print(ceri.ring_number)

    # call a function
    print(dyfi.get_info())
    print(Owl.get_info(cati))
    print(ceri.get_info())

    print(Owl.has_ring(ceri))
    print(Owl.has_ring(dyfi))
    print(Owl.has_ring(cati))