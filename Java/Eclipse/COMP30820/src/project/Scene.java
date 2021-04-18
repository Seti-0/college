package project;

import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Collection;
import java.util.Iterator;
import java.util.Scanner;
import java.util.function.Predicate;

import project.scenes.Menu;

/**
 * A "Scene" in the application. This could be a menu, or a game. 
 * 
 * @see Game
 * @see Menu
 */
public abstract class Scene {
	
	// Aside from being a way to logically regroup scenes in the application,
	// this is just a collection of utilities. There is a lot of code reused between 
	// the different games and menus. A utility class could have been used instead of inheritence
	// for that, though.
	
	// Strictly speaking, these variables should be ecapsulated, possibly. Though
	// they are final, which is something. I opted not to encapsulate them in this 
	// little project because they form a very neat shorthand throughout.
	protected final Scanner in;
	protected final PrintWriter out;
	
	public Scene() {
		
		this.in = Main.getInput();
		this.out = Main.getOutput();
		
	}
	
	/**
	 * Pause the application and wait for a user prompt to continue.
	 */
	protected void pause() {
		
		out.println("(Press Enter to continue)");
		out.flush();
		
		in.nextLine();
		
	}
	
	/**
	 * Slow the application briefly. Useful when a lot of text could
	 * speed by to fast to be read by the user.
	 */
	protected void shortPause() {
		
		pauseFor(0.5);
		
	}
	
	private void pauseFor(double seconds) {
		
		out.flush();
		
		try {
			
			Thread.sleep((long) (1000 * seconds));
		
		} catch (InterruptedException e) {
			
			e.printStackTrace();
		
		}
		
	}
	
	/**
	 * Takes a list of String options to display, and returns
	 * the option the user selects. A return option is also displayed,
	 * and if this is selected, null is returned.
	 */
	protected String showMenu(Collection<String> options) {
		
		String[] optionsArray = new String[options.size()];
		options.toArray(optionsArray);
		return showMenu(true, optionsArray);
		
	}
	
	/**
	 * Takes one or more String options to display, and returns
	 * the option the user selects. A return option is also displayed,
	 * and if this is selected, null is returned.
	 */
	protected String showMenu(String... options) {
		
		return showMenu(false, options);
		
	}
	
	/**
	 * Takes one or more String options to display, and returns
	 * the option the user selects. A return option can also displayed,
	 * and if this is displayed and selected, null is returned.
	 */
	protected String showMenu(boolean showReturn, String... options) {
		
		out.println();
		
		while (true) {
			
			for (String option : options) {
				
				char firstChar = option.charAt(0);
				String remainder = option.substring(1);
				
				out.println("[" + firstChar + "]" + remainder);
				
			}
			
			if (showReturn) {
				
				out.println();
				out.println("[B]ack");	
				
			}
			
			out.println();
			out.flush();
			String rawInput = in.nextLine().trim().toLowerCase();
			
			if (rawInput.isEmpty())
				continue;
			
			char result = rawInput.charAt(0);
			
			if (showReturn && result == 'b')
				return null;
			
			for (String option : options)
				if (option.toLowerCase().charAt(0) == result)
					return option;
			
			out.println("Unable to parse input.");
			out.println();
			
		}
		
	}
	
	/**
	 * Show one or more String options compactly, on a single line.
	 * @param options String options to display to the user.
	 * @return The option selected by the user.
	 */
	protected String showOptions(String... options) {
		
		while (true) {
			
			out.print("Choose ");
			
			for (int i = 0; i < options.length - 1; i++) {
				
				char firstChar = options[i].charAt(0);
				String remainder = options[i].substring(1);
				
				out.print("[" + firstChar + "]" + remainder);
				out.print(", ");
				
			}
			
			char firstChar = options[options.length - 1].charAt(0);
			String remainder = options[options.length - 1].substring(1);
			out.print("or [" + firstChar + "]" + remainder + ".");
			
			out.println();
			
			out.flush();
			String rawInput = in.nextLine().trim();
			
			if (rawInput.isEmpty())
				continue;
			
			char result = rawInput.toLowerCase().charAt(0);
			
			for (String option : options)
				if (option.toLowerCase().charAt(0) == result)
					return option;
			
			out.println("Unable to parse input.");
			out.println();
			
		}
		
	}
	
	/**
	 * Ask a yes/no question.
	 * @param question The message for the user
	 * @return True if the user answered yes, false if the user answered no.
	 */
	protected boolean askQuestion(String question) {
		
		while (true) {
			
			out.print(question);
			out.println(" [y]es/[n]o");
			
			out.flush();
			
			String rawInput = in.nextLine().trim();
			if (rawInput.isEmpty())
				continue;
			
			char input = rawInput.toLowerCase().charAt(0);
			switch (input) {
				case 'y': return true;
				case 'n': return false;
				default:
					out.println("Unable to parse input.");
					continue;
			}
			
		}
		
	}
	
	/**
	 * Display an array of integers in a friendly way.
	 */
	protected void printItems(int[] items) {
		
		// I can't belive java doesn't just have a sensible
		// toString for arrays and collections.
		
		printItems(Arrays.stream(items).iterator());
		
	}
	
	/**
	 * Display an iterator of items in a friendly way.
	 */
	protected void printItems(Iterator<?> items) {
		
		if (items.hasNext())
			out.print(items.next());
		
		items.forEachRemaining(item -> {
			
			out.print(", ");
			out.print(item.toString());
			
		});
		
		out.println();
		
	}
	
	// Lots of copy and pasting of documentation here... 
	// Is there a neater way?
	
	/**
	 * Request that the user choose a number.
	 * @param message The message displayed before " from X to Y".
	 * @param start Lower bound (inclusive)
	 * @param end Upper bound (inclusive)
	 * @return The number chosen.
	 */
	protected int chooseNumber(String message, int start, int end) {
		
		return chooseNumber(message, start, end, null, null, false);
		
	}
	
	/**
	 * Request that the user choose a number.
	 * @param message The message displayed before " from X to Y".
	 * @param start Lower bound (inclusive)
	 * @param end Upper bound (inclusive)
	 * @param allowSkip If true, allow the user to skip this choice.
	 * @return The number chosen, or 0 if the user skipped the choice.
	 */
	protected int chooseNumber(String message, int start, int end, boolean allowSkip) {
		
		return chooseNumber(message, start, end, null, null, allowSkip);
		
	}
	
	/**
	 * Request that the user choose a number.
	 * @param message The message displayed before " from X to Y".
	 * @param start Lower bound (inclusive)
	 * @param end Upper bound (inclusive)
	 * @param check An additional predicate that must pass before the input
	 * is accepted.
	 * @param checkMessage A message to display to the user on the predicate failing.
	 * @return The number chosen.
	 */
	protected int chooseNumber(String message, int start, int end, 
			Predicate<Integer> check, String checkMessage) {
		
		return chooseNumber(message, start, end, check, checkMessage, false);
		
	}
	
	/**
	 * Request that the user choose a number.
	 * @param message The message displayed before " from X to Y".
	 * @param start Lower bound (inclusive)
	 * @param end Upper bound (inclusive)
	 * @param allowSkip If true, allow the user to skip this choice.
	 * @param check An additional predicate that must pass before the input
	 * is accepted.
	 * @param checkMessage A message to display to the user on the predicate failing.
	 * @return The number chosen, or 0 if the user skipped the choice.
	 */
	protected int chooseNumber(String message, int start, int end, 
			Predicate<Integer> check, String checkMessage, boolean allowSkip) {
				
		while (true) {
			
			if (allowSkip)
				out.print("[P]ass, or ");
			
			out.println(message + " from " + start + " to " + end + ": ");
			out.flush();
			
			int input;
			try {
				
				String rawInput = in.nextLine().trim();
				
				if (allowSkip && (!rawInput.isEmpty()) && rawInput.toLowerCase().charAt(0) == 'p')
					return 0;
				
				input = Integer.parseInt(rawInput);
				
		
			} catch (NumberFormatException e) {
				
				out.println("Unable to read input.");
				continue;
				
			}
			
			if (input < start) {
				
				out.println("Input must be " + start + " or greater.");
				continue;
				
			}
			
			if (input > end) {
				
				out.println("Input must " + end + " or less.");
				continue;
				
			}
			
			if (check != null && !check.test(input)) {
				
				out.println(checkMessage);
				continue;
				
			}
			
			return input;
			
		}
		
	}
	
}
