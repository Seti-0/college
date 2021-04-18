package assignments.ma3;

public class TestRegularPolygon {

	public static void main(String[] args) {
		
		RegularPolygon[] polys = new RegularPolygon[] {
				
				new RegularPolygon(3, 10),
				new RegularPolygon(6, 7.5),
				new RegularPolygon(8, 3.5),
				new RegularPolygon(12, 4)
				
		};
		
		double minPerimeter = Double.MAX_VALUE;
		RegularPolygon minPerimeterPoly = null;
		
		double maxArea = 0;
		RegularPolygon maxAreaPoly = null;
		
		for (RegularPolygon poly : polys) {
			
			System.out.println(poly);
			System.out.println("Perimeter: " + poly.getPerimeter());
			System.out.println("Area: " + poly.getArea());
			
			System.out.println();
			
			if (poly.getPerimeter() < minPerimeter)
			{
				minPerimeter = poly.getPerimeter();
				minPerimeterPoly = poly;
			}
			
			if (poly.getArea() > maxArea) {
				maxArea = poly.getArea();
				maxAreaPoly = poly;
			}
			
		}
		
		System.out.println("Min perimeter: " + minPerimeterPoly);
		System.out.println("Max area: " + maxAreaPoly);
		
	}
	
}
