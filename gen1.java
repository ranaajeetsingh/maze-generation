import java.util.*;
import java.io.*;

public class gen1 {
   
    // HashMap for directions
    private HashMap<String, Integer> directions = new HashMap<String, Integer>();
   
    // non constant list for each direction
    private List<String> intList = new ArrayList<String>();
   
    // mashmaps for more directions
    private HashMap<String, Integer> DX = new HashMap<String, Integer>();
    private HashMap<String, Integer> DY = new HashMap<String, Integer>();
    private HashMap<String, Integer> OPPOSITE = new HashMap<String, Integer>();
   
    // default constructor
    public gen1() {
        setup();
    }
   
    // recursive backtracking algorithm
    public void carve(int cx, int cy, int[][] grid) {
        // shuffle the list of directions
        Collections.shuffle(intList);
        // for each possbile direction
        for (String direction : intList) {
            // declare the new x and y variables
            int nx = cx + DX.get(direction);
            int ny = cy + DY.get(direction);
            // if nx and ny are valid and not visited previously
            if (0 <= ny && ny < grid.length && 0 <= nx && nx < grid[ny].length && grid[ny][nx] == 0) {
                grid[cy][cx] |= directions.get(direction);
                grid[ny][nx] |= OPPOSITE.get(direction);
                carve(nx, ny, grid);
            }
        }
    }
    
    // method to display all values of grid
    public void display(int[][] grid) {
        for (int x = 0; x < grid.length; x++) {
            for (int y = 0; y < grid[x].length; y++) {
                System.out.print(grid[y][x] + " ");
            }
            System.out.println();
        }
    }
   
    // method to set up private variables
    public void setup() {
        // set up directions
        directions.put("E", 4);
        directions.put("W", 8);
        directions.put("N", 2);
        directions.put("S", 1);
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
        // set up intList
        intList.add("N");
        intList.add("S");
        intList.add("E");
        intList.add("W");
        // set up OPPOSITE
        OPPOSITE.put("E", 8);
        OPPOSITE.put("W", 4);
        OPPOSITE.put("N", 2);
        OPPOSITE.put("S", 1);
    }
}

/* confusion :(
 * hmmm the direction numbers are confusing. The grid starts out as empty
   and the method fills it in runtime
 * The grid is filled with directions, specifically integers.
 * Link to what I am shamelessly copying: https://www.onlinegdb.com/online_java_compiler#
 
*/
