import java.awt.*;
import java.util.List;
import javax.swing.*;


public class Kaca extends Lik{	
	
    public Kaca(int x, int y) {
        super(x, y);
    }

	@Override
	public void narisiSe(Graphics g) {
		g.setColor(Color.BLACK);
		g.fillOval(x, y, 25, 25);
		
	}

}