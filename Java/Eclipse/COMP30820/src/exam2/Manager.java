package exam2;

public class Manager extends Employee{
	private double bonus;
	private String office;
	
	public Manager() {
		bonus = 0;
		office = "None";
	}
	
	public Manager(String name, int age, String email, 
			double salary, double bonus, String office) {
		super(name, age, email, salary);
		this.bonus = bonus;
		this.office = office;
	}
	
	public double getBonus() {
		return bonus;
	}
	
	public void setBonus(double bonus) {
		if (bonus < 0)
			throw new IllegalArgumentException("Bonus cannot be negative!");
		
		this.bonus = bonus;
	}
	
	public String getOffice() {
		return office;
	}
	
	public void setOffice(String office) {
		this.office = office;
	}
	
	@Override
	public double getSalary() {
		return super.getSalary() + bonus;
	}
	
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return super.toString() + bonus + "\n" + office + "\n";
	}
}
