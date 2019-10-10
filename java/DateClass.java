package SexyGirls;

import java.util.*;
import java.text.*;

public class DateClass {

   public static void main(String args[]) {
      // Date() class
      Date date = new Date();

      // SimpleDateFormat() class 
      SimpleDateFormat x = new SimpleDateFormat("E yyyy.MM.dd 'at' hh:mm:ss a zzz");

      // Display time and date using toString()
      System.out.println(date.toString());
      System.out.println(x.format(date));
   }
}
