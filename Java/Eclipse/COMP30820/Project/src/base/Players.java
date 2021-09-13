package base;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.*;
import java.util.function.Supplier;

/**
 * Maintains a list of base.Players, and base.Player types.
 * <p>
 * A player type can be registered with a type name. A new player can be
 * added directly, or created using a type name. The list of players 
 * can be saved to or loaded from a text file.
 * </p>
 * 
 * @see #register(String, Supplier)
 * @see #add(Player, String)
 * @see #save()
 * @see Player
 */
public class Players {
	
	private static HashMap<String, Supplier<Player>> suppliers = new HashMap<>();
	
	private static HashMap<String, Player> players = new HashMap<>();
	private static HashMap<String, String> playerTypes = new HashMap<>();
	
	private static HashSet<String> hiddenTypes = new HashSet<>();
	
	/**
	 * Register a new type of {@link Player}.
	 * @param name The name of the type.
	 * @param supplier A function by which a new player of this type
	 * can be created.
	 */
	public static void register(String name, Supplier<Player> supplier) {
		
		suppliers.put(name, supplier);
		
	}
	
	/**
	 * Set whether ot not a player type should be visible
	 * to the user. 
	 * 
	 * @see #getTypes()
	 * @see #add(String, String)
	 */
	public static void setHidden(String name, boolean hidden) {
		
		if (hidden)
			hiddenTypes.add(name);
		else
			hiddenTypes.remove(name);
		
	}
	
	/**
	 * Get a list of player types. Does not include hidden
	 * types.
	 * 
	 * @see #setHidden(String, boolean)
	 * @see #getTypes(boolean)
	 */
	public static Set<String> getTypes() {
		
		return getTypes(false);
		
	}
	
	/**
	 * Get a list of player types.
	 * @param includeHidden Whether or not to include types that
	 * should be hidden to the user.
	 * 
	 * @see #setHidden(String, boolean)
	 */
	public static Set<String> getTypes(boolean includeHidden) {
		
		Set<String> set = new HashSet<>(suppliers.keySet());
		set.removeAll(hiddenTypes);
		
		return set;
		
	}
	
	/**
	 * Retrieve an existing player by name. Returns null
	 * if no player of that name exists.
	 */
	public static Player get(String name) {
		
		return players.get(name);
		
	}
	
	/**
	 * Create a new player with a given name, of a registered
	 * player type. If a player of the same name already exists,
	 * it is replaced.
	 * 
	 * @see #register(String, Supplier)
	 * @see #getTypes()
	 * @see #get(String)
	 */
	public static Player add(String name, String playerType) {
		
		Supplier<Player> supplier = suppliers.get(playerType);
		if (supplier == null)
			throw new IllegalArgumentException("Unrecognized player type!");
		
		Player player = supplier.get();
		player.setName(name);
		
		add(player, playerType);
		
		return player;
		
	}
	
	private static void add(Player player, String playerType) {
		
		players.put(player.getName(), player);
		playerTypes.put(player.getName(), playerType);
		
	}
	
	/**
	 * Get a list of existing player names.
	 */
	public static Collection<Player> getPlayers() {
		
		return new ArrayList<Player>(players.values());
		
	}
	
	/**
	 * Save current players to a text file. Overwrites the previous save
	 * if it exists, creates a new file if it does not.
	 * <p>
	 * Note that {@link Player} objects can request to not be saved.
	 * If there are no players to be saved, the previous save is deleted, 
	 * if it exists. No action is taken if it does not.
	 * </p>
	 * @see #load()
	 */
	public static void save() {
		
		File file = new File("players.sav");
		
		if (players.values().stream().allMatch(x -> !x.canSave())) {
			
			if (file.exists())
				file.delete();
			
			return;
			
		}
		
		if (!file.exists())
			try {
				
				if (!file.createNewFile())
				{
					System.out.println("Failed to create file: " + file.getAbsolutePath());
					return;	
				}
			
			} catch (IOException e1) {
				
				System.out.println("Failed to create file: " + file.getAbsolutePath());
				e1.printStackTrace();
				return;
			}
		
		// Because an error in saving one player may effect 
		// the rest of the data, the save is either entirely
		// successful or fails entirely.
		
		// This is an unfortunate aspect of saving things line
		// by line in an unstructured stream.
		
		try (PrintWriter out = new PrintWriter(file)) {
			
			for (Player player : players.values()) {
				
				if (!player.canSave())
					continue;
			
				String playerType = playerTypes.get(player.getName());
				
				out.println(playerType);
				player.onSave(out);
				out.println();
				
			}
			
		} catch (FileNotFoundException e) {

			System.err.println("Unable to write to file: " + file.getAbsolutePath());
			e.printStackTrace();
			
		} catch (Exception e) {
			
			System.err.println("Exception occured while attempting to save players.");
			e.printStackTrace();
			
		}
		
	}
	
	/**
	 * Attempts to load player information from a previous save.
	 * If no previous save exists, this method has no effect.
	 * 
	 * @see #save()
	 */
	public static void load() {
		
		File file = new File("players.sav");
		
		if (!file.exists())
			return;
		
		// Because an error in loading one player may effect 
		// the rest of the data, the load is either entirely
		// successful or fails entirely.
		
		// This is an unfortunate aspect of saving things line
		// by line in an unstructured stream.
		
		try (Scanner scanner = new Scanner(file)) {
			
			while (scanner.hasNext()) {
				
				String playerType = scanner.nextLine();
				Player player = suppliers.get(playerType).get();
				
				player.onLoad(scanner);	
				
				add(player, playerType);
				
				scanner.nextLine();
				
			}
			
		} catch (FileNotFoundException e) {

			System.err.println("Unable to write to file: " + file.getAbsolutePath());
			e.printStackTrace();
			
		} catch (Exception e) {
			
			System.err.println("Error occured while attempting to load players.");
			e.printStackTrace();
			
		}
		
	}
	
}
