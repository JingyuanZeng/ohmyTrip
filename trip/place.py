class Place(object):
	def __init__(self, country, local):
		pass

class Region(Place):
	points = [] # Point list

class Point(Place):
	def __init__(self, weight_user):
		self.weight_user = weight_user

class Bar(Point):
	def __init__(self, weight_user):
		super(Bar, self).__init__(weight_user)

	def __str__(self):
		return "bar"

class Museum(Point):
	def __init__(self, weight_user):
		super(Museum, self).__init__(weight_user)

	def __str__(self):
		return "musem"

class Park(Point):
	def __init__(self, weight_user):
		super(Park, self).__init__(weight_user)

	def __str__(self):
		return "park"

class Beach(Point):
	def __init__(self, weight_user):
		super(Beach, self).__init__(weight_user)

	def __str__(self):
		return "beach"

class SkyStation(Point):
	def __init__(self, weight_user):
		super(SkyStation, self).__init__(weight_user)

	def __str__(self):
		return "sky"

class Restaurant(Point):
	def __init__(self, weight_user):
		super(Restaurant, self).__init__(weight_user)

	def __str__(self):
		return "restaurant"

class NightClub(Point):
	def __init__(self, weight_user):
		super(NightClub, self).__init__(weight_user)

	def __str__(self):
	return "boite de nuit"

class Zoo(Point):
	def __init__(self, weight_user):
		super(Zoo, self).__init__(weight_user)

	def __str__(self):
		return "zoo"

class Bridge(Point):
	def __init__(self, weight_user):
		super(Bridge, self).__init__(weight_user)

	def __str__(self):
		return "pont"

class Board(Point):
	def __init__(self, weight_user):
		super(Board, self).__init__(weight_user)

	def __str__(self):
		return "port"