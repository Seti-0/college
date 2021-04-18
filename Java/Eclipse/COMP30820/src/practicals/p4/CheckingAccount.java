package practicals.p4;

public class CheckingAccount extends Account {

	private double overdraftLimit = 1000;
	
	public CheckingAccount() {
		
		super();
		
	}
	
	public CheckingAccount(int id, double balance) {
		
		super(id, balance);
		
	}
	
	public double getOverdraft() {
		
		return overdraftLimit;
	
	}
	
	public void setOverdraftLimit(double overdraftLimit) {
		
		this.overdraftLimit = overdraftLimit;
		
	}
	
	@Override
	public String toString() {
		
		String template = "%s (Overdraft: %.2f)";
		return template.formatted(super.toString(), overdraftLimit);
		
	}
	
	@Override
	public void withdraw(double amount) {
		
		if (amount > getBalance() + overdraftLimit) {
			
			String template = "Your current balance is $%.2f.\n"
					+ "Your overdraft limit is %.2f.\n"
					+ "You have attempted to withdraw $%.2f.\n"
					+ "This transaction cannot be completed.\n"
					+ "Your balance is unchanged.";
			
			String message = template.formatted(getBalance(), overdraftLimit, amount);
			System.out.println(message);
			return;
			
		}
		
		super.withdraw(amount);
	}
	
	@Override
	public double getMonthlyInterest() {
		
		if (getBalance() < 0)
			return 0;
		
		return super.getMonthlyInterest();
		
	}
	
}
