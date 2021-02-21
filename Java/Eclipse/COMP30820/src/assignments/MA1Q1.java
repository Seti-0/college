package assignments;

import java.util.Scanner;

public class MA1Q1 {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		// Collect user input. 
		
		// The scanner will throw an exception if the
		// input is not a number here, that's fine for this assignment.
		
		System.out.println("Enter a number for speed:");
		double speed = scanner.nextDouble();
		
		System.out.println("Enter a number for acceleration:");
		double acceleration = scanner.nextDouble();
		
		// For the condition character, an error message should
		// be displayed if the input is unexpected.
		
		System.out.println("Enter 'w' for wet conditions, or 'd' for dry conditions:");
		
		scanner.nextLine();
		String condition = scanner.nextLine();
		
		// Case should not be considered.
		condition = condition.toLowerCase();
		
		if (!(condition.equals("w") || condition.equals("d")))
		{
			System.err.println("Unexpected input! Condition should be 'd' or 'w'.");
			System.exit(1);
		}
		
		scanner.close();
		
		// Now that the input has been collected, calculate the
		// runway length and print it.
		
		double length = speed * speed / (2 * acceleration);
		
		if (condition.equals("w"))
			length *= 1.15;
		
		System.out.println("The length of runway required is: " + length);
		
	}
	
}
