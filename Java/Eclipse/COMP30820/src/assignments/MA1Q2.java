package assignments;

import java.util.Scanner;

public class MA1Q2 {

	public static void main(String[] args) {
		
		// Collect user input
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Enter year number:");
		int year = scanner.nextInt();
		
		System.out.println("Enter month number:");
		int month = scanner.nextInt();
		
		if (month < 1 || month > 12) {
			System.out.println("Unexpected input! Expected month to be between 1 and 12.");
			System.exit(1);
		}
		
		scanner.close();
		
		// Now that the user input is collected, calculate and print the 
		// number of days in the month 
		
		// This variable must be initialized in general before printing, 
		// but it should always be overriden in the switch statement.
		int dayCount = -1;
		
		switch (month) {
		
		case 1:
		case 3:
		case 5:
		case 7:
		case 8:
		case 10:
		case 12:
			dayCount = 31;
			break;
			
		case 4:
		case 6:
		case 9:
		case 11:
			dayCount = 30;
			break;
			
		case 2:
			
			// Special case for February, it depends on the year.
			if (isLeapyear(year))
				dayCount = 29;
			else
				dayCount = 28;
		
		}
		
		System.out.println("There are " + dayCount + " days in month " + month + " of year " + year + ".");

	}
	
	private static boolean isLeapyear(int year) {
		
		// This implementation is based off an algorithm from wikipedia:
		// https://en.wikipedia.org/wiki/Leap_year#Algorithm
		
		if (year % 4 != 0)
			return false;
		
		else if (year % 100 != 0)
			return true;
		
		else if (year % 400 != 0)
			return false;
		
		return true;
		
	}

}
