public class MergeSortedArray {

  public static void merge(int[] nums1, int m, int[] nums2, int n) {
    // brute force is to insert and bubble
    // Below sol: O(m+n) time; O(m+n) space
    int[] merged = new int[m+n];
    int i = 0, j = 0, k = 0;
    
    while(i < m && j < n) {
        if(nums1[i] <= nums2[j]){
            merged[k] = nums1[i];
            i++;
        }
        else {
            merged[k] = nums2[j];
            j++;
        }
        k++;
    }
    
    // adding on tails
    for(; i < m; i++) { // nums2 has been processed, nums1 remaining
        merged[k] = nums1[i];
        k++;
    }
    for(; j < n; j++) { // nums1 has been processed, nums2 remaining
        merged[k] = nums2[j];
        k++;
    }
    
    // copying
    for(i = 0; i < m+n; i++)
      nums1[i] = merged[i];

    // printing nums1
    System.out.print("[ ");
    for(i = 0; i<nums1.length; i++)
      System.out.print(nums1[i]+", ");
    System.out.print("]");

  }

  public static void optimalMerge(int[] nums1, int m, int[] nums2, int n) {
    int i = m-1, j = n-1;

    for(int k = m+n-1; k >= 0; k--){
      if(j < 0) break;
      if(i >= 0 && nums1[i] > nums2[j])
        nums1[k] = nums1[i--]; // NOTE: "use then change" syntax used well!
      else
        nums1[k] = nums2[j--];
    }

    // printing nums1
    System.out.print("[ ");
    for(i = 0; i<nums1.length; i++)
      System.out.print(nums1[i]+", ");
    System.out.print("]");
  }

  public static void main(String[] args) {
    int[] nums1 = new int[]{4,5,6,0,0,0};
    int[] nums2 = new int[]{1,2,3};
    int m = 3;
    int n = 3;
    optimalMerge(nums1, m, nums2, n);
  }
}

// Note:
// best sol: *back to front*, not extra space used.
// for above sol, think like a machine: 
//  the "adding tails" part can be omitted if I made a copy of nums1 and directly overwrote nums1 itself
// for best sol break condition logic:
//  if j done before i, no changes need to be made as nums1 is already sorted
//  if i done before j, else condition is processed everytime