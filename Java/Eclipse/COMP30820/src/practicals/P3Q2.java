package practicals;

import java.util.Scanner;

public class P3Q2 {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Enter some text and press enter:");
		String subject = scanner.nextLine();
		
		if (isPalindrome(subject)) {
			
			System.out.println("You entered a palindrome!");
			
		}
		else {
			
			System.out.println("That is in fact not a palindrome.");
			
		}
		
		scanner.close();
		
	}
	
	public static boolean isPalindrome(String subject) {
		
		for (int i = 0; i < subject.length() / 2; i++) {
			
			char left = subject.charAt(i);
			char right =  subject.charAt(subject.length() - 1 - i);
			
			if (left != right)
				return false;
			
		}
		
		return true;
		
	}

}
