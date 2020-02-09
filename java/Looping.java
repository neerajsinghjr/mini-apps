public class Looping{

	public static void main(String args[]){

		int number[] = {10, 20, 30 , 40, 50, 60, 70, 80, 90, 100};
		String name[] = {"apple", "banana", "mango", "grapes", "pineApple", "guawa"};

		// Iterating Through the numbers
		for( int x : number){
			System.out.println(x + "\r");
		}

		// Iterating Through the names
		for( String x : name){
			System.out.println(x);
		}
	}
}