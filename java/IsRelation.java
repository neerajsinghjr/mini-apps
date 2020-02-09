/* Is-A-Relationship check whether the object belongs to that class or alternatively instanceof  in inheritnace */

class Grandfather {
	Grandfather(){
		// System.out.println("Grandfather");
	}
}

class Father extends Grandfather {
	Father() {
		// System.out.println("Father");
	}
}

class Son extends Father {
	Son() {
		// System.out.println("Son");
	}
}

class SonChild extends Son  {
	SonChild() {
		// System.out.println("SonChild");
	}
}

class StepChild {
	StepChild () {
		// System.out.println("SonChildChild");	
	}
}
class IsRelation {
	public static void main(String[] args) {
		SonChild a = new SonChild();
		Son b = new Son();
		StepChild x = new StepChild();

		System.out.println(a instanceof Grandfather);
		System.out.println(b instanceof Grandfather);
		// System.out.println(x instanceof Grandfather);
	}
}