import random
import string


class User:

	def __init__(self, name):
		self.name = name

	def buy(self, seat, card):
		pass


class Seat:

	database = "cinema.db"

	def __init__(self, seat_id):
		self.seat_id = seat_id

	def get_price(self):
		pass

	def is_free(self):
		pass

	def occupy(self):
		pass


class Card:

	database = "banking.db"

	def __init__(self, type, number, cvc, holder):
		self.type = type
		self.number = number
		self.cvc = cvc
		self.holder = holder

	def validate(self, price):
		pass


class Ticket:

	def __init(self, user, price, seat_number):
		self.user = user
		self.price = price
		self.seat_number = seat_number
		self.id = "".join([random.choice(string.ascii_letters) for i in range(8)])

	def to_pdf(self):
		pass
