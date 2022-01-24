package practicals;

import java.util.Scanner;

public class P3Q3 {

	public static void main(String[] args) {
		
		System.out.println("Enter your credit card number:");
		
		Scanner scanner = new Scanner(System.in);
		String number = scanner.nextLine();
		scanner.close();
		
		if (isValid(number)) 
			System.out.println("This is valid!");
		
		else 
			System.out.println("This is invalid.");
	}
	
	private static boolean isValid(String number) {
		
		// Ignore spacing
		number = number.replace(" ", "");
		
		final String digits = "0123456789";
		
		// Is it made up of digits?
		for (int i = 0; i < number.length(); i++) {
			if (digits.indexOf(number.charAt(i)) == -1)
			{
				System.out.println("Non-digit character detected!");
				return false;	
			}
		}
		
		// The number must have between 13 and 16 digits
		if (number.length() > 16 || number.length() < 13)
		{
			System.out.println("Too large or too small");
			return false;	
		}

		// The Luhn check.
		
		// Add odd digits together
		int countOdd = 0;
		
		// Double and normalize even digits, and add them together.
		// (See "evenValue" for the definition of normalize here...)
		int countEven = 0;
		
		for (int i = 0; i < number.length(); i++) {
			
			char character = number.charAt(number.length() - 1 - i);
			
			// The even/odd-ness is considered based on their 
			// 1-based position, not their 0-based position!
			int pos = i + 1;
			
			if (pos % 2 == 0) {
				countEven += evenValue(character);
			}
			else {
				countOdd += oddValue(character);
			}
			
		}
		
		System.out.println(countOdd);
		System.out.println(countEven);
		
		if ((countOdd + countEven) % 10 == 0)
			return true;
		
		else
		{
			System.out.println("Luhn check failed");
			return false;
		}
		
	}
	
	private static int oddValue(char input) {
		
		final String digits = "0123456789";
		return digits.indexOf(input);
		
	}
	
	private static int evenValue(char input) {
		
		final String digits = "0123456789";
		
		int number = digits.indexOf(input);
		number = number * 2;
		
		if (number > 9)
			number = (number - 10 ) + 1;
		
		return number;
		
	}
}
