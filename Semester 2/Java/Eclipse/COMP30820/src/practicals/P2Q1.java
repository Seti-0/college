package practicals;

import java.util.Scanner;

public class P2Q1 {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Enter three numbers:");
		double a = scanner.nextDouble();
		double b = scanner.nextDouble();
		double c = scanner.nextDouble();
		
		boolean valid = true;
		
		if (a + b <= c)
			valid = false;
		
		if (b + c <= a)
			valid = false;
		
		if (a + c <= b)
			valid = false;
		
		if (!valid)
			System.out.println("These numbers"
			+ " do not make up the"
			+ " sides of a triangle.");
		
		
		else {
			
			double perimeter = a + b + c;
			
			System.out.println("The perimeter"
				+ " of the triangle with these"
				+ " side lengths is " + perimeter);
		}
		
		scanner.close();
		
	}

}
