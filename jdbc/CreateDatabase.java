/*
 *   Creating database using the jdbc;
 */


package jdbc;

import java.sql.*;
import java.io.*;
import java.util.*;

public class CreateDatabase {
    
    // Database credentials;
    static final String DB_DRIVER = "com.mysql.cj.jdbc.driver";
    static final String DB_URL = "jdbc:mqsql://localhost/";
    static final String USER = "root";
    static final String PASS = "fuckingInsane@9";
    
    public void main (String args[]) {
        
        // Required Credentials;
        Statement stmt = null;
        Connection connect = null;
        
        try {
            
            // Register jdbc driver;
//            Class.forName('com.mysql.cj.jdbc.Driver');
            
            // Connecting to database;
            System.out.println("Connecting to the Database ...");
            connect = DriverManager.getConnection(DB_URL, USER, PASS);
            
            // Creating database;
            System.out.println("Creating Database JDBC...");
            stmt = connect.createStatement();
            String sql = "create database jdbc;";
            stmt.executeQuery(sql);
            System.out.println("Database Created Successfully ...");
            
        } catch (SQLException se) {
            
            se.printStackTrace();
            
        } catch (Exception e) {
            
            e.printStackTrace();
            
        } finally {
            
            try {
                
                if (stmt != null)
                    stmt.close();
                
            } catch(SQLException se) {
                
                System.out.print("Connection Problem");
                
            } 
            
            try {
                
                if (connect != null)
                    connect.close();
                
            } catch(SQLException se) {
                
                System.out.print("Connection Problem");
                
            }
        }
        
        
    } // end of main()
    
} // end of CreateDatabase{}