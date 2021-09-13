package practicals;

import java.util.Scanner;

public class P2Q4 {

	public static void main(String[] args) {
		
		try (Scanner scanner = new Scanner(System.in)) {
			
			System.out.println("Enter number:");
			int number = scanner.nextInt();
			
			if (number < 0) {
				System.out.println("Number can't be negative!");
				System.exit(0);
			}
			
			String digits = "0123456789ABCDEF";
			
			if (number >= digits.length()) {
				System.out.println("Number to large.");
				System.exit(0);
			}
			
			char digit = digits.charAt(number);
			
			System.out.println("Hex digit: " + digit);
			
		}

	}

}
