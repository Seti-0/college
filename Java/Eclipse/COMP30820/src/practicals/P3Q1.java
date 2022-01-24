package practicals;

public class P3Q1 {

	public static void main(String[] args) {
		
		System.out.println("First 10 primes:");
		
		int number = 0;
		int count = 0;
		
		while (count < 10) {
			
			if (isPrime(number)) {
				System.out.println(number);
				count++;
			}
			
			number++;
		}
	}
	
	public static boolean isPrime(int number) {
		
		if (number < 2)
			return false;
		
		for (int i = 2; i <= number/2; i++) {
			
			if (number % i == 0)
				return false;
			
		}
		
		return true;
	}
}
