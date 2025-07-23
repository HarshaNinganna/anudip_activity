class Events:
    def __init__(self, type, cost, venue):
        self.type = type
        self.cost = cost
        self.venue = venue
    def display_details(self):
        print(f"Event Type: {self.type}")
        print(f"Cost: {self.cost}")
        print(f"Venue: {self.venue}")        
Event1 = Events("Birthday", 15000, "VintageInn")
Event2 = Events("Anniversary", 25000, "VintageInn")
Event1.display_details()
print("_______________________")
Event2.display_details()
