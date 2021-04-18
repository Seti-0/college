package project;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.function.Supplier;

/**
 * Maintains a list of games keyed by name. 
 * 
 * @see #register(String, Supplier)
 * @see #create(String)
 * @see #getNames()
 * @see Game
 */
public class Games {

	private static HashMap<String, Supplier<Game>> suppliers = new HashMap<>();
	
	/**
	 * Register a new game.
	 * @param name The name of the game. If a game of this name already exists,
	 * it is replaced.
	 * @param supplier A supplier with which a new insteance of this game can
	 * be created.
	 */
	public static void register(String name, Supplier<Game> supplier) {
		
		suppliers.put(name, supplier);
		
	}
	
	/**
	 * Retrieve a list of all currently registered game names.
	 */
	public static Set<String> getNames() {
		
		return new HashSet<String>(suppliers.keySet());
		
	}
	
	/**
	 * Create a new game.
	 * 
	 * @param name The name the game was registered with.
	 * @throws IllegalArgumentException if the name is
	 * not recognized.
	 */
	public static Game create(String name) {
		
		Supplier<Game> supplier = suppliers.get(name);
		
		if (supplier == null)
			throw new IllegalArgumentException("Unrecognized game: " + name);
		
		return supplier.get();
		
	}
	
}
