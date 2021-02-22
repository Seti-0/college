package assignments;

import java.util.Scanner;

public class MA3Q3 {

	public static void main(String[] args) {
		
		System.out.println("Enter results series:");
		
		Scanner scanner = new Scanner(System.in);
		String series = scanner.nextLine();
		scanner.close();
		
		int wins = 0;
		int draws = 0;
		int losses = 0;
		
		for (int i = 0; i < series.length(); i++) {
			
			char character = series.charAt(i);
			
			switch (character) {
			
			case 'W':
				wins += 1;
				break;
			
			case 'D':
				draws += 1;
				break;
				
			case 'L':
				losses += 1;
				break;
				
			default:
				System.out.println("Unexpected character at index " + i + ": '"+character + "'");
				System.exit(1);
				
			}
			
		}
		
		System.out.println("Wins: " + wins);
		System.out.println("Draws: " + draws);
		System.out.println("Losses: " + losses);
		
		int totalPoints = wins * 3 + draws;
		double averagePoints = totalPoints / (double) series.length();
		
		System.out.println("Total Points: " + totalPoints);
		System.out.println(String.format("Average Points: %.2f", averagePoints));
		
	}
	
}
