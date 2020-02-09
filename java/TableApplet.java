import java.awt.*;
import java.awt.event.*;
import java.awt.Color;
import java.applet.*;

public class TableApplet extends Applet implements ActionListener{
	// Adding TextField;
	Label label = new Label("Your Number:");
	TextField number = new TextField();
	Button result = new Button("Result");

	public TableApplet() {
		// Setting background
		this.setLayout(new GridLayout(1,2));

		// background color
		setBackground(Color.cyan);

		// Adding Elements to Screen
		add(label);
		add(number);
		add(result);
		result.addActionListener(this);

		// g.drawString("Message",100, 90);
	}

	public void actionPerformed(ActionEvent e) {
		// number.setText("works!");
		String temp = number.getText();
		int value = Integer.parseInt(temp);
		if(value >= 0 && value <= 20){
			createTable(value);
		}else{
			throwWarning();
		}
	}

	public void createTable(int value){
		Graphics g;
		for(int i=1; i<10; i++){
			// sum 
		}
	}

	public void throwWarning() {
		Graphics g;
		// g.drawString("Task Fail: Overflown", 200, 90);
	}

}