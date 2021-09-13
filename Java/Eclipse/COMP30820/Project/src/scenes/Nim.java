package scenes;

import base.Game;

import java.util.Arrays;
import java.util.Random;

/**
 * A {@link Game} in which there are several piles
 * of items and two players. base.Players take turns to choose
 * one pile and take any number of items from it. The player 
 * who takes the last item in the game loses.
 *
 */
public class Nim extends Game {

	@Override
	public boolean play() {
		
		out.println("Welcome to Nim!");
		out.println();
		out.println("Remove items from a pile each round.");
		out.println("But don't be the one to remove the last item!");
		out.println();
		
		// Generate 3 piles of items with between 2 and 5 items (inclusive)
		
		final int n_piles = 3;
		int[] piles = new int[n_piles];
		
		Random random = new Random();
		
		for (int i = 0; i < piles.length; i++)
			piles[i] = 2 + random.nextInt(4);

		out.print("Piles: ");
		printItems(piles);
		
		// Each turn, the player selects a pile and an amount of
		// items and removes that amount of items from the pile.
		
		// The computer does the same, pretty much at random.
		
		// If someone takes the last item in the game, the other
		// person wins.
		
		while (true) {
			
			// base.Player's Turn
			
			int selection = chooseNumber("Choose a pile", 1, piles.length,
					choice -> piles[choice - 1] != 0, "That pile is already empty!");			
			
			selection--;
			
			int amount;
			if (piles[selection] == 1)
				amount = 1;
			
			else {
				
				amount = chooseNumber("Choose an amount", 1, piles[selection]);
				out.println();
				
			}
			
			piles[selection] -= amount;
			if (piles[selection] < 0)
				piles[selection] = 0;
			
			out.print("Piles: ");
			printItems(piles);
			out.println();
			
			if (Arrays.stream(piles).sum() == 0) {
				out.println("The computer wins!");
				return false;
			}
			
			// Computer's Turn
			
			do
				selection = random.nextInt(piles.length);
			while (piles[selection] == 0);
			
			amount = 1;
			
			int pilesLeft = Arrays.stream(piles)
					.map(Integer::signum)
					.sum();
			
			// Take more, possibly, but not if it means losing straight away.
			if (pilesLeft > 1)
				amount += random.nextInt(piles[selection] - 1);
			
			else if (piles[selection] > 2)
				amount += random.nextInt(piles[selection] - 2);
			
			out.println("The computer takes " + amount 
					+ " item(s) from pile "+ (selection + 1) + ".");
			
			out.println();
			
			piles[selection] -= amount;
			
			out.print("Piles: ");
			printItems(piles);
			
			if (Arrays.stream(piles).sum() == 0) {
				out.println("The player wins!");
				return true;
			}
			
		}
		
	}	
		
}
