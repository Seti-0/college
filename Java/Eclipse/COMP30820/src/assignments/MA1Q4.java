package assignments;

import java.util.Scanner;

public class MA1Q4 {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Enter two strings:");
		String a = scanner.nextLine();
		String b = scanner.nextLine();
		
		scanner.close();
		
		// Print the common prefix of inputs a and b.
		
		// To do this, iterate through each character until
		// the end of the shorter string is reached or the 
		// characters don't match, appending to the result
		// string along the way.
		
		String result = "";
		
		int index = 0;
		while (true) {
			
			if (index >= a.length() || index >= b.length())
				break;
			
			if (a.charAt(index) != b.charAt(index))
				break;
			
			result += a.charAt(index);
			index++;
			
		}
		
		if (result.isBlank())
			System.out.println("No common prefix.");
		else
			System.out.println("Common prefix: " + result);
		
	}
	
}
