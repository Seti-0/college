package project.players;

import java.io.PrintWriter;
import java.util.Scanner;

import project.Player;

/**
 * A {@link Player} with a custom title before their name.
 */
public class Special extends Player {

	private String title;
	
	public Special() {
		
		title = "";
		
	}
	
	public Special(String name, String title) {
		
		super(name);
		this.title = title;

	}
	
	public String getTitle() {
		
		return title;
		
	}
	
	public void setTitle(String title) {
		
		this.title = title;
		
	}
	
	@Override
	public String toString() {

		return "(" + title + ") " + super.toString();
		
	}
	
	@Override
	public void onSave(PrintWriter writer) {

		super.onSave(writer);
		
		writer.println(title);
		
	}
	
	@Override
	public void onLoad(Scanner scanner) {

		super.onLoad(scanner);
		
		title = scanner.nextLine();
		
	}

}
