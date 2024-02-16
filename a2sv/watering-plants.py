class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        total_step_needed = 0 # Store the total steps used to watering plants
        left_water = capacity # Used to trace the water left in the can

        i = 0
        # iterate through the plants using while loop
        while i < len(plants):
            if plants[i] > left_water: # check if the plants need more water than in the can
                left_water = capacity # re-fill it from the river
                total_step_needed += (2*i + 1) # it takes 2 * i + 1 step to take water from river and water it
            else:
                total_step_needed += 1 # if the water in the can is enough to water only one step is need to water it
            
            left_water -= plants[i] 

            i += 1

        return total_step_needed # return the total step used

