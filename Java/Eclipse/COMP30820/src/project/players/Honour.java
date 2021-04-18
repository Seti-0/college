package project.players;

import project.Game;
import project.Player;

/**
 * A {@link Player} whose score is reset each time they
 * fail to win a game. Victory is all!
 */
public class Honour extends Player {

	@Override
	public boolean play(Game game) {

		boolean playerWin = super.play(game);
		
		if (!playerWin)
			resetScore();
		
		return playerWin;
		
	}
	
	@Override
	public String toString() {

		return "(Honour) " + super.toString();
		
	}
	
}
