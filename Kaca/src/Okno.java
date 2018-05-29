import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.KeyEventDispatcher;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JButton;
import javax.swing.JFrame;

public class Okno extends JFrame implements ActionListener {
    private Platno platno;
    private JButton gumb;
        
    public Okno() {
        Container pane = this.getContentPane();
        GridBagLayout layout = new GridBagLayout();
        pane.setLayout(layout);
        
        GridBagConstraints gumbLayout = new GridBagConstraints();
        gumbLayout.gridx = 0;
        gumbLayout.gridy = 1;
        this.gumb = new JButton("Start");
        gumb.addActionListener(this);
        pane.add(this.gumb, gumbLayout);
        
        GridBagConstraints platnoLayout = new GridBagConstraints();
        platnoLayout.gridx = 0;
        platnoLayout.gridy = 0;       
        this.platno = new Platno();
        pane.add(platno, platnoLayout);
        platno.narisiKaco();  /* nariše kaco in krogec na platno ob zagonu */
        platno.narisiKrogec();
        
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent windowEvent){
               System.exit(0);
            }

        });
    }
    
    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == this.gumb) {
            System.out.println("Gumb pritisnjen");      
            platno.igraTece = true;
            
            
        }       
    }


    public static void main(String[] args) {
        JFrame okno = new Okno();
        okno.pack();
        okno.setVisible(true);
        
        
    }
    

}
