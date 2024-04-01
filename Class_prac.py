class CAT:
    def __init__(self, name, color, action): #parameterized constructor
        self.name = name #instance variable
        self.color = color #instance variable
        self.action = action #instance variable

    def view(self):
        print(self.color, self.name, 'cat is', self.action)
    
    def compare(self, cat):
        if self.action == cat.action: #pass by reference
            print('Both cats are', self.action)
        else: 
            print('Their actions are different')

    def set_action(self, new_action):
        self.action = new_action

    def get_action(self):
        print('New action has been updated')

#============================================================================================
        
c1 = CAT("Jacky", "Brown", "dancing")
c2 = CAT("Tom", "Navy blue", "jumping")

c1.view()
c2.view()

c1.compare(c2)

c2.set_action("dancing")

c2.compare(c1)
