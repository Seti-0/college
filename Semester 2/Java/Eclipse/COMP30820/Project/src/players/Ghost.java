package players;

import base.Player;

/**
 * A transient {@link Player} which is never saved
 * between sessions.
 * 
 * @see #canSave()
 */
public class Ghost extends Player {
	
	@Override
	public boolean canSave() {
		
		// A Ghost is never saved between sessions.
		
		// Since players cannot be explictly deleted, this allows
		// a user to play anonymously, and was handy for testing
		// without adding to the save file too.
		
		return false;
	
	}

	@Override
	public String toString() {

		return "(Ghost) " + super.toString();
		
	}
	
}
