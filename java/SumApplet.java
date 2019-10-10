import java.awt.event.*;
import java.awt.Color;
import java.awt.*;
import java.applet.*;

public class SumApplet extends Applet implements ActionListener {

	// Applet Label and TextBox
	 	Label num1 = new Label("Number 1: ");
	 	TextField box1 = new TextField();
	 	Label num2 = new Label("Number 2: ");
	 	TextField box2 = new TextField();
		Button result = new Button("Result");
		TextField box3 = new TextField();

	 public SumApplet() {	

	 	// Grid Layout 3X3
	 	// this.setLayout(new BorderLayout(2, 4));
	 	// this.setLayout(new FlowLayout());
	 	setLayout(new GridLayout(3, 2));

	 	// Background (awt)
	 	Color color = new Color(177, 165, 255);
	 	setBackground(color);

	 	// adding elements to the screen
	 	add(num1);
	 	add(box1);
	 	add(num2);
	 	add(box2);
	 	add(result);
	 	add(box3);

	 	// ActionListener
	 	result.addActionListener(this);

	}

	 public void actionPerformed(ActionEvent e) {
	 	// box3.setText("works!");
	 	String s1 = box1.getText();
	 	String s2 = box2.getText();
	 	int t1 = Integer.parseInt(s1);
	 	int t2 = Integer.parseInt(s2);
	 	// string result = String.toString(temp1 + temp2);
	 	int temp = t1 + t2;
	 	box3.setText(""+temp);
	}
}