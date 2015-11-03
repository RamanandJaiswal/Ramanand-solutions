import java.util.Hashtable;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class PrimeString {
public static int  checkPrime(int num){
	int flag=0;
	if(num==1)
	 flag=1;
	else if(num==2)
		flag=0;
	else{
		for(int i=2;i<=num/2;i++){
			if(num%i==0)
				flag=1;
			else
				continue;
		}
	}
	return flag; 
}
	public static void main(String[] args) {
	 
	Scanner sc=new Scanner(System.in);
	int T=sc.nextInt();
	for(int t=0;t<T;t++){
	String s=sc.next();
    
    char s1[]=s.toCharArray();
    Hashtable h=new Hashtable();
    int count=0;
    for(char c :s1){
    	count=1;
    	if(h.containsKey(c)){
    		h.put(c, ++count); 
    	}
    	else
    	{
    		h.put(c, count);
    	}
    
    }
    int c=0;
    int size=(int)h.size();
   
    int res=PrimeString.checkPrime(size);
    
    if(res==0){
    int temp=0;
    Set set = h.entrySet();
    Iterator it = set.iterator();
    while (it.hasNext()) {
      Map.Entry entry = (Map.Entry) it.next();
      int value=(int)entry.getValue();
      int result=PrimeString.checkPrime(value);
      if(result==1){
    	  temp=1;
    	  break;
    	  }
      else
    	  temp=0;
       
    	 
       
    }
    if(temp==0) 
    	System.out.println("YES");
    else
    	System.out.println("NO");
     
    }
    else{
    	System.out.println("NO");
    }
}
	}

}
