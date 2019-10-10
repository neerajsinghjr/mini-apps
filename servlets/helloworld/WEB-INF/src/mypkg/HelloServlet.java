package mypkg;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class HelloServlet extends HttpServlet {

	@Override
	public void doGet(HttpServletRequest request, HttpServletResponse response) 
	throws IOException, ServletException {
		// response type
		response.setContentType("text/html; charset=utf-8");
                // setting up output functionality
		PrintWriter out = response.getWriter();

		// output content declaration
		try {
			out.println("<!DOCTYPE html>");
                        out.println("<html>");
                        out.println("<head>");
                        out.println("<title>Hello World, Servlet</title>");
                        out.println("<body>");
                        out.println("<h1>Hello World, Mr.devil</h1>");
			
			// Getting Client Details
                        out.println("<p>Request URI: "+ request.getRequestURI() +"</p>");
                        out.println("<p>Protocol: "+request.getProtocol() + "</p>");
                        out.println("<p>Remote Address: "+ request.getRemoteAddr() + "</p>");
                        out.println("<p>Path Info: "+ request.getPathInfo() +"</p>");

			// Random Number Generation
                        out.println("<p>Random Number: "+ Math.random() +"</p>");
                        out.println("</body>");
                        out.println("</html>");
		} finally {
			out.close();
		}
	}

}






