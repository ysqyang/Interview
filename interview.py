def max_profit(prices, unit_weights, capacity):
	'''
	dynamic programming approach
	'''
	n_types = len(unit_weights)   # number of cargo types
	# max number of units the ship can carry for each cargo type
	n_units = [capacity//weight for weight in unit_weights] 

	# At each port, there are a total of n_types+1 possible states:
        # empty and fully loaded with each type of cargo 
	# cash: maximum profit at current port if ship is empty 
	# hold: maximum profit at current port if ship is fully loaded with the i-th type of cargo
	cash, hold = 0, [-prices[0][i]*n_units[i] for i in range(n_types)]

	for price in prices: # price is a list of cargo prices at the current port
		# profits gained by selling current cargo on ship
		tmp = [hold[i]+price[i]*n_units[i] for i in range(n_types)]
		cash_new = max(cash, max(tmp)) 
		
		hold_new = []
		for i in range(n_types):
			# profits gained by replacing current (j-th) cargo on ship with the i-th type of cargo    
			tmp1 = [hold[j]+n_units[j]*price[j]-n_units[i]*price[i] for j in range(n_types)]
			hold_new.append(max(cash-price[i]*n_units[i], max(tmp1)))

		# update cash and hold
		cash = cash_new 
		hold = hold_new

	# return cash in the end since the ship must eventually be empty to achieve max profit 
	return cash
