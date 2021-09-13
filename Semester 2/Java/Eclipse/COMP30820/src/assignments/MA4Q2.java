package assignments;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.time.LocalDateTime;

public class MA4Q2 {

	public static void main(String[] args) {
		
		if (args.length == 0)
		{
			System.out.println("Usage: MA4Q1 [filename]");
			return;
		}
		
		String newName = args[0] + LocalDateTime.now();
		
		// The date time string may contain characters like ":",
		// which are not compatible with the windows file system at least.
		newName = newName.replaceAll("[^a-zA-Z0-9\\/._]", "_");
		
		try {
			
			Files.move(Path.of(args[0]), Path.of(newName), StandardCopyOption.REPLACE_EXISTING);
			System.out.println("File renamed to '" + newName + "'.");
		
		} catch (IOException e) {
			
			System.out.println("Unable to rename file.");
		
		}

	}

}
