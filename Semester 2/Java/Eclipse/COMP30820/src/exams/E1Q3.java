package exams;

import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class E1Q3 {

	public static void main(String[] args) {
		
		// Take in user input.
		
		System.out.println("Enter a number of times:");

		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		scanner.close();
		
		// Simulate dice rolls.
		// Also keep a running total, this will
		// be useful later.
		
		int[] sums = new int[n];
		int total = 0;
		
		Random r = new Random();
		
		for (int i = 0; i < n; i++) {
			sums[i] = rollDice(r) + rollDice(r);
			total += sums[i];
		}
		
		// Sort the sums and calculate the average.
		
		Arrays.sort(sums);
		double average = total / (double) n;
		
		// Display the results.
		
		System.out.println(Arrays.toString(sums));
		System.out.println("Average: %.2f".formatted(average));
	}
	
	private static int rollDice(Random random) {
		
		// random.nextInt(6) gives a number between 0 and 5, inclusive.
		// 1 needs to be added to it to get the number that would be on the dice.
		return 1 + random.nextInt(6);
	}
}
