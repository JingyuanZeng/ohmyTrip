# -*- coding: UTF-8 -*-

from YelpHelper import query_api as yelp_request
from place import *
try:
    xrange
except:
    xrange = range

class Trip(object):
    """

    """
    id_sejour = -1

    def __init__(self, date_begin, date_end, places, user):
        Trip.id_sejour += 1
        self.date_begin = date_begin
        self.date_end = date_end
        self.periode = date_end - date_begin
        self.places = places
        self.user = user
        self.id = Trip.id_sejour
        self.getPointsActivity()
        print "create trip (%d)" % self.id

    def placesToString(self, liste_place):
        s = ""
        for i in liste_place:
            s += " " + unicode(i)
        print unicode(s)

    def getTripNbDays(self, daily_trip):
        return sum([len(v) for v in daily_trip])

    def getPointsActivity(self):
        #TODO: delete return
        self.activite = {}
            
        for p in self.places:
            self.activite[p] = []
            for i in self.user.getProfil():
                interet = self.user.getInteret(i)
                y = yelp_request(i, p)
                self.activite[p] += y

        daily_trip = []
        villes = []

        for place in self.activite:
            print "(%s)-------------" % (place)
            liste_place = self.activite[place]
            jours = []
            jour = 0
            while(len(liste_place) > 0):
                l = self.chooses_items_per_day(liste_place, 720)
                liste_place = [i for i in liste_place if i not in l]
                print "Jour %d/%s : %d/%d ---------" % (jour+1, place, len(l), len(liste_place))
                self.placesToString(l)
                jours += [l]
                jour += 1
            villes += jours

        print "-----------------"
        daily_trip += [villes]
        pprint.pprint(daily_trip)
        nb_days =  self.getTripNbDays(daily_trip)
        while(nb_days > self.periode.days):
            print "%d  > %d"  % (self.periode.days, nb_days)
            nb_days -= 1
            
    def getId(self):
        return self.id

    def getWeightValuesPlace(self, item):
        time = item.time()
        note_user = int(self.user.profil[item.__class__])
        val = item.value(note_user)

        return [item, time, val]

    def chooses_items_per_day(self, items, time_limit):
        table = [[0]*(time_limit + 1) for j in xrange(len(items) + 1)]
        for j in xrange(1, len(items) + 1):
            item, time, val = self.getWeightValuesPlace(items[j-1])
            for w in xrange(1, time_limit + 1):
                if time > w:
                    table[j][w] = table[j-1][w]
                else:
                    table[j][w] = max(table[j-1][w],
                                      table[j-1][w-time] + val)
        result = []
        w = time_limit
        for j in range(len(items), 0, -1):
            was_added = table[j][w] != table[j-1][w]
     
            if was_added:
                #item, time, val = items[j-1]
                item, time, val = self.getWeightValuesPlace(items[j-1])
                result.append(items[j-1])
                w -= time
     
        return result