package SexyGirls;

public class Employee{
	String name;
	int age;
	float salary;
	String designation;

	// Default Constructor
	public Employee(){
		System.out.println("Default Constructor Called!");
	}

	// Parameter Constructor
	public Employee(String name, int age, float salary, String designation){
		this.name = name;
		this.age = age;
		this.salary	= salary;
		this.designation = designation;
	}

	// Display the details
	public void display(){
		System.out.println("Name: " + name);
		System.out.println("Age: " + age);
		System.out.println("Salary: " + salary);
		System.out.println("Designation: " + designation);
	}
}
