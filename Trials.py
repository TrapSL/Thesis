def optimize_profit(lead_times, spot_rates, opportunity_costs, sailing_costs):
    T = len(lead_times)  # time horizon
    P = ['Arabian Gulf', 'China']  # positions
    R = len(spot_rates)
    
    # Initialize value function
    V = [[[0 for _ in range(R)] for _ in P] for _ in range(T)]
    
    # Initialize decision function
    D = [[[None for _ in range(R)] for _ in P] for _ in range(T)]
    
    # Iterate through time, position, and spot rate
    for t in reversed(range(T-1)):
        for p in P:
            for r in range(R):
                # Calculate profit for accepting a contract
                profit_accept = spot_rates[r] - sailing_costs[p]
                
                # Calculate profit for waiting
                profit_wait = opportunity_costs[p]
                
                # Calculate the value of future states
                value_future_accept = V[t+1][(p+1) % 2][r]
                value_future_wait = V[t+1][p][r]
                
                # Choose the optimal decision
                if profit_accept + value_future_accept > profit_wait + value_future_wait:
                    V[t][p][r] = profit_accept + value_future_accept
                    D[t][p][r] = 'accept'
                else:
                    V[t][p][r] = profit_wait + value_future_wait
                    D[t][p][r] = 'wait'
                    
    return V, D