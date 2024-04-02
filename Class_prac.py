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

no_of_cats = int(input("Enter the number of cats you want to see: "))

cats=[]
for each in range(no_of_cats):
    cat_ = f"Cat_{each + 1}"
    cats.append(cat_)
    cat_ = CAT(*input("Enter the name, color and action of your cat in order with a space in between: ").split())
    cat_.view()
for every in cats:
    print(f'Your objects: {every}')
