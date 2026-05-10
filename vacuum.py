class VacuumCleaner:
    def __init__(self):
        # Environment: living room and kitchen
        # Status: 1 represents 'Dirty', 0 represents 'Clean'
        self.locations = {'Living Room': 1, 'Kitchen': 1}
        self.current_pos = 'Living Room'

    def sense(self):
        """Perceives the cleanliness of the current room."""
        return self.locations[self.current_pos]

    def act(self, action):
        """Executes an action: either cleaning or moving to the next room."""
        if action == 'SUCK':
            print(f"{self.current_pos} is Dirty. Sucking up the dirt.")
            self.locations[self.current_pos] = 0
            print(f"The {self.current_pos} is now clean!")
            
        elif action == 'MOVE':
            # Identify the other room to move to
            other_room = 'Kitchen' if self.current_pos == 'Living Room' else 'Living Room'
            print(f"Nothing to do here. Moving to the {other_room}.")
            self.current_pos = other_room

    def run(self, cycles=4):
        """
        The main control loop for the agent.
        Each cycle involves sensing the environment and taking an action.
        """
        print(f"Starting cleaning sequence. Initial position: {self.current_pos}")
        
        for i in range(cycles):
            print(f"\n--- Cycle {i+1} ---")
            is_dirty = self.sense()
            
            if is_dirty:
                self.act('SUCK')
            else:
                self.act('MOVE')
        
        print("\nCleaning sequence complete.")

# Instantiate the agent and run the simulation
agent = VacuumCleaner()
agent.run()