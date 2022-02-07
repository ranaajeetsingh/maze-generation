import java.util.*;
import java.io.*;

public class Main
{
   
	public static void main(String[] args) {
	   System.out.println("did it work");
	   int x = 3;
	   Maze test = new Maze(5, 5);
	   test.setCell(0, 0);
	   test.getCell(0, 0).discover();
		//Maze mazeObj = new Maze(5, 5);
		//DFS(mazeObj, mazeObj.getCell(0, 0));
		System.out.println("yes");
	}
	
	private static void DFS(Maze G, Cell v) {
	   List<Cell> cells = new ArrayList<>();
	   cells = G.getEdges(v.x, v.y);
	   Cell W = cells.get(0);
	   cells.remove(0);
	   
	}
}
