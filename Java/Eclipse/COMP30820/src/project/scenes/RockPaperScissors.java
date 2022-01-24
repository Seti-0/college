package project.scenes;

import java.util.Random;

import project.Game;

/**
 * A {@link Game} of classic Rock, Paper Scissors, best of 3.
 */
public class RockPaperScissors extends Game {

	@Override
	public boolean play() {

		out.println("Paper Scissors!");
		out.println("(Best of 3)");
		out.println();
		
		int playerScore = 0;
		int computerScore = 0;
		
		while (true) {

			int playerChoice = 0;
			switch (showOptions("Rock", "Paper", "Scissors")) {
				case "Rock": playerChoice = 0; break;
				case "Paper": playerChoice = 1; break;
				case "Scissors": playerChoice = 2; break;
			}
			
			Random random = new Random();
			int computerChoice = random.nextInt(3);
			
			out.print("The computer chose ");
			switch (computerChoice) {
				case 0: out.println("Rock"); break;
				case 1: out.println("Paper"); break;
				case 2: out.println("Scissors"); break;
			}
			
			if (computerChoice == playerChoice)
				out.println("This round is a draw.");
			
			else if (playerChoice == ((computerChoice + 1) % 3)) {
				
				out.println("The player wins this round.");
				playerScore++;
				
			}
			
			else {
				
				out.println("The computer wins this round.") ;
				computerScore++;
				
			}
		
			if (playerScore >= 2){
				
				out.println("The player wins the game!");
				return true;
			
			}
			else if (computerScore >= 2) {
				
				out.println("The computer wins the game!");
				return false;
				
			}
			
			out.println("The game continues...");
			out.println();
			
		}
		
	}

}
