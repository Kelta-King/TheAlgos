// CPP program to find sum of k-th group of 
// positive odd integers. 
#include <bits/stdc++.h> 
using namespace std; 

// Return the sum of k-th group of positive 
// odd integers. 
int kthgroupsum(int k) 
{ 
	// Finding first element of kth group. 
	int cur = (k * (k - 1)) + 1; 
	int sum = 0; 

	// Finding the sum. 
	while (k--) { 
		sum += cur; 
		cur += 2; 
	} 

	return sum; 
} 

// Driver code 
int main() 
{ 
	int k = 3; 
	cout << kthgroupsum(k) << endl; 
	return 0; 
} 
