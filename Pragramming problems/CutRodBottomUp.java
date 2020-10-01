import java.io.*;
import java.util.Scanner;
class RodCut{
    int memoized_cut_rod(int[] p,int n){
        int r[]= new int[n+1];
        for (int i=0;i<=n;i++){
            r[i]=-11111;
        }
        return memoized_cut_rod_aux(p,n,r);
    }

    int memoized_cut_rod_aux(int[] p,int n,int[] r){
        int q=0;
        if(r[n]>=0)
            return r[n];
        if(n==0)
            q=0;
        else{
            q=-1;
        }
        for(int i=1;i<=n;i++){
            q= max(q,p[i]+memoized_cut_rod_aux(p, n-i, r));
            r[n]=q;
            
        }
        return q;

    }
    int max(int a,int b){
        if(a>b){
            return a;
        }
        else{
            return b;
        }
    }

}
class uk{
    public static void main(String args[]){
    Scanner sc= new Scanner(System.in);
    int n=sc.nextInt();
    int p[]= {0,1,5,8,9,10,17,17,20,24,30};

    /*int p[]= new int[n+1];
    for(int i=0;i<n;i++){
        p[i]= sc.nextInt();
    }*/

RodCut r = new RodCut();
System.out.println(r.memoized_cut_rod(p,n));
}
}
