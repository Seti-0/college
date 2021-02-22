package assignments;

import java.util.Scanner;

public class MA2Q2 {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Enter password:");
		String password = scanner.nextLine();

		if (isLongEnough(password) && isAlphaNumeric(password) && hasThreeDigits(password)) {
			
			System.out.println("This is a valid password!");
		
		}
		else {
		
			System.out.println("This is not a valid password.");
			
		}
		
		scanner.close();
		
	}

	public static boolean isLongEnough(String password) {
		
		// The password must be at least 10 characters long.
		// The original assignment said 2, but apparently this was a typo.
		
		return password.length() > 9;
	
	}
	
	public static boolean isAlphaNumeric(String password) {
		
		// Ignore letter case
		password = password.toLowerCase();
		
		// Alphanumeric characters are allowed
		final String allowed = "abcdefghijklmnopqrstuvwxyz0123456789";
		
		for (int i = 0; i < password.length(); i++) {
			
			// -1 means the character was not found among 
			// the allowed characters
			if (allowed.indexOf(password.charAt(i)) == -1)
				return false;
		}
		
		return true;
		
	}
	
	public static boolean hasThreeDigits(String password) {
		
		final String digits = "0123456789";
		
		int count = 0;
		
		for (int i = 0; i < password.length(); i++) {
			
			// -1 means that the character is not found in the "digits" String
			if (digits.indexOf(password.charAt(i)) != -1) {
				
				count++;
				if (count > 2)
					return true;
				
			}
			
		}
		
		return false;
		
	}
	
}
