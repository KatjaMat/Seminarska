import java.awt.Graphics;

public class GlavaKace extends Kaca {
	
	private int r = 10;
	
    public GlavaKace(int x, int y, int r) {
        super(x, y);
        this.r = r; 
    }
    

    @Override
    public void narisiSe(Graphics g) {
        int x = 150;
		int y = 150;
		g.fillOval(x - r, y - r, 2*r, 2*r);
        
    }

    @Override
    public String toString() {
        return String.format("Krog [r=%d]", r);
    }
    
    
}
