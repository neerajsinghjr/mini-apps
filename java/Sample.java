import Java.Applet.*; 
import Java.awt.*; 
import Java.awt.event.*; 

public class Sample 
{ 
	public static void main (String[] args) 
	{ 
		Frame f = new Frame("TestMouseListener"); 
		f.setSize(500,500); 
		f.setVisible(true); 
		f.addMouseListener(new MouseAdapter() 
			{ 
				public void mouseClicked(MouseEvent e) 
				{ 
					System.out.println("Mouse clicked: ("+e.getX()+","+e.getY()+")"); 
				} 
			}); 
	} 
}