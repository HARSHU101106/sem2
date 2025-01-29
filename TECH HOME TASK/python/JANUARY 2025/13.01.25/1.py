gas = list(map(int, input("Enter the gas available at each station (space-separated): ").split()))
cost = list(map(int, input("Enter the cost to travel to the next station (space-separated): ").split()))
total_tank = 0  
curr_tank = 0   
starting_station = 0  
if len(gas) != len(cost):
    print("Error: The gas and cost arrays must have the same length.")
else:
    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        curr_tank += gas[i] - cost[i]
        if curr_tank < 0:
            starting_station = i + 1
            curr_tank = 0
    result = starting_station if total_tank >= 0 else -1
    print(result)
