package mypkg;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import java.util.*;

public class HtmlFormServlet extends HttpServlet {

	@Override

	public void doGet(HttpServletRequest request, HttpServletResponse response)
	throws IOException, ServletException {
        
        // setting up the resposne content type;
        response.setContentType("text/html; charset=utf-8");
        
        // setting up the print writer;
        PrintWriter out = response.getWriter();
        
        try {
            // basic page layout;
            out.println("<html>");
            out.println("<head>");
            out.println("<meta http-equiv='Content-Type' content='text/html; charset=UTF-8'>");
            out.println("<title>HTML Form Servlet</title>");
            out.println("</head>");
            out.println("<body>");
            out.println("<H2>Survey Result...</h2>");
            
            // username validation
            String username = request.getParameter("username");
            if(username == null) {
                out.println("<p class=text-danger>Name is missing</p>");
            }else {
                out.println("<p class='text-success'>Name: " + username + "</p>");
            }
            
            // password validation;
            String password = request.getParameter("password");
            if(password == null) {
                out.println("<p class=text-danger>Password can be empty</p>");
            }else {
                out.println("<p class=text-sucess>Password: " + password + "</p>");
            }
            
            // Gender validation;
            String gender = request.getParameter("gender");
            if (gender == null) {
                out.println("<p class='text-danger'>Gender is not selected</p>");
            }else if(gender.equals('m')) {
                out.println("<p class='text-success'>Gender: Male</p>");
            } else if(gender.equals('f')) {
                out.println("<p class='text-success'>Gender: Female</p>");
            }else {
                out.println("<p class='text-success'>Gender: Other</p>");
            }
               
            // Age validation;
            String age = request.getParameter("age");
            if (gender == null) {
                out.println("<p class='text-danger'>Age is not selected</p>");
            }else {
                out.println("<p class='text-success'>Age: " + age + "</p>");
            }   
            
            // Age validation;
            String language = request.getParameter("language");
            if (gender == null) {
                out.println("<p class='text-danger'>Language is not selected</p>");
            }else {
                out.println("<p class='text-success'>Language: " + language + "</p>");
            }

            // Get null if the parameter is missing from query string;
            String instruction = request.getParameter("instruction");
            if (instruction == null /*|| (instruction = htmlFilter(instruction.trim())).length() == 0*/ ) {
                out.println("<p>Instruction is empty</p>");
            } else {
                out.println("<p>Instruction: " + instruction + "</p>");
            }
            
            // Retrieve the 'secret' hidden token;
            String secret = request.getParameter("secret");
            out.println("<p>Secret: " + secret + "</p>");
                
            // Hyperlink 'BACK' to input page
            out.println("<a href='index.html'>BACK</a>");
 
            out.println("</body></html>");
      
        } finally {
            // Always close the output writer
            out.close(); 
        }
   } // end of doGet();
    
}   // end of HtmlFormServlet();