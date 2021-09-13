package exam2;

public class Employee extends Person {
	private double salary;

	public Employee() {
		salary = 0;
	}
	
	public Employee(String name, int age, String email, double salary) {
		super(name, age, email);
		this.salary = salary;
	}
	
	public double getSalary() {
		return salary;
	}

	public void setSalary(double salary) {
		if (salary < 0)
			throw new IllegalArgumentException("Salary cannot be negative!");
		
		this.salary = salary;
	}
	
	@Override
	public String toString() {
		return super.toString() + salary + "\n";
	}
}
