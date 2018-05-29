import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import javax.swing.JPanel;
import javax.swing.Timer;

public class Platno extends JPanel implements ActionListener {
    private List<Lik> liki;
    private Kaca kaca;
    private Krogec krogec;
    protected boolean igraTece;
    private Timer timer;
    
    public Platno() {
        super();
        this.liki = new ArrayList<Lik>();
        this.setBackground(Color.LIGHT_GRAY);
        igraTece = false;

        
        timer = new Timer(20,this);
        timer.start();
        //timer.addActionListener(this);
        
    }
    
    public void dodajLik(Lik lik) {
        liki.add(lik);
    }
    
    public void narisiKaco() {
    	kaca = new Kaca(100, 100);
    	dodajLik(kaca);
    	repaint();
    }
    
    public void narisiKrogec() {
    	Random rand = new Random(); 
    	int x = rand.nextInt(700);
    	int y = rand.nextInt(700);
    	krogec = new Krogec(x, y);
    	dodajLik(krogec);
    	repaint();
    }
    
    
    public void brisi() {
        liki.clear();
        repaint();
    }


    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.red);
        for(Lik lik: this.liki) {
            lik.narisiSe(g);
        }
    }

    @Override
    public Dimension getPreferredSize() {   
        return new Dimension(700, 700);
    }

	@Override
	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == timer){
			if (igraTece){
				kaca.x += 1;
				repaint();
				System.out.println("0");
			}
		}
		
	}
    
    
}
