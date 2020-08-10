import java.util.Scanner;

class KeltaMath{
    
    static double square_root(double n){
        
        //Here I will use newton's method to calculate square root
        
        double x = n;
        double l = 0.000001; //tolerance
        double root;
        
        while(true){
            root = 0.5*(x + (n/x));
            if(Math.abs(root - x) <= l){
                break;
            }
            else{
                x = root;
            }
        }
        
        return root;
        
    }
    
}

public class Main{
    
	public static void main(String[] args) {
	    
	    KeltaMath m = new KeltaMath();
	    Scanner s = new Scanner(System.in);
	    System.out.println("Enter the number for square root");
	    int x = s.nextInt();
	    double y = KeltaMath.square_root(x);
	    System.out.println("Square root of "+x+" is "+y);
	    
	}
	
}
