package exam2;

public class Test {
	public static void main(String[] args) {
		
		// declare, create and initialise an array of Person objects
		// When you have implemented Manager and Employee, you should be able
		// to uncomment the commented code below.
		Person[] people = {
			    new Manager("C. Darwin", 455, "c.darwin@species.com", 150000, 1000, "Room 101"),
				new Person("J. Doe", 200, "j.doe@supermail.com"), 
				new Student("A. Bee", 120, "a.bee@bettermail.com", "19000091"), 
			    new Employee("B. Cee", 111, "b.cee@okmail.com", 50000), 
				new Student(),
			    new Manager("A. Einstein", 105, "a.einstein@emc2.com", 100000, 2000, "Room 202")					
		};
		
		// display the objects
		display(people);
		
		// display student numbers
		displayNumbers(people);
	}
	
	// displays each object in the array
	public static void display(Person[] arr) {
		for (int i = 0; i < arr.length; i++)
			System.out.println(arr[i].toString());
	}
	
	public static void displayNumbers(Person[] arr) {
		for (int i = 0; i < arr.length; i++)
			if (arr[i] instanceof Student)
				System.out.println(((Student) arr[i]).getNumber());
	}
}
