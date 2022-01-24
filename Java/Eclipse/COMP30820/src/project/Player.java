package project;

import java.io.PrintWriter;
import java.util.Scanner;

import project.players.*;

/**
 * A named entity which can play games, and keep a score. 1 point is earned
 * per game won, games lost or tied have no effect.
 * 
 * @see Game
 * @see #play(Game)
 * @see Ghost
 * @see Honour
 * @see Special
 */
public class Player {
	
	private String name;
	
	private int score;	
	
	/**
	 * Creates a player with no name. The name should be set afterwards
	 * with {@link #setName(String)}.
	 */
	public Player() {
		
		this("(No name?)");
		
	}
	
	public Player(String name) {
		
		setName(name);
		
	}
	
	public String getName() {
		
		return name;
		
	}
	
	public void setName(String name) {
		
		this.name = name;
		
	}
	
	public int getScore() {
		
		return score;
		
	}
	
	/**
	 * Set the score back to zero.
	 */
	public void resetScore() {

		score = 0;
		
	}
	
	protected void setScore(int score) {
	
		this.score = score;
		
	}
	
	public boolean play(Game game) {
		
		boolean playerWin = game.play();
		
		if (playerWin)
			this.score += 1;
		
		return playerWin;
		
	}
	
	@Override
	public String toString() {
		
		return name + " - " + score;
		
	}
	
	/**
	 * Determines whether or not the player 
	 * should be saved between sessions.
	 */
	public boolean canSave() {
		
		// Don't save players with zero score.
		// Since there is no way to delete players, this
		// means that players created accidentally are not
		// saved.
		
		return score != 0;
		
	}
	
	/**
	 * Called when saving to let the Player save relevant data. This can
	 * be overridden by subclasses to save additional data. If this method
	 * is overriden, {@link #onLoad(PrintWriter)} should be overriden as well.
	 */
	public void onSave(PrintWriter writer) {
		
		writer.println(name);
		writer.println(score);
		
	}
	
	/**
	 * Called when loading to let the Player load relevant data. If this method
	 * is overridden, {@link #onSave(Scanner)} should be overriden as well.
	 */
	public void onLoad(Scanner scanner) {
		
		name = scanner.nextLine();
		score = Integer.parseInt(scanner.nextLine().trim());
		
	}
	
}
