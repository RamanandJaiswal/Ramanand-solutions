 

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
/*
Chandan is an extremely biased person, and he dislikes people who fail to solve all the problems in the interview he takes for hiring people. There are n people on a day who came to be interviewed by Chandan.
Chandan rates every candidate from 0 to 10. He has to output the total ratings of all the people who came in a day. But, here's the problem: Chandan gets extremely frustrated when someone ends up scoring a 0 in the interview. So in frustration he ends up removing the candidate who scored that 0, and also removes the candidate who came before him. If there is no candidate before the one who scores a 0, he does nothing.
You've to find the summation of all the ratings in a day for Chandan.
Example :input
5 2 3 0 7 0
output : 2
/
public class BiasedChandan {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
      Scanner sc=new Scanner(System.in);
      List l=new ArrayList();
      int n=sc.nextInt();
      int v;
      int a[]=new int[n];
      for(int i=0;i<n;i++){
    	  v=sc.nextInt();
    	  if(v==0)
    		  l.remove(l.size()-1);
    	  else
    		  l.add(v);
      }
      int sum=0;
      for(int i=0;i<l.size();i++){
    	  
    		 sum=sum+(int)l.get(i);
    	 
      }
       
      System.out.println(sum);
	}

}
