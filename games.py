import cards
def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while True:
        try:
            response = int(input(question))
            if response  in range(low, high):
                return response
            else:
                print("thats out of range")
        except:
            print("thats not a number")
            
def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

class Player(object):

    """ A player for a game. """
    def __init__(self, name,score):
        self.name = name
        self.score = score
    def __str__(self):
        rep = self.name
        rep = rep +" " +str(self.score)
        return rep

if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")




    
