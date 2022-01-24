package practicals;

import java.util.Scanner;

public class P2Q5 {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Enter a letter:");
		String input = scanner.nextLine();
		
		if (input.length() == 0) {
			System.out.println("Invalid input");
			System.exit(0);
		}
		
		char character = input.charAt(0);
		
		if (!Character.isAlphabetic(character)) {
			System.out.println(
					"Alphabetic, please!");
			System.exit(0);
		}
		
		String kind;
		switch (Character.toLowerCase(character)) {
		
		case 'a':
		case 'e':
		case 'i':
		case 'o':
		case 'u':
			kind = "vowel";
			break;
		default:
			kind = "consonant";
			break;
		
		}
		
		System.out.println("That letter is a "
				+ kind + ".");
		
		scanner.close();

	}

}
