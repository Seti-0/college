package scenes;

import base.Game;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Random;

/**
 * <p>
 * A card game similar to blackjack, found within the game
 * Star Wars - Knights of the Old Republic. 
 * </p>
 * <p>
 * There are two players, each with a total of points. 
 * Each round, a random amount of points
 * is added to the total. To goal is to reach as close to 20 as possible,
 * while not going over 20. The players start with 4 cards and can play them 
 * to affect their total. They can "commit", upon which they can no longer 
 * play cards and no longer recieve points. 
 * </p>
 * <p>
 * If both players have less than 20 at the end
 * of the game, the player closest to 20 wins. If both players have the 
 * same number of points at the end, the game ends in a draw.
 * </p>
 * */
public class Pazaak extends Game {

	private ArrayList<Integer> playerCards = new ArrayList<>();
	private ArrayList<Integer> computerCards = new ArrayList<>();
	
	private Random random = new Random();
	
	private boolean playerCommitted, computerCommitted;
	private int playerTotal, computerTotal;

	private boolean playerWin;
	private boolean computerWin;

	private void resetGame() {
		
		playerCards.clear();
		computerCards.clear();
		
		// Give each player 4 cards with random values
		// from 1 to 10 and -1 to -10.
		
		// The original game was best of 3, which I deemed to long
		// for this use case. This means that the players have way too
		// many cards... but I'm leaving it the way it is. It's fun and simple,
		// which suits the project.
		
		for (int i = 0; i < 4; i++) {
			
			int amount = 1 + random.nextInt(10);
			if (random.nextBoolean())
				amount = amount * -1;
			
			playerCards.add(amount);
			
			amount = 1 + random.nextInt(10);
			if (random.nextBoolean())
				amount = amount * -1;
			
			computerCards.add(amount);
			
		}
		
		playerTotal = 0;
		playerCommitted = false;
		
		computerTotal = 0;
		computerCommitted = false;
		
		playerWin = false;
		computerWin = false;
		
	}
	
	@Override
	public boolean play() {
		
		out.println("Welcome to Pazaak!");
		out.println();
		out.println("Recieve a random number of points each round.");
		out.println("Closest to 20 points wins.");
		out.println("Exceeding 20 means getting eliminated though!");
		out.println("Commit if you are getting too close.");
		out.println("Play cards to nudge things your way.");
		out.println();
		
		resetGame();
		
		while (true) {
			
			takePlayerTurn();
			
			out.println();
			shortPause();
			
			takeComputerTurn();
			
			out.println();
			shortPause();
			
			checkTotals();

			if (playerWin && computerWin) {
				out.println("This game is a draw.");
				return false;
			}
			
			else if (playerWin) {
				out.println("The player wins the game!");
				return true;
			}
			
			else if (computerWin) {
				out.println("The computer wins the game!");
				return false;
			}
			
			out.println("The game continues...");
			out.println();
				
		}
		
	}
	
	private void takePlayerTurn() {
		
		if (playerCommitted) {
			
			// "Committed" means that the player is content with the
			// current total. It only remains to see if the
			// computer will do better, now.
			
			out.println("Your total is: " + playerTotal);
			return;
			
		}
		
		// Add a random number of points from 1 to 10.
		
		int playerNext = 1 + random.nextInt(10);
		playerTotal += playerNext;
		
		out.println(playerNext + " is added to your total.");
		out.println("Your total is: " + playerTotal);		
		
		// If this pushes the player to 20 or above, depending on
		// the players cards there may be nothing more the player can
		// do.
		
		if (playerAutoCommit())
			return;
		
		// Allow the player to play a card, or pass.
		
		out.print("Your cards are: ");
		printItems(playerCards.iterator());
		int card = chooseNumber("choose a card", 1, playerCards.size(), true);
		
		if (card > 0) {
			
			int value = playerCards.remove(card - 1);
			
			playerTotal += value;
			out.println("Your total is: " + playerTotal);
			
			// The score has changed again, and the player may
			// no longer have anything to do.
			
			if (playerAutoCommit())
				return;
			
		}	
		
		// There is no point committing before the score
		// is at least 10. But if it is, give the player the option.
		
		if (playerTotal > 10) {
			
			if (askQuestion("Do you want to commit?")) {
				
				playerCommitted = true;
				out.println("base.Player committed");
				
			}	
			
		}
		
	}
	
	private boolean playerAutoCommit() {
		
		if (playerTotal == 20) {
			
			// This is the best state the player can be in.
			// It's either a win or a draw from here.
			
			out.println("Score is 20, auto-committing.");	
			playerCommitted = true;
			return true;
			
		}
		
		if (playerCards.size() == 0) {
			
			// Playing cards is the only action 
			// a player can take.
			
			out.println("No moves left, auto-committing.");
			playerCommitted = true;
			return true;
			
		}
		
		// If the player has no cards capable of bringing 
		// them back from having gone bust, there is nothing
		// more to be done.
		
		int comebackAbility = 0;
		for (int value : playerCards)
			if (value < comebackAbility)
				comebackAbility = value;
		
		if (playerTotal + comebackAbility > 20) {
			
			out.println("No comeback possible, auto-committing.");
			playerCommitted = true;
			return true;
		}
		
		return false;
		
	}
	
	private void takeComputerTurn() {
		
		if (computerCommitted) {
			
			// "Committed" means that the computer is content
			// with the current total. It only remains to see if
			// the player will do better.
			
			out.println("The computer's total is: " + computerTotal);
			return;
			
		}
		
		// Add a random number from 1 to 10 to the total.
		
		int next = 1 + random.nextInt(10);
		computerTotal += next;
		
		out.println(next + " is added to the computer's total.");
		out.println("The computer's total is: " + computerTotal);
		
		// Check which card (if any) it makes most sense
		// to play. The card chosen is the one that gets 
		// the computer closest to 20, but not over 20.
		
		int possibleCard = -1;
		int possibleDistance = 20;
		for (int i = 0; i < computerCards.size(); i++) {
			
			int value = computerCards.get(i);
			int distance = 20 - (value + computerTotal);
			
			if (distance < 0)
				continue;
			
			if (distance < possibleDistance) {
				
				possibleCard = i;
				possibleDistance = distance;
				
			}
			
		}
		
		// If there is a card, and the computer is about to go
		// bust, play it. Might as well!
		
		// If the computer is safe-ish at the moment, though, only
		// play it if the distance is decent.
		
		boolean playCard = possibleCard >= 0
				&& (computerTotal > 20 || possibleDistance < 5);
		
		if (playCard) {
			
			int value = computerCards.remove(possibleCard);
			computerTotal += value;
			
			out.println("The computer plays a card of value: " + value);
			out.println("The computer's total is: " + computerTotal);
			
		}
		
		// Finally, the question of whether or not to commit. 
		// This is a decision tree.
		
		Comparator<Integer> simple = Comparator.comparing(Integer::valueOf);
		int danger = 20 + computerCards.stream().min(simple).orElse(0);
		
		boolean commit = 
				
				// The player can't win, may as well commit.
				playerTotal > 20 
				
				// Autocommit either way because of game rules.
				|| computerTotal >= 20
				
				// Don't commit if the player is ahead, that just means losing.
				|| (computerTotal >= playerTotal && ( 
						
						// Dangerously high...
						danger > 18 
						
						// Fairly high. Maybe commit, maybe not.
						|| (random.nextBoolean() && danger > 15) 
						));
		
		if (commit) {
			
			out.println("The computer commits.");
			computerCommitted = true;
			return;
			
		}
		
	}
	
	private void checkTotals() {
		
		// The goal is reach 20.
		// If you exceed 20, you lose though.
		
		// Both players winning is a draw, both players
		// losing is a draw.
		
		// Finally, note that even if one player has commited,
		// the other may have moves to make. So the player with, say,
		// 20 currently, has not won until the other player has commited.
		// (And it may end up being a draw instead of a win)
		
		if (playerTotal == 20 && computerCommitted)
			playerWin = true;
		
		if (computerTotal == 20 && playerCommitted)
			computerWin = true;
		
		if (computerTotal > 20 && playerCommitted)
			playerWin = true;
		
		if (playerTotal > 20 && computerCommitted)
			computerWin = true;
		
		if (playerCommitted && computerCommitted)
			if (playerTotal < 20 && computerTotal < 20) {
				
				playerWin = playerTotal > computerTotal;
				computerWin = !playerWin;
			
			}
		
	}

}
