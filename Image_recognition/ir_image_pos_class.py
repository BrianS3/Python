class image_pos():
    def __init__(self, imgwidth, imgheight):
        self.x = 0
        self.y = 0
        self.image_height = imgheight
        self.image_width = imgwidth

    def create_positions(self):
        positions = []
        for ix in range(0, self.image_width):
            for iy in range(0,self.image_height):
                self.x = ix
                self.y = iy
                positions.append((self.x,self.y))
        return positions

test1 = image_pos(800,450)
pos = test1.create_positions()
print(len(pos))
print(pos[1:10])
#(0, 1)
print(pos[2])
#(0,2)
#print(pos[245879])
#(546,179)

for tup in pos[1:10]:
    print(tup)