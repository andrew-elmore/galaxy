# importing the required module 
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt 
from numpy import random
import math
import time
from systems import System
from cultures import Culture
import cv2
from datetime import datetime











class Galaxy:
    def __init__(self, num_stars, num_cultures, img, scale, radius):
        self.scale = scale
        self.radius = radius
        self.stars = []
        self.cultures = []
        self.year = 2100
        self.num_cultures = num_cultures
        self.plt = plt
        self.img = img
        self.createSystems(num_stars)
        self.createCultures()

    def yearPass(self):
        duration = 1
        self.year += duration
        for culture in self.cultures:
            culture.gatherResources(self.year, duration)
            culture.colonizeStars(self.year, self.stars)

    def paintGalaxy(self):
        for culture in self.cultures:
            pass
            # self.paintCultureHomeworld(culture)

        for star in self.stars:
            star.paint(self.scale, self.radius, cv2, self.img, None)



    def createSystems(self, num_stars):
        for x in range(0, num_stars):
            system = System(x, self.radius)
            if system.radius < self.radius:
                self.stars.append(system)


    def findClosestStars(self):
        for star in self.stars:
            star.findClosestStars(self.stars)
        

    def createCultures(self):
        culture_colors = [
                    (0, 0, 255),
                    (0, 255, 0),
                    (255, 0, 0),
                    (0, 255, 255),
                    (255, 0, 255),
                    (255, 255, 0)
                ]
        for i in range(0, self.num_cultures):
            red = random.uniform(0, 1)
            green = random.uniform(0, 1)
            blue = random.uniform(0, 1)
            a = 1
            homeworld = self.stars[random.randint(0, len(self.stars))]
            culture = Culture(homeworld, culture_colors[i])
            self.cultures.append(culture)



    def paintCulture(self, culture):
        homeworld = culture.homeworld
        culture_homeworld = self.plt.Circle((homeworld.x, homeworld.y), radius=culture.sphier_of_influence, color='lightBlue')
        self.plt.gca().add_patch(culture_homeworld)





scale = 100
radius = int(52850)

img = Image.new("RGB", (int(radius/scale*2), int(radius/scale*2)))
img.save('galaxy.png')
img = cv2.imread('galaxy.png')


def show():
    galaxy_1 = Galaxy(1000, 1, img, scale, radius)
    while True:
        # print (galaxy_1.year)
        galaxy_1.paintGalaxy()
        cv2.imshow('Galaxy', img)
        print(galaxy_1.year)
        time.sleep(0.5)
        galaxy_1.yearPass()

        key = cv2.waitKey(1) & 0xff
        if key == ord('q'):  # ESC
            print('end')
            break
        # elif key == ord('w'):
        #     galaxy_1.yearPass()
        elif key == ord('a'):
            culture = galaxy_1.cultures[0]
            
            frontline = culture.findFrontLine()
            for star in frontline:
                star.paint(galaxy_1.scale, galaxy_1.radius, cv2, galaxy_1.img,  (255, 0, 0))
            print(frontline)


    cv2.destroyAllWindows()


def chart():
    for i in range(0, 50):
        galaxy_1 = Galaxy(1000, 1, img, scale, radius)

        galaxy_1.findClosestStars()

        print(i)


        year_data = []
        stars_data = []
        year_data.append(galaxy_1.year)
        stars_data.append(len(galaxy_1.cultures[0].inhabited_stars))
        while(len(galaxy_1.cultures[0].inhabited_stars) < 999 and galaxy_1.year < 5000):
            # print(galaxy_1.year)
            # print(len(galaxy_1.cultures[0].inhabited_stars))
            galaxy_1.yearPass()
            year_data.append(galaxy_1.year)
            stars_data.append(len(galaxy_1.cultures[0].inhabited_stars))


        # print(year_data)
        # print(stars_data)
        plt.plot(year_data, stars_data, label=i)


    plt.legend()
    plt.show()


show()
# chart()



