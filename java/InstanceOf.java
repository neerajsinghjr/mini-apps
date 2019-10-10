
public class InstanceOf{
	int value = 10;
	public static void main(String args[]){
		var result = value instanceof Integer;
		System.out.println("Result: " + result);
		// System.out.println(typeof(value)); // typeof() is absent in java !!! 
	}
}

public class InstanceOf {

   public static void main(String args[]) {
      String name = "James";
      boolean result = name instanceof String;
      System.out.println( result );
      // System.out.println( typeof(name) ); // typeof() is absent in java !!!
   }

}