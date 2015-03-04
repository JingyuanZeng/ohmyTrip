from YelpHelper import query_api as yelp_request
try:
    xrange
except:
    xrange = range

class Sejour(object):
    """

    """
    id_sejour = -1

    def __init__(self, date_begin, date_end, places, user):
        Sejour.id_sejour += 1
        self.date_begin = date_begin
        self.date_end = date_end
        self.places = places
        self.user = user
        self.id = Sejour.id_sejour
        self.getPointsActivity()
        print "create sejour (%d)" % self.id

    def getPointsActivity(self):
        self.activite = {}
        for p in self.places:
            self.activite[p] = []
            for i in self.user.getProfil():
                interet = self.user.getInteret(i)
                if(interet == 0):
                    continue
                yelp_request(str(i()), str(p))
                #self.activite[p] = []

    def getId(self):
        return self.id

    def chooses_items_per_day(items, time_limit):
        table = [[0]*(time_limit + 1) for j in xrange(len(items) + 1)]
        for j in xrange(1, len(items) + 1):
            item, time, val = items[j-1]
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
                item, time, val = items[j-1]
                result.append(items[j-1])
                w -= time
     
        return result