import java.awt.*;
import java.util.List;
import javax.swing.*;


public class Kaca {
	
	private JFrame okno;
	private JPanel ozadje;
	private static int yKaca;
	private static int xKaca;
	public void narisiSe(Graphics g) {
	}
	
	
	public Kaca(int x, int y){
		platno();
        this.xKaca = x;
        this.yKaca = y;
        
	}
		
	public void platno(){ /* Naše platno */
		okno = new JFrame("Marjan");
		okno.pack();
		okno.setVisible(true);
		okno.setSize(700,700);
		okno.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		ozadje = new JPanel();
		ozadje.setBackground(Color.white);
		okno.add(ozadje);
			
			
		}


	public static void main(String[] args) {
		new Kaca(xKaca, yKaca);
	}
	
}