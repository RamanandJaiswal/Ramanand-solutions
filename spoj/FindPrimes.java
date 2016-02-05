
import java.util.*;
import java.lang.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
/*find all prime number between two numbers*/
class FindPrimes1
{
  	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 Scanner sc=new Scanner(System.in);
		 long T=sc.nextInt();
		 for(long t=0;t<T;t++){
			 int n1=sc.nextInt();
			 int n2=sc.nextInt();
			  
			  
			 
			 runEratosthenesSieve(n1,n2);
		 }
	}
  	
  	public static void runEratosthenesSieve(int low,int upperBound) {
        int upperBoundSquareRoot = (int) Math.sqrt(upperBound);
        boolean[] isComposite = new boolean[upperBound + 1];
        for (int m = 2; m <= upperBoundSquareRoot; m++) {
              if (!isComposite[m]) {
            	  if(m>=low)
                    System.out.print(m + " ");
                    for (int k = m * m; k <= upperBound; k += m)
                          isComposite[k] = true;
              }
        }
        for (int m = upperBoundSquareRoot; m <= upperBound; m++)
              if (!isComposite[m] && m>=low)
                    System.out.print(m + " ");
  }
 

  
}
