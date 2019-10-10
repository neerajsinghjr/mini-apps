public class CharacterClass{

	public static void main(String args[]){
		
		char letter = 'c';
		System.out.println(Character.toString(letter));

		boolean result = letter instanceof String;
		System.out.println(result);

	}
}