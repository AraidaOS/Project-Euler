#include <iostream>
#include <cmath>

using namespace std;

bool is_prime(int n) {
	if (n < 2)
		return false;
	int root = sqrt(n);
	for (int i=2; i<=root; i++) {
		if (n%i==0)
			return false;
	}
	return true;
} // end of helper function


// problem 10 - SUmmation of all primes
// trying in cpp for speed
int main() {
	long long LIMIT = 2000000;
	long long sum = 0;
	cout << "Problem 10 - Summation of Primes" << endl;
	for (int i=2; i<= LIMIT; i++) {
		if (is_prime(i))
			sum += i;
	}
	cout << "Sum of Primes: " << endl;
	cout << sum << endl;

	return 0;
} // end of main
