# https://www.codecademy.com/courses/learn-python-3/projects/basta-fazoolin
# Q19 Q20
class Business:
  businesses_count = 0
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
    Business.businesses_count += 1
    self.business_id = Business.businesses_count
  
# Q12 Q13
class Franchise:
  franchises_count = 0
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
    Franchise.franchises_count += 1
    self.franchise_id = Franchise.franchises_count
  
  def __repr__(self):
    return "We are at " + self.address
  
  # Q16
  def available_menus(self, time):
    self.time = time
    self.available = []
    for menu in self.menus:
      if self.time >= menu.start_time and self.time <= menu.end_time:
        self.available.append(menu)
    # print(self.available)
    return self.available

# Q1 Q2
class Menu:  
  menus_count = 0
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    Menu.menus_count += 1
    self.menu_id = Menu.menus_count
  
  # Q7
  def __repr__(self):
    self.representative_string = "{menu} available from {start}0 to {end}0".format(menu=self.name, start=self.start_time, end=self.end_time)
    return self.representative_string

  # Q9
  def calculate_bill(self, purchased_items):
    self.price_to_pay = 0
    for item in purchased_items:
      if self.items.get(item) != None:
        self.price_to_pay += self.items.get(item)
    # print(self.price_to_pay)
    return self.price_to_pay

# Q3
brunch = Menu('Brunch', {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 11.00, 16.00)

# Q4
early_bird = Menu('Early-bird', {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 15.00, 18.00)

# Q5
dinner = Menu('Dinner', {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17.00, 23.00)

# Q6
kids = Menu('The kids menu', {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11.00, 21.00)

# Q8
# print(brunch)
# print(early_bird)
# print(dinner)
# print(kids)

# Q10
brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
brunch.calculate_bill(['mimosa', 'orange juice'])

# Q11
early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])

# Q14
menus = [brunch, early_bird, dinner, kids]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
# print(flagship_store.menus)

# Q15 another part of the question __repr__
# print(flagship_store)
# print(new_installment)

# Q17
flagship_store.available_menus(12.00)
# print
# Q18
# new_installment.available_menus(17.00)


# Q21
franchise = [flagship_store, new_installment]
basta = Business("Basta Fazoolin' with my Heart", franchise)

# Q22
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu('Take a\' Arepa', arepas_items, 10.00, 20.00)

# Q23
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# arepas_place.available_menus(12.00)
# new_installment.available_menus(17.00)

# Q24
arepa = Business("Take a' Arepa", [arepas_place])


# Quickly testing that each class ID is incrementing
print("----------------------------------------------------------------------------")
print("Count of businesses:\t", Business.businesses_count)
print("Example business ID for Arepa Store:\t", arepa.business_id)
print("Count Franchises:\t", Franchise.franchises_count)
print("Example franchise ID for the Flagship Store\t", flagship_store.franchise_id)
print("Count of Menues:\t", Menu.menus_count)
print("Example Menu ID for The Kids Menu\t", kids.menu_id)
print("----------------------------------------------------------------------------")
print("\n")


# Q25 making sure all business exist!!
print("The Arepa Business:\t\t" + str(arepa.franchises[0]) + "\nwith the following menu(s)\t" + str(arepa.franchises[0].menus[0]))
print("\n")
print("Hi The Basta Business has 2 resturants located at:\n" + str(basta.franchises[0]) + "\n" + str(basta.franchises[1]) + "\n\nlist of menus are at times:\n" + str(basta.franchises[0].menus[0]) + "\n" + str(basta.franchises[0].menus[1]) + "\n" + str(basta.franchises[0].menus[2]) + "\n" + str(basta.franchises[0].menus[3]))