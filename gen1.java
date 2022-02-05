import java.util.*;
import java.io.*;

public class gen1 {
   
   // width and height of maze
   private int width, height;
   
   // integer array for grid
   private int[][] grid = new int[width][height];
   
   // constants for directions
   private final int N = 1;
   private final int S = 2;
   private final int E = 4;
   private final int W = 8;
   
   // mashmaps for more directions
   private Map<String, Integer> DX = new HashMap<>();
   private Map<String, Integer> DY = new HashMap<>();
   private Map<String, String> OPPOSITE = new HashMap<>();
   
   
   // default constructor
   public gen1() {
      // set up width and height
      width = 10;
      height = 10;
      // set up DX
      DX.put("E", 1);
      DX.put("W", -1);
      DX.put("N", 0);
      DX.put("S", 0);
      // set up DY
      DY.put("E", 0);
      DY.put("W", 0);
      DY.put("N", -1);
      DY.put("S", 1);
      // set up OPPOSITE
      OPPOSITE.put("E", "W");
      OPPOSITE.put("W", "E");
      OPPOSITE.put("N", "S");
      OPPOSITE.put("S", "N");
   }
   
   // recursive backtracking algorithm
   private void carve(int cx, int cy) {
      
   }
}

/* confusion :(
 * hmmm the direction numbers are confusing. The grid starts out as empty
   and the method fills it in runtime
 * The grid is filled with directions, specifically integers.
 * Link to what I am shamelessly copying: https://www.onlinegdb.com/online_java_compiler#
 
*/
