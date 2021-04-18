package project.scenes;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import project.Games;
import project.Player;
import project.Players;
import project.Scene;

/**
 * The main and starting {@link Scene} of the application - 
 * shows the main menu, login, scores and allows the user to select and
 * start a game.
 *
 * @see #showMain()
 * @see Scene
 * @see Main
 * @see Games
 * @see Players
 */
public class Menu extends Scene {
	
	/**
	 * Show the main menu. From here, the user can show scores,
	 * or login and play games. Scores are also displayed on exiting 
	 * the main menu.
	 * 
	 * @see Players
	 * @see Games
	 */
	public void showMain() {
		
		out.println("Welcome to the Games Cupboard!");
		
		// This is the main application loop. 
		// (It's not the only application loop though - game selection
		// has a loop, and each game will have their own loop too.)
		
		while (true) {
			
			switch (showMenu("Play", "Show Scores", "Quit")) {
				case "Play": showLogin(); break;
				case "Show Scores": showScores(); pause(); break;
				case "Quit": showScores(); return;
					
			}	
			
		}
		
	}
	
	private void showLogin() {
		
		// Players are considered to have unique names in this 
		// app. So if a name is given that was saved before, this
		// is treated as "logging in".
		
		out.println("Enter name:");
		out.println("(Leave empty to return to main menu)");
		out.flush();
		
		String name = in.nextLine().trim();
		
		if (name.isEmpty())
			return;
		
		Player player = Players.get(name);
		
		// If the player already exists, no need to specify
		// a type. If it does not, there is.
		
		if (player == null) {
			
			out.println("Welcome, " + name + "!");
			out.println("Select player type:");
			
			String selection = showMenu(Players.getTypes());
			
			if (selection == null)
				return;
			
			player = Players.add(name, selection);
			
		} else {
			
			out.println("Welcome back, " + name + ".");
			
		}
		
		showGameSelection(player);
		
	}
	
	private void showGameSelection(Player currentPlayer) {
		
		// The second application loop - game selection.
		
		while (true) {
			
			out.println("Game Selection:");
			
			String selection = showMenu(Games.getNames());
			
			// The selection is null if the user selects the return option
			// in the menu.
			if (selection == null)
				return;
			
			currentPlayer.play(Games.create(selection));	
			
			out.println();
			
			pause();
			
			// Save after every game. This means that the user can terminate
			// the app (by x-out, or ctrl-c, for example) without worrying about
			// losing data.
			
			out.println("Saving scores...");
			Players.save();
			out.println("Save complete.");
			out.println();
			
		}
		
	}
	
	private void showScores() {
		
		// Don't show players with no score. This is partially 
		// because some special players are hardcoded in but should 
		// not be shown by default, and partially because users made
		// by mistake and never used should not be shown.
		// (There is no way to delete a player, strictly speaking, though
		// players without a score do no persist between sessions)
		
		List<Player> players = new ArrayList<>(Players.getPlayers());
		players.removeIf(x -> x.getScore() == 0);
		Collections.sort(players, (a,b) -> b.getScore() - a.getScore());
		
		if (players.isEmpty()) {
			
			out.println("There are no scores to show yet...");
			return;
			
		}
		
		out.println("=== Scores ===");
		out.println();
		
		for (Player player : players)
			out.println(player);
		
		out.println();
		out.println("==============");

	}
	
}
