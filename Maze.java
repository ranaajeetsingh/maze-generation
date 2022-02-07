import java.io.*;
import java.util.*;

public class Maze
{
   // width and length of maze
   private int rows, cols;
   
   // 2D array of cells
   private static Cell[][] mazeList;
   
   public Maze() {
      this.rows = 5;
      this.cols = 5;
   }
   
   // constructor
   public Maze(int r, int c) {
      this.rows = r;
      this.cols = c;
      mazeList = new Cell[rows][cols];
      //mazeList[0][0].direction = "N";
      //mazeList[0][0].discover();
      /*
      for (int x = 0; x < rows; x++) {
         for (int y = 0; y < cols; y++) {
            mazeList[x][y].x = x;
            mazeList[x][y].y = y;
         }
      }
      System.out.println(mazeList[0][0]);
      */
   }
   
   public Cell getCell(int x, int y) {return mazeList[x][y];}

   public void setCell(int x, int y) {mazeList[x][y] = new Cell();}
   
   // method to return a list of possible cells to move in
   public List<Cell> getEdges(int x, int y) {
      List<Cell> cellList = new ArrayList<>();
      cellList.add(mazeList[x-1][y]);
      mazeList[x-1][y].direction = "E";
      
      cellList.add(mazeList[x+1][y]);
      mazeList[x+1][y].direction = "W";
      
      cellList.add(mazeList[x][y+1]);
      mazeList[x][y+1].direction = "N";
      
      cellList.add(mazeList[x][y+1]);
      mazeList[x][y-1].direction = "S";
      
      Collections.shuffle(cellList);
      
      return cellList;
   }
   
}

/* MAZE STRUCTURE
The maze contains a 2D array of Cells
There are certain methods to manipulate the maze an its 

*/
