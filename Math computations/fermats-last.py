# Python3 program to verify fermat's last 
# theorem for a given range and n. 

def testSomeNumbers(limit, n) : 

	if (n < 3): 
		return
	
	for a in range(1, limit + 1): 
		for b in range(a, limit + 1): 
		
			# Check if there exists a triplet 
			# such that a^n + b^n = c^n 
			pow_sum = pow(a, n) + pow(b, n) 
			c = pow(pow_sum, 1.0 / n) 
			c_pow = pow(int(c), n) 
			
			if (c_pow == pow_sum): 
				print("Count example found") 
				return
	print("No counter example within given range and data") 

# Driver code 
testSomeNumbers(10, 3) 

# This code is contributed by Smitha Dinesh Semwal. 
