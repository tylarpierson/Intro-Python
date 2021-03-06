from item import Item, Treasure

# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, playerName, startRoom):
        self.room = startRoom
        self.name = playerName
        self.items = []
        self.score = 0
    
    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, name):
        item = self.findItem(name)
        self.items.remove(item)

    def findItem(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def pickupItem(self, name):
        item = self.room.findItem(name)
        if item is None:
            print('Item not found')
        else:
            if isinstance(item, Treasure):
                if item.picked_up == False:
                    item.picked_up = True
                    self.addToScore(item.value)

            self.addItem(item)
            self.room.removeItem(item.name)

            
    def dropItem(self, name):
        item = self.findItem(name)
        if item is None:
            print('Item not found\n')
        else:
            self.removeItem(item.name)
            self.room.addItem(item)

    def printInventory(self):
        if len(self.items) > 0:
            print('Inventory:\n')    
            for item in self.items:
                print('name:', item.name, 'description: ', item.description)
        else:
            print('You have no items in inventory')

    def addToScore(self, amount):
        self.score += amount

    def substractFromScore(self, amount):
        if self.score > 0:
            self.score -= amount

    def printScore(self):
        print('Your score is: ', self.score)