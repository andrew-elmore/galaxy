from numpy import random
import math




class System:
    def __init__(self, name, radius):

        r = random.randint((radius* -1), radius)
        x = int(round(random.uniform((-1 * r), r)))
        y = int(round(math.sqrt((r ** 2) - (x ** 2)) * random.uniform(-1, 1)))

        self.name = name
        self.radius = r
        self.x = x
        self.y = y
        self.planet_type = 'unknown'
        self.owner = 'none'
        self.value = max(random.normal(50, 25), 1)
        self.development = 0
        self.parents = []
        self.children = []
        
    def findClosestStars(self, stars):
        sorted_stars = stars
        def by_distance(star):
            return star.findDistance(self)
        
        sorted_stars.sort(key=by_distance)
        return sorted_stars

    def findDistance(self, star):
        dist_x = abs(self.x - star.x)
        dist_y = abs(self.y - star.y)
        dist = math.sqrt(dist_x ** 2 + dist_y ** 2)
        return dist
    
    def addParent(self, star):
        self.parents.append(star)
        star.addChild(self)

    def addChild(self, star):
        self.children.append(star)

    def inhabit(self, culture):
        if self.owner == 'none':
            self.owner = culture
            return True
        else:
            if self.owner.agression * culture.agression > 2500:
                if len(self.owner.inhabited_stars) < len(culture.inhabited_stars):
                    return False
                else:
                    self.owner.looseSystem(self)
                    self.owner = culture
                    return True
            else: 
                return False


    def integrate(self, stars, owner):
        i = 0
        unintergrated = True
        while unintergrated:
            # print('integrate: ', self.findClosestStars(stars))
            # print('integrate: ', i)

            star = self.findClosestStars(stars)[i]
            if (star.owner == owner and star != self):
                self.addParent(star)
                unintergrated = False
            i += 1
            if (i == len(stars)):
                unintergrated = False

    def paint(self, scale, radius, cv2, img, chosen_color):
        star_x = int((self.x / scale)+(radius/scale))
        star_y = int((self.y / scale)+(radius/scale))
        # print(self.value)
        cv2.circle(img, (star_x, star_y), int(1/scale), (255, 255, 255), -1)
        if self.owner != 'none':
            color = self.owner.color
            cv2.circle(img, (star_x, star_y), int(self.value/scale)+2, color, 1)
            if chosen_color != None:
                cv2.circle(img, (star_x, star_y), int(100/scale)+2, chosen_color, 5)
        for child in self.children:
            child_x = int((child.x / scale)+(radius/scale))
            child_y = int((child.y / scale)+(radius/scale))
            cv2.line(img, (star_x, star_y), (child_x, child_y), color, 1)
