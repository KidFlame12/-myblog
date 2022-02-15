class score():
    def __init__(self):
        self.score = 1
        
    def show_score(self):
        print(self.score)
        
    def update_score(self):
        self.score = self.score +1
        print(self.score)
        
player = score()
player.update_score()
player.show_score()