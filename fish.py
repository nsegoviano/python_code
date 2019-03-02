class Fish:
    def __init__(self, first_name, last_name="Fish", skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swin(self):
        print("The fish is swiming.")
   
    def swin_backwards(self):
        print("The fish can swim backwards.")

