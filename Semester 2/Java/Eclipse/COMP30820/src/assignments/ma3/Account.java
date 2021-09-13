package assignments.ma3;

import java.util.Date;

public class Account {
	
	private static double annualInterestRate = 0;
	
	public static double getAnnualInterestRate() {
		
		return annualInterestRate;
	
	}

	public static void setAnnualInterestRate(double rate) {
	
		annualInterestRate = rate;
	
	}
	
	private int id = 0;
	
	private double balance = 0;
	
	private Date dateCreated;
	
	public Account() {
		
		dateCreated = new Date();
	
	}
	
	public Account(int id, int balance) {
		
		this();
		
		this.id = id;
		this.balance = balance;
		
	}

	public int getId() {
		
		return id;
	
	}

	public void setId(int id) {
	
		this.id = id;
	
	}

	public double getBalance() {
	
		return balance;
	
	}

	public void setBalance(double balance) {
	
		this.balance = balance;
	
	}

	public Date getDateCreated() {
	
		return dateCreated;
	
	}
	
	public double getMonthlyInterestAmount() {
	
		return balance * (annualInterestRate / 12);
		
	}
	
	public void Withdraw(double amount) {
		
		balance -= amount;
		
	}
	
	public void Deposit(double amount) {
		
		balance += amount;
		
	}
	
	@Override
	public String toString() {
		
		return String.format("%d - %s: %d", id, dateCreated, balance);
		
	}
}
