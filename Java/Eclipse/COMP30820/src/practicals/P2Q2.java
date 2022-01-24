package practicals;

import java.util.Scanner;

public class P2Q2 {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);

		System.out.println("Enter radius:");
		double radius = scanner.nextDouble();
		
		if (radius <= 0) {
			
			System.out.println("The radius must be >= 0");
			System.exit(0);
			
		}
		
		double sideLength = 2 * radius * Math.sin(Math.PI/5);
		double area = 5 * Math.pow(sideLength, 2) / (4 * Math.tan(Math.PI/5));
		
		System.out.println("The area of the pentagon described by "
			+ " this radius is: " + area);
		
		scanner.close();
		
	}

}
