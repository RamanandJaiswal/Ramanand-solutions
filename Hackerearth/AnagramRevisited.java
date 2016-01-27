import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Scanner;
import java.util.Map.Entry;
/*Arnab is a robber and he has managed to rob N different strings from Akash. 
Now he decides to sell these strings in the market to make some profit. 
But, of all the strings he has, he wants to find the size of the largest anagram group 
so that he can easily sell that one first and make maximum profit initially. 
Help him find the largest size of groups of anagrams.
An anagram of a string is another string that contains same characters, only the order of characters can be different. 
For example, “abcd” and “dabc” are anagram of each other.*/
public class AnagramRevisited {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		 int n=sc.nextInt();
		 String a[]=new String[n];
		 for(int i=0;i<n;i++){
			 a[i]=sc.next();
		 }
		int count=0;
		Hashtable<String,Integer> ht=new Hashtable<String,Integer>();
       for(int i=0;i<n;i++){
    	   count=1;
    	   char[] chars = a[i].toCharArray(); 
    	   Arrays.sort(chars);
    	   //System.out.println(chars);
    	   if(ht.get(String.valueOf(chars))!=null){
    		   count=1+ht.get(String.valueOf(chars)).intValue();
    		   ht.put(String.valueOf(chars),count);
    	   }
    	   else{
    		   ht.put(String.valueOf(chars),count);
    	   }
       }
       for (Entry<String, Integer> entry : ht.entrySet()) {
    	   System.out.println(entry.getKey()+":"+entry.getValue());
       }
       
       int maxValueInMap=(Collections.max(ht.values())); 
       System.out.println("Anagram group with maximum group"+maxValueInMap);
        
	}

}
