package base;

import scenes.Nim;
import scenes.Pazaak;
import scenes.RockPaperScissors;

/**
 * A {@link Scene} that can be played.
 * 
 * @see #play()
 * @see Nim
 * @see RockPaperScissors
 * @see Pazaak
 *
 */
public abstract class Game extends Scene {

	/**
	 * Play the game, using the input and output channels from base.Main.
	 * 
	 * @return True if the player won, false if the player lost or the 
	 * game was a draw.
	 * 
	 * @see Main
	 * @see Scene
	 * */
	public abstract boolean play();
	
}
