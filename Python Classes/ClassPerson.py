class Person:
 def __init__(self, name, birth_year, gender, father=None, mother=None):
    	self.name = name
    	self.birth_year = birth_year
    	self.gender = gender
    	self.father = father
    	self.mother = mother
    	self.children = []
    	if father and mother:
        	if father.birth_year - self.birth_year < 18 or mother.birth_year - self.birth_year < 18:
            	print("Parents must be at least 18 years older than the child")
        	else:
         	father.children.append(self)
         	mother.children.append(self)


	def get_brothers(self):
         return [
        	(child for child in self.father.children if child.gender == 'M' and child != self)
        	or
        	(child for child in self.mother.children if child.gender == 'M' and child != self)
    	]


	def get_sisters(self):
         return [
        	(child for child in self.father.children if child.gender == 'F' and child != self)
        	or
        	(child for child in self.mother.children if child.gender == 'F' and child != self)
    	]


	def get_children(self, gender=None):
            if gender:
        	return [child for child in self.children if child.gender == gender]
        else:
        return self.children


	def is_direct_successor(self, other):
            return other in self.children or self in other.children




person1 = Person("John", 1980, "M")
person2 = Person("Alice", 1990, "F")
person3 = Person("Bob", 1989, "M")
person4 = Person("Patricia", 1979, "F")


person1.father = person3
person1.mother = person4


person3.children.append(person1)
person4.children.append(person1)


brothers = person1.get_brothers()
sisters = person1.get_sisters()


children = person3.get_children()
sons = person3.get_children("M")
daughters = person3.get_children("F")


successor = person1.is_direct_successor(person3)
