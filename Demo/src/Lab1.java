import javax.swing.*;
import java.util.Scanner;

public class Lab1 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        // part2();

        // part3q1(in);

        // part3q2();

        part4(in);

        // Remember, this closes the underlying input stream!
        in.close();

    }

    public static void part2() {
        // q1
        System.out.println("Hello World!");

        // q2
        System.out.println("Another!");
        System.out.println("And another!");

        // q3
        for (int i = 0; i < 5; i++) {
            System.out.println("Every time...");

            // q4
            System.out.println("Current: " + i);
        }
    }

    public static void part3q1(Scanner in) {
        System.out.println("Enter your name: ");
        String name = in.nextLine();

        System.out.println("Hello " + name + "!");
    }

    public static void part3q2() {

        String name = JOptionPane.showInputDialog("Enter your name:");
        JOptionPane.showMessageDialog(null, "Hello " + name + "!");

    }

    public static void part4(Scanner in) {

        System.out.println("Enter a: ");
        String aText = in.nextLine();
        System.out.println("Enter b: ");
        String bText = in.nextLine();

        int a = Integer.parseInt(aText);
        int b = Integer.parseInt(bText);

        // q1
        int c = a + b;

        System.out.println("a + b is: " + c);

        // q2
        int d = add(a, b);
        System.out.println("add(a,b) is: " + d);
    }

    public static int add(int a, int b) {
        return a + b;
    }

}
