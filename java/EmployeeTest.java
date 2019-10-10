import SexyGirls.Employee;

public class EmployeeTest{
	public static void main(String args[]){
		Employee manoj = new Employee();	
		Employee ganesh = new Employee("Ganesh Bhatt", 26, 30000, "Assistant Unit Tester");
		manoj.display();
		ganesh.display();
	}
}