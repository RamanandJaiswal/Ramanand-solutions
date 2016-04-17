 

import java.util.Scanner;

public class PairWithKthDifference {
	
	//sorting
	void quicksort(long a[],int l,int r){
		if(l<r)
		{ 
		int pos=partition(a, l, r);
		quicksort(a,l,pos-1);
		quicksort(a,pos+1,r);
		}
	}
	int partition(long[] a, int l, int r) {
		 long pivot=a[r];
		 int pindex=l;
		 long temp;
		 for(int i=l;i<=r-1;i++){
			 if(a[i]<=pivot){  //check if element is smaller than pivot element
				 temp=a[pindex];
				 a[pindex]=a[i];
				 a[i]=temp;
				 pindex++;
				}
		 }
		 //swap pivot with element with partitioned element
		 temp=a[pindex];
		 a[pindex]=a[r];
		 a[r]=temp;
		return pindex;
	}
    public static int findPair(long a[],int k){
    	int n=a.length,count=0;			
    	for(int i=0;i<n;i++){
        	for(int j=i;j<n;j++){
        		if(Math.abs(a[i]-a[j])==k){
        			count++;
        		}
        	}
        }
    	return count;
    }
    //Binary search
    int binarySearch(long a[],int beg,int end,long element){
    	if(beg<=end){
    		int middle=(beg+end)/2;
    		if(a[middle]==element)
    			return middle;
    		if(element >a[middle])
    			return binarySearch(a,middle+1,end,element);
    		else
    			return binarySearch(a,beg,middle-1,element);
    	}
		return 0;
    }
  
     
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*5 2  
		1 5 3 4 2 */
	Scanner sc=new Scanner(System.in);
	int n=sc.nextInt();
	int k=sc.nextInt();
	int  count=0;
	long a[]=new long[n];
	for(int i=0;i<n;i++)
       a[i]=sc.nextLong();
     
    PairWithKthDifference pwk=new PairWithKthDifference();
    pwk.quicksort(a, 0, n-1);
    
    for(int i=0;i<a.length;i++){
    	 
    	 if(pwk.binarySearch(a,i+1, n-1,a[i]+k)!=0){
    		 count++;
    	 }
    	
    }
    // complexity(O(NLogN))
    System.out.println("Count : "+count);
    // complexity(O(N^2))
    System.out.println(findPair(a,k));
    
   
	}

}
