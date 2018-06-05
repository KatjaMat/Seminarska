import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.KeyEventDispatcher;
import java.awt.KeyboardFocusManager;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class Okno extends JFrame implements ActionListener {
    private Platno platno;
    private JButton gumb;
    public static boolean levo = false;
    public static boolean desno = true;
    public static boolean gor = false;
    public static boolean dol = false;
        
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
        
        
        KeyboardFocusManager.getCurrentKeyboardFocusManager()
        .addKeyEventDispatcher(new KeyEventDispatcher() {
            @Override            
            public boolean dispatchKeyEvent(KeyEvent e) {
            	int keyCode = e.getKeyCode();
            	switch (keyCode) {
            		case KeyEvent.VK_LEFT:
            			levo = true;
            			desno = false;
            			gor = false;
            			dol = false;
            			break;
            		case KeyEvent.VK_RIGHT:
            			levo = false;
            			desno = true;
            			gor = false;
            			dol = false;
            			break;
            		case KeyEvent.VK_UP:
            			levo = false;
            			desno = false;
            			gor = true;
            			dol = false;
            			break;
            		case KeyEvent.VK_DOWN:
            			levo = false;
            			desno = false;
            			gor = false;
            			dol = true;
            			break;
            	}
              return false;
            }
      });
        
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent windowEvent){
               System.exit(0);
            }

        });
    }
    
    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == this.gumb) {     
            platno.igraTece = true;
            
            
        }       
    }
    
    public static void main(String[] args) {
        JFrame okno = new Okno();
        okno.pack();
        okno.setVisible(true);
        
        
    }

}
