class Animal {
	Animal() {
		System.out.println("Animal chiggy chiggy bhau bhau !");
	}
	public void speciality(){
		System.out.println("They can crawl, bark or meow.");
	}
	public void animal(){
		System.out.println("Animal");
	}
}

class Dog extends Animal{
	Dog() {
		System.out.println("Dog Bhoww Bhoww !");
	}
	public void speciality() {
		super.speciality();
		System.out.println("Dog can bark");
	}
	public void dog(){
		System.out.println("Dog");
	}
}

class Cat extends Animal{
	public Cat() {
		System.out.println("Cat meoow meoow !");
	}
	public void speciality() {
		System.out.println("Cat can meow");
	}
	public void cat(){
		System.out.println("Cat");
	}
}

public class MethodOverriding {
	public static void main(String args[]) {
		// Animal a = new Animal();
		Animal d = new Dog();
		// Animal c = new Cat();

		/* CASE 1: Animal Reference with Dog */
		// a = d;
		// a.animal();
		// d.dog();	// Animal reference can't find the method dog()
		d.speciality();	// Animal reference call the speciality() method of dog because its upgraded
		// d.animal();	// Animal reference call the animal() method of class Animal.

	}
}