public class Program
{
    
    static int rev(int n){
        
        int reverse = 0;
        int remainder = 0;
        while(n != 0){
            
            remainder = n%10;
            reverse = reverse*10 + remainder;
            n = n/10;
            
        }
        
        return reverse;
        
    }
    
	public static void main(String[] args) {
		
		   System.out.println(rev(123));
		
	}
}
