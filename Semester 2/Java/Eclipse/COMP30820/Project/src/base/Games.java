package base;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

/**
 * Maintains a list of games keyed by name. 
 * 
 * @see #add(String, Game)
 * @see #get(String)
 * @see #getNames()
 * @see Game
 */
public class Games {

	private static HashMap<String, Game> games = new HashMap<>();
	
	/**
	 * Add a new game.
	 * @param name The name of the game. If a game of this name already exists,
	 * it is replaced.
	 * @param game The new game.
	 */
	public static void add(String name, Game game) {
		
		games.put(name, game);
		
	}
	
	/**
	 * Retrieve a list of all currently available game names.
	 */
	public static Set<String> getNames() {
		
		return new HashSet<String>(games.keySet());
		
	}
	
	/**
	 * Create a new game.
	 * 
	 * @param name The name the game was added with.
	 * @throws IllegalArgumentException if the name is
	 * not recognized.
	 */
	public static Game get(String name) {
		
	    Game game = games.get(name);
		
		if (game == null)
			throw new IllegalArgumentException("Unrecognized game: " + name);
		
		return game;
		
	}
	
}
