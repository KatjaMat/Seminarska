
import java.awt.*;
import java.util.List;
import javax.swing.*;
import java.util.Random;

public class Krogec extends Lik{	
	
    public Krogec(int x, int y) {
        super(x, y);
    }

	@Override
	public void narisiSe(Graphics g) {
		g.setColor(Color.RED);
		g.fillOval(x, y, 25, 25);
	}
	

}

