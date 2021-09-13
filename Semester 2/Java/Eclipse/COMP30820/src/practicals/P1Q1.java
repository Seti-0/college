package practicals;

import java.util.InputMismatchException;
import java.util.Scanner;

public class P1Q1 {
	
	public static void main(String[] args) {
		
		try (Scanner scanner = new Scanner(System.in)) {
			
			System.out.println("Enter radius: ");
			double radius = scanner.nextDouble();
			
			System.out.println("Enter length: ");
			double length = scanner.nextDouble();

			double area = radius * radius * Math.PI * length;
			
			System.out.println(area);
			
		}
		catch (InputMismatchException e) {
			System.out.println("Failed to parse number");
		}
		
	}
	
}
