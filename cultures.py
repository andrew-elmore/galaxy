from numpy import random
import math
from economy import Economy



class Culture:
    def __init__(self, homeworld, color):
        self.homeworld = homeworld
        # self.expantion_inclanation = random.uniform(0, 100)
        self.expantion_inclanation = 40
        self.development_inclanation = 40
        self.consumption_inclanation = 20
        self.scanned_stars = [homeworld]
        self.inhabited_stars = [homeworld]
        self.color = color
        self.agression = 90
        self.economy = Economy(self.inhabited_stars)
        self.front_line = []
        self.resources = 10000
        self.annual_resources = homeworld.value
        self.network_upkeep = 0
        homeworld.inhabit(self)


    def colonizeStars(self, year, stars):
        print('val:', int(self.resources))
        expantion_budget = (self.resources - self.network_upkeep)* (self.expantion_inclanation / 100) 
        # print('network_upkeep', self.network_upkeep)
        # print('expantion_budget', expantion_budget)
        # expantion_budget = 52850/5
        targets = {}
        frontline = self.findFrontLine()
        for star_1 in frontline:
            passed_capacity = False
            used_budget = 0
            i = 0
            closest_stars = star_1.findClosestStars(stars)
            while(not passed_capacity and i < len(closest_stars)):
                # print('colonizeStars: ', star_1.findClosestStars(stars))
                # print('colonizeStars: ', i )
                star_2 = closest_stars[i]
                distance = star_1.findDistance(star_2) 
                benifit = distance / star_2.value
                if (star_2.owner != self and benifit < expantion_budget and used_budget < expantion_budget):
                    if targets.get(star_2) == None:
                        targets[star_2] = distance
                        used_budget += distance
                    else:
                        targets[star_2] = min(distance, targets.get(star_2))
                elif(benifit >= expantion_budget or used_budget >= expantion_budget):
                    passed_capacity = True
                i += 1
                   
        # print('targets', len(targets))
        def by_distance(star):
            return targets.get(star)
        target_locations = list(targets.keys())
        target_locations.sort(key=by_distance)

        i = 0
        while(expantion_budget > 0 and i < len(targets)):
            target = target_locations[i]
            if target.inhabit(self):
                self.inhabited_stars.append(target)
                self.annual_resources += target.value
                target.integrate(stars, self)
                expantion_budget -= (targets[target])
                self.network_upkeep += targets[target]
            i += 1


 
        return (self.inhabited_stars)

    def takeAction(self, year, stars, duration):
        self.gatherResources(year, duration)
        self.colonizeStars(year, stars)

    def gatherResources(self, year, duration):
        gain = 0
        for star in self.inhabited_stars:
            gain += star.value
        self.resources += gain

    def findFrontLine(self, passed_node=''):
        node = passed_node
        if passed_node == '':
            node = self.homeworld
        if len(node.children) == 0:
            # print(node)
            return [node]
        else:
            frontline = []
            for child in node.children:
                res = self.findFrontLine(child)
                # frontline.append(*res)
                frontline +=  res
            return frontline

    def looseSystem(self, star):

        index = self.inhabited_stars.index(star)
        del self.inhabited_stars[index]
    


    

