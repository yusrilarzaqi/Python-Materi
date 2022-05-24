class Hero:
	# var class
	jumlah=0

	def __init__(self,name,health,attackDamage):
		self.name=name
		self.health=health
		self.attackDamage=attackDamage
		Hero.jumlah+=1

		# variable instance private
		self.__private='Private'
		# variable private tidak bisa diakses ataupun dirubah

		# variabel protected
		self._protected="Protected"
		# bisa diru

# main program

shen=Hero('Shen',123,15)
print(shen.jumlah)
shen._protected='Hello'
print(shen._protected)
print(shen.__dict__)


