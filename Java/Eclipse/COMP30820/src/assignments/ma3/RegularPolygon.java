package assignments.ma3;

public class RegularPolygon {

	private int n = 3;
	
	private double length = 1;
	
	public RegularPolygon() {
		
		// No need to set anything here, the defaults
		// are set above.
	
	}
	
	public RegularPolygon(int n, double length) {
		
		this.n = n;
		this.length = length;
		
	}
	
	public int getN() {
		
		return n;
	
	}

	public void setN(int n) {
	
		this.n = n;
	
	}

	public double getLength() {
	
		return length;
	
	}

	public void setLength(double length) {
	
		this.length = length;
	
	}

	public double getPerimeter() {
		
		return n * length;
		
	}
	
	public double getArea() {
		
		double a = n * length * length;
		double b = 4 * Math.tan(Math.PI / n);
		
		return  a / b;
		
	}
	
	@Override
	public String toString() {
		
		String template = "Regular Polygon: %d sides of length %.02f";
		return String.format(template, n, length);
		
	}
	
}
