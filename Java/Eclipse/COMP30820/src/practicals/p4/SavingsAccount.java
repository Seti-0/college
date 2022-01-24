package practicals.p4;

public class SavingsAccount extends Account {

	public SavingsAccount() {
		
		super();
		
	}
	
	public SavingsAccount(int id, double balance) {
		
		super(id, balance);
		
	}
	
	@Override
	public void withdraw(double amount) {
		
		if (amount > getBalance()) {
			
			String template = "Your current balance is $%.2f.\n"
					+ "You have attempted to withdraw $%.2f.\n"
					+ "This transaction cannot be completed.\n"
					+ "Your balance is unchanged.";
			
			String message = template.formatted(getBalance(), amount);
			System.out.println(message);
			return;
			
		}
		
		super.withdraw(amount);

	}
	
}
