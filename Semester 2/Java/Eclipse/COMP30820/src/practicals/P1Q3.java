package practicals;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class P1Q3 {
	
	public static void main(String[] args) {
		
		Point a = null, b = null;
		
		try (Scanner scanner = new Scanner(System.in)) {
			
			a = readPair("Enter a point: ", scanner);
			b = readPair("Enter another point: ", scanner);
			
		}
		
		if (a == null || b == null)
			System.out.println("Failed to read input");
		
		else {
			
			double distance = Math.sqrt(a.X * b.X + a.Y * b.Y);
			
			System.out.println("The distance is: " + distance);
			
		}
		
	}
	
	private static class Point {
		
		public double X, Y;
		
		public Point(double x, double y) {
			X = x;
			Y = y;
		}
		
	}
	
	private static Point readPair(String promt, Scanner scanner) {
		
		// Pattern for a pair of items, eg. (4, 5)
		Pattern pattern = Pattern.compile("\\(([^,]*)\\,([^\\)]+)\\)");
		
		System.out.println(promt);
		String input = scanner.nextLine();
		
		Matcher matcher = pattern.matcher(input);
		boolean success = matcher.find();
		
		if (!success)
			return null;
		
		double x = Double.parseDouble(matcher.group(1));
		double y = Double.parseDouble(matcher.group(1));
		
		return new Point(x, y);
		
	}
	
}
