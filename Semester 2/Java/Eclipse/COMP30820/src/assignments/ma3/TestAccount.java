package assignments.ma3;

import java.util.Date;

public class TestAccount {

	public static void main(String[] args) {
		
		Account account = new Account(101, 20000);
		Account.setAnnualInterestRate(0.045);
		
		account.Withdraw(2500);
		account.Deposit(3000);
		
		double balance = account.getBalance();
		double monthlyBalance = account.getMonthlyInterestAmount();
		Date dateCreated = account.getDateCreated();
		
		System.out.println("Balance: " + balance);
		System.out.println("Monthly Balance: " + monthlyBalance);
		System.out.println("Date Created: " + dateCreated);
		
	}
	
}
