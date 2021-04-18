package exams;

import java.util.Random;
import java.util.Scanner;

public class E1Q2 {

	public static void main(String[] args) {
		
		// Take in some text from the user
		
		System.out.println("Enter a string:");
		
		Scanner scanner = new Scanner(System.in);
		String input = scanner.nextLine();
		scanner.close();
		
		// Print a random character from that text.
		
		System.out.println(getRandomChar(input));
		
		// Note that the character could be empty whitespace! Like a space or a tab.
		// In this case, nothing is printed.
		
	}
	
	private static char getRandomChar(String input) {
		
		Random random = new Random();
		
		int index = random.nextInt(input.length());
		char result = input.charAt(index);
		
		return result;
		
	}

}
