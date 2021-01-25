package practicals;

import java.text.DecimalFormat;
import java.util.Scanner;

public class P1Q2 {

	public static void main(String[] args) {
		
		final double 
		
			currentPopulation = 31203248,
			
			secondsPerYear = 365 * 24 * 60 * 60,
			secondsPerBirth = 7,
			secondsPerDeath = 13,
			secondsPerImmigrant = 45,
		
			birthsPerYear = secondsPerYear / secondsPerBirth,
			deathsPerYear = secondsPerYear / secondsPerDeath,
			immigrantsPerYear = secondsPerYear / secondsPerImmigrant,
			
			populationChangePerYear = birthsPerYear - deathsPerYear + immigrantsPerYear;
	
		try (Scanner scanner = new Scanner(System.in)) {
			
			System.out.print("Enter a number of years: ");
			double years = scanner.nextDouble();
			
			double futurePopulation = currentPopulation + years * populationChangePerYear;
			
			DecimalFormat formatter = new DecimalFormat("#,##0.00");
			System.out.println("The future population will be: "
					+ formatter.format(futurePopulation));
			
		}
		
	}
	
}
