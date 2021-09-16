public class Lab1P3Q3 {

    private String greeting;

    /*
     * This is a constructor, it creates a new instance of your class
     * It also takes a String as input to initialise the class
     * The variable that is instantiated (above) is called an instance variable
     * Instance variables are specific ways to store data in a class
     * Every class has its own values for the instance variables
     */

    public Lab1P3Q3(String s) {
        //here we initialise greeting with the value in s
        greeting = s;
    }

    public void sayHello() {
        //insert code here to get input from the user
        String name = "";

        System.out.println(greeting + " " + name);
    }

    public static void main(String[] args) {
        //now we see how to reuse and repurpose our code above
        // Lab1P3Q3 english = new Lab1P3Q3("Greetings");
        // Lab1P3Q3 irish = new Lab1P3Q3("Dia dhuit");
        Lab1P3Q3 german = new Lab1P3Q3("Guten Tag");
        Lab1P3Q3 french = new Lab1P3Q3("Bonjour");

        //Now if we call the methods of our two Objects
        //english.sayHello();
        //irish.sayHello();
        german.sayHello();
        french.sayHello();

        /*
         * We retain the basic functionality, but out instance variable: greeting
         * allows us to change how the class behaves
         *
         * Note that we cannot call sayHello without creating an instance of the class
         * we must use the dot notation to call the method on an instance of our class
         * i.e. the following is incorrect Java, uncomment the line and see what the compiler says
         */

        //sayHello();
    }

}
