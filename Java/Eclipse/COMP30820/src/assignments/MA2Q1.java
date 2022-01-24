package assignments;

import java.util.Scanner;

public class MA2Q1 {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Amount:");
		double amount = scanner.nextDouble();
		
		if (amount < 0) {
			System.err.println("Amount should be positive!");
			System.exit(1);
		}
		
		System.out.println("Annual Interest Rate:");
		double annualRate = scanner.nextDouble();
		
		System.out.println("Amount invested: " + amount);
		System.out.println("Annual interest rate: " + annualRate);
		
		double monthlyRate = (annualRate) / 1200;
		
		System.out.println("Years\tValue");
		for (int i = 0; i < 30; i++) {
			
			int year = i + 1;
			double value = futureValue(amount, monthlyRate, year);
			
			System.out.println(String.format("%s\t%.2f", year, value));
		
		}
		
		scanner.close();
		
	}
	
	public static double futureValue(double amount, double monthlyRate, int years) {
		
		int months = years * 12;
		
		return amount * Math.pow(1 + monthlyRate, months);
	
	}

}
