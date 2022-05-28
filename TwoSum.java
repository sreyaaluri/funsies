import java.util.HashMap;
import java.util.Map;

class TwoSum {
  public static void main(String[] args) {
      int[] nums = {3,0,2,4};
      int target = 7;
      int[] ans = twoSum(nums,target);
      System.out.format("[%d,%d]%n", ans[0], ans[1]);
  }

  public static int[] twoSum(int[] nums, int target) {
    HashMap<Integer, Integer> map = new HashMap<>();
    for(int i = 0; i < nums.length; i++){
        int betterHalf = target-nums[i];
        if(map.containsKey(betterHalf)){
          // for(Map.Entry<Integer, Integer> e: map.entrySet()){
          //   System.out.println("key: "+e.getKey()+", value: "+e.getValue());
          // }
            return new int[]{i, map.get(betterHalf)};
        }
        map.put(nums[i], i);
    }
    // for(Map.Entry<Integer, Integer> e: map.entrySet()){
    //   System.out.println("key: "+e.getKey()+", value: "+e.getValue());
    // }
    return null;
}
}

// Note:
// The HashMap DOESN't contain dupicate keys - it can.
// It replaces the val with new val. 
// This works because you check before replace.
// It worked in 2 diff for loops because I'm taking curr element 
//   to compute "betterHalf" from nums and not from map
// So the replaced values will be in nums and their SINGULAR counterpart 
//   will be the one in maps