# Implement a class to hold room information. This should have name and
# description attributes.
class room:
  def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return "You are currently " + self.name + '\n' + self.description]