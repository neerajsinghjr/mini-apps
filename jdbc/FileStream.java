package jdbc;

import java.sql.*;
import java.io.*;
import java.util.*;

public class FileStream {
   // JDBC driver name and database URL
    // static final String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";  
   static final String DB_URL = "jdbc:mysql://localhost:3306/xerus";

   //  Database credentials
   static final String USER = "root";
   static final String PASS = "fuckingInsane@9";
   
   public static void main(String[] args) {
       
       ResultSet rs = null;
       Statement stmt = null;
       PreparedStatement pstmt = null;
       Connection conn = null;
       
       try{
          // Register JDBC driver
           // Class.forName("com.mysql.cj.jdbc.Driver");

          // Open a connection
          System.out.println("Connecting to database...");
          conn = DriverManager.getConnection(DB_URL,USER,PASS);

          // Create a Statement object;
          stmt = conn.createStatement();
          // Creating table;
          createXMLTable(stmt);
           
            

          //Open a FileInputStream
          File f = new File("employee.xml");
          long fileLength = f.length();
          FileInputStream fis = new FileInputStream(f);

          //Create PreparedStatement and stream data
          String SQL = "INSERT INTO employee VALUES (?,?)";
          pstmt = conn.prepareStatement(SQL);
          pstmt.setInt(1,1);
          pstmt.setAsciiStream(2,fis,(int)fileLength);
          pstmt.execute();

          //Close input stream
          fis.close();

          // Do a query to get the row
          SQL = "SELECT emp_details FROM employee WHERE id=100";
          rs = stmt.executeQuery (SQL);
          // Get the first row
          if (rs.next ()){
             //Retrieve data from input stream
             InputStream xmlInputStream = rs.getAsciiStream (1);
             int c;
             ByteArrayOutputStream bos = new ByteArrayOutputStream();
             while (( c = xmlInputStream.read ()) != -1)
                bos.write(c);
             //Print results
             System.out.println(bos.toString());
          }
          // Clean-up environment
          rs.close();
          stmt.close();
          pstmt.close();
          conn.close();
       }catch(SQLException se){
          //Handle errors for JDBC
           System.out.println("jdbc error");
//          se.printStackTrace();
       }catch(Exception e){
          //Handle errors for Class.forName
           
          e.printStackTrace();
       }finally{
          //finally block used to close resources
          try{
             if(stmt!=null)
                stmt.close();
          }catch(SQLException se2){
          }// nothing we can do
          try{
             if(pstmt!=null)
                pstmt.close();
          }catch(SQLException se2){
          }// nothing we can do
          try{
             if(conn!=null)
                conn.close();
          }catch(SQLException se){
             se.printStackTrace();
          }//end finally try
           
       }//end try
       
       System.out.println("Goodbye!");
       
   }//end main

    
    public static void createXMLTable(Statement stmt) 
    throws SQLException {
    
       System.out.println("Creating employee table..." );
        
       //Create SQL Statement
       String sql = "CREATE TABLE employee (id INT, emp_details LONG)";
        
       
       try{
            
            //Drop table first if it exists.   
            stmt.executeUpdate("DROP TABLE XML_Data");
           
       } catch(SQLException se){
           
            System.out.println("Error: "+ se.getMessage());
 
       }
        
        stmt.executeUpdate(sql);
        
    
    }//end createXMLTable
    
}//end JDBCExample