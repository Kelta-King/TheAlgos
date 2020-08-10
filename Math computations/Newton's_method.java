
/*

Here is the explanation of the code...
there are 2 things required. Input number and tolerance value.

In newton's method, if we want to find the square root of a number n then we can find the square root of that number bt 0.5(x + (n/x))
Here x is assumed square root and root is proper square root.

Now in a while loop find the root and if their difference is less than or equal to the the tolerance then that root will be answer. 
Else that root will be new assumed root.

*/

import java.util.Scanner;

class KeltaMath{
    
    static double square_root(double n){
        
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
