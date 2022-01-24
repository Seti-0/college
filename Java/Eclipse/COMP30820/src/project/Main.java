package project;

import java.io.PrintWriter;
import java.util.Scanner;

import project.players.*;
import project.scenes.*;

/**
 * Contains the entry point to the application. Also offers
 * static methods for getting the application input and output streams.
 * 
 * @see Menu
 * @see Players
 * @see Games
 */
public class Main {
	
	private static Scanner in;
	private static PrintWriter out;
	
	public static void main(String[] args) {
		
		in = new Scanner(System.in);
		out = new PrintWriter(System.out);
		
		out.println("Loading...");
		
		loadComponents();
		
		Players.load();
		
		Menu menu = new Menu();
		menu.showMain();
		
		out.println("Saving...");
		
		Players.save();
		
		out.println("Done.");
		out.flush();
		
	}
	
	/**
	 * Get the input stream of the application.
	 */
	public static Scanner getInput() {
		
		return in;
		
	}
	
	/**
	 * Get the output stream of the application.
	 */
	public static PrintWriter getOutput() {
		
		return out;
		
	}
	
	private static void loadComponents() {
		
		// I'd have loved to separate these out into two or three modular plugins,
		// loaded by inspecting a "Plugins" folder and using inspection, 
		// that seems to be quite awkward in java. I didn't want to make 
		// a setup that might be finicky to run on the computer of the one
		// doing the assessing!
		
		// So I'm just listing them all.
		
		Games.add("Rock, Paper, Scissors", new RockPaperScissors());
		Games.add("Nim", new Nim());
		Games.add("Pazaak", new Pazaak());
		
		Players.register("Normal", () -> new Player());
		Players.register("Honour", () -> new Honour());
		Players.register("Ghost", () -> new Ghost());
		
		// Register a hidden player type. These serve no particular purpose
		// except as a li'l easter egg.
		
		Players.register("Special", () -> new Special());
		Players.setHidden("Special", true);
		
		setTitle("Seti", "Dev");
		setTitle("Odhranos", "Lord");
		setTitle("DeeKay", "Dr");
		
		setTitle("Aang", "Avatar");
		setTitle("Korra", "Avatar");
		setTitle("Max", "Mad");
		setTitle("X", "Professor");
		
	}
	
	private static void setTitle(String name, String title) {
		
		Special player = (Special) Players.add(name, "Special");
		player.setTitle(title);
		
	}

}
