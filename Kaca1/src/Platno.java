import java.awt.Color;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.Timer;

public class Platno extends JPanel implements ActionListener {
    private List<Lik> liki;
    protected Kaca kaca;
    private Krogec krogec;
    protected boolean igraTece;
    private Timer timer;
    private int stevec = 0;
    private JLabel tocke;
    
    public Platno() {
        super();
        this.liki = new ArrayList<Lik>();
        this.setBackground(Color.LIGHT_GRAY);
        igraTece = false;

        
        timer = new Timer(20,this);
        timer.start();
        
        this.tocke = new JLabel("TOÈKE: "+ stevec);
        tocke.setBounds(0, 600, 100, 50);
        this.add(tocke);
        
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
    	int krogecx = rand.nextInt(680);
    	int krogecy = rand.nextInt(680);
    	krogec = new Krogec(krogecx, krogecy);
    	dodajLik(krogec);
    	repaint();
    }
    
    
    public void brisi() {
        liki.clear();
        repaint();
    }
    
    public void pojejBonboncek (){
    	if ((kaca.x >= krogec.x-12 && kaca.x <= krogec.x+12) && (kaca.y >= krogec.y-12 && kaca.y <= krogec.y+12)){
        	krogec.x = 1500;
    		krogec.y = 1500;
    		narisiKrogec();
    		stevec += 1;
    		tocke.setText("TOÈKE: "+ stevec);
    		
    	}
    }
    public void zaletiSe (){
    	if((kaca.x >= 700)|| (kaca.x <= 0) || (kaca.y >= 700) || (kaca.y <= 0)){
    		kaca.x = 100;
    		kaca.y = 100;
    		igraTece = false;
    		stevec = 0;
    		tocke.setText("TOÈKE: "+ stevec);
    		
    	}
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
			//KONTROLSI
			if (igraTece){
				if(Okno.levo){
					kaca.x-=3;
				}
				else if(Okno.desno){
					kaca.x += 3;
				}
				else if(Okno.gor){
					kaca.y -= 3;
				}
				else if(Okno.dol){
					kaca.y += 3;
				}
				zaletiSe();
				pojejBonboncek();
				repaint();
			}
		}
		
	}
    
	
    
}
