import java.io.*;
import java.util.*;

public class Cell
{
   // hastable for edges
   public Map<String, Boolean> edges = new HashMap<>();
   
   // hashtable for opposite edges
   public Map<String, String> opposites = new HashMap<>();
   
   // boolean to check if the cell has been visited
   public boolean visited;
   
   public int x, y;
   
   // direction the cell came from
   public String direction = "O";
   
   // constructor
   public Cell() {
      // set up hash maps
      setEdges();
      setOpposites();
   }
   
   public void discover() {
      visited = true;
   }
   
   // method to discover edge
   public void discoverCell(Cell original) {
      edges.replace(opposites.get(direction), false);
      visited = true;
      original.edges.replace(direction, false);
   }
   
   // method to set edges
   private void setEdges() {
      edges.put("N", true);
      edges.put("E", true);
      edges.put("S", true);
      edges.put("W", true);
   }
   
   // method to set opposites
   private void setOpposites() {
      opposites.put("N", "S");
      opposites.put("S", "N");
      opposites.put("E", "W");
      opposites.put("W", "E");
   }
}

/* CELL STRUCTURE
The structre of each cell represents a node with four edges, or walls.
The cell contains it's own hashtable(String, boolean) for each edge.
There are also methods to get the opposite edge given one.
Other methods will come as I write out the code.
The cell will also have an attribute to mark if they have been visited
*/
