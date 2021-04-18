package assignments;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class MA4Q1 {

	public static void main(String[] args) {
		
		if (args.length == 0)
		{
			System.out.println("Usage: MA4Q1 [filename]");
			return;
		}
		
		try {
			
			String contents = Files.readString(Path.of(args[0]));
			
			System.out.println("File "+ args[0] + " has:");
			printSummary(contents);
			
		} catch (FileNotFoundException e) {
			
			System.out.println("File not found: '%s'".formatted(args[0]));
			
		} catch (IOException e) {
			
			System.out.println("Unable to read file: '%s'".formatted(args[0]));
			
		}
		
	}
	
	public static void printSummary(String text) {
		
		// Note: I'm aware the example in the Q shows 3 lines, but I think by the usual
		// definition of a line in a text file 'text.txt' has 4, with the last line being
		// empty.
		
		// Rather than complicate things by trying to detect empty lines, I'm leaving it
		// as is with "4" printed for the number of lines.
		
		int lines = 1;
		int words = 0;
		int characters = 0;
		
		boolean inWord = false;
		
		for (int i = 0; i < text.length(); i++) {
			
			char character = text.charAt(i);
			characters++;
			
			if (Character.isWhitespace(character)) {
				
				if (character == '\n')
					lines++;
				
				if (inWord)
					inWord = false;
				
			}
			else {
				
				if (!inWord) {
					
					inWord = true;
					words++;
					
				}
				
			}
			
		}
		
		System.out.println(characters + " characters");
		System.out.println(words + " words");
		System.out.println(lines + " lines");
		
	}
	
}
