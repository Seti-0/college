package practicals;

import java.util.Scanner;

public class P1Q6 {

	public static void main(String[] args) {
		
		System.out.println("Enter a number: ");
		
		Scanner scanner = new Scanner(System.in);
		int number = scanner.nextInt();
		
		int total = 0;
		
		int count = (int) Math.log10(number);
		for (int i = 0; i < count; i++) {
			
			total += number % 10;
			number /= 10;
			
		}
		
		total += number;
		
		System.out.println("Sum of digits: "+total);
		
		scanner.close();
		
	}
	
	
	
}
