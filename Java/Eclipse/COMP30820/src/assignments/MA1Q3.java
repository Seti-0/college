package assignments;

import java.util.Random;
import java.util.Scanner;

public class MA1Q3 {

	public static void main(String[] args) {
		
		Random random = new Random();
		
		// The answer should be between 0 and 100 inclusive!
		// Since the function below is exclusive, that means 
		// the upper bound is 101.
		int answer = random.nextInt(101);

		System.out.println("Guess a number between 0 and 100:");
		
		Scanner scanner = new Scanner(System.in);
		
		while (true) {
			
			int guess = scanner.nextInt();
			
			if (guess > answer)
			{
				System.out.println("Too high.");	
			}
			else if (guess < answer)
			{
				System.out.println("Too low.");
			}
			else
			{
				break;
			}
			
		}
		
		scanner.close();
		
		System.out.println("Correct!");
		
	}

}
