package practicals;

import java.util.Scanner;

public class P2Q3 {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
				
		System.out.println("Enter two numbers:");
		int x = scanner.nextInt();
		int y = scanner.nextInt();
		
		Rect rect = new Rect(-5, -2.5, 10, 5);
		
		if (rect.contains(x, y))
			System.out.println("Indeed");
		
		else System.out.println("Nope!");
		
		scanner.close();
		
	}
	
	private static class Rect {
		
		public double x, y, w, h;
		
		public Rect(double x, double y,
					double w, double h) {
			
			this.x = x;
			this.y = y;
			this.w = w;
			this.h = h;
		
		}
		
		public boolean contains(double x, 
								double y) {
			
			if (x < this.x || x > this.x + w)
				return false;
			
			if (y < this.y || y > this.y + h)
				return false;
			
			return true;
			
		}
	}

}
