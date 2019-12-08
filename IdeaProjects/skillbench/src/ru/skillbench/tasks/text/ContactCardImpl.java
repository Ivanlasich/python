package ru.skillbench.tasks.text;

import java.io.File;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.Period;
import java.time.ZoneId;
import java.util.*;

public class ContactCardImpl  implements ContactCard {
//    System.setProperty("console.encoding","utf-8");
    private String FN;
    private String ORG;
    private String GENDER;
    private String BDAY;
    private Collection TEL;
    private Collection TYPE;

    public ContactCardImpl(){
        this.FN = null;
        this.ORG = null;
        this.GENDER = null;
        this.BDAY = null;
        this.TEL  = new ArrayList();
        this.TYPE  = new ArrayList();
    }

    @Override
    public ContactCard getInstance(Scanner scanner) {



         String s;

         String str[];
         int i = 0;
         Collection collection = new ArrayList();

         while (scanner.hasNext()) {
             collection.add(scanner.nextLine());
             i++;

         }
         Iterator iterator = collection.iterator();
         str = new String[i];
         i = 0;
         while (iterator.hasNext()) {
             s = iterator.next().toString();
             str[i] = s;
             i++;
         }

         if (!str[0].equals("BEGIN:VCARD")) {
             throw new NoSuchElementException();
         }
         if (!str[str.length - 1].equals("END:VCARD")) {
             throw new NoSuchElementException();
         }
         if (!str[1].startsWith("FN:")) {
             System.out.println(str[1]);
             throw new NoSuchElementException();
         }
         if (!str[2].startsWith("ORG:")) {
             throw new NoSuchElementException();
         }


         for (i = 1; i < str.length - 1; i++) {

             if (str[i].startsWith("FN:")) {
                 this.FN = str[i].substring(str[i].indexOf(":") + 1);
                 continue;
             }
             if (str[i].startsWith("ORG:")) {
                 this.ORG = str[i].substring(str[i].indexOf(":") + 1);
                 continue;
             }
             if (str[i].startsWith("GENDER:")) {
                 this.GENDER = str[i].substring(str[i].indexOf(":") + 1);
                 continue;
             }
             if (str[i].startsWith("BDAY:")) {

                 this.BDAY = str[i].substring(str[i].indexOf(":") + 1);
                 if (!this.BDAY.matches("\\d{2}-\\d{2}-\\d{4}")) {
                     throw new InputMismatchException();
                 }
                 continue;
             }
             if (str[i].startsWith("TEL;")) {
                 try {
                     String a;
                     a = str[i].substring(str[i].indexOf(";") + 1);
                     if (!a.startsWith("TYPE")) {
                         throw new InputMismatchException();
                     }

                     this.TYPE.add(str[i].substring(str[i].indexOf("=") + 1, str[i].indexOf(":")));
                     String b;
                     b = str[i].substring(str[i].indexOf(":") + 1);
                     if (b.length() != 10) {
                         throw new InputMismatchException();
                     }
                     if (!b.matches("\\d{10}")) {
                         throw new InputMismatchException();
                     }
                     this.TEL.add(b);
                     continue;
                 } catch (InputMismatchException e) {
                     throw new InputMismatchException();
                 }
             }
             throw new InputMismatchException();
         }

        return this;
    }

    @Override
    public ContactCard getInstance(String data) {
        Scanner scan = new Scanner(data);
        return getInstance(scan);
    }

    @Override
    public String getFullName() {
        return this.FN;
    }

    @Override
    public String getOrganization() {
        return this.ORG;
    }

    @Override
    public boolean isWoman() {
        if(this.GENDER.equals("F")){
            return true;
        }
        if(this.GENDER.equals("M")){
            return false;
        }
        throw new InputMismatchException();

    }

    @Override
    public Calendar getBirthday()  {
        if(this.BDAY==null){
            throw new NoSuchElementException();
        }
        if (!this.BDAY.matches("\\d{2}-\\d{2}-\\d{4}")) {
            throw new InputMismatchException();
        }
        String[] c;
        c = this.BDAY.split("-");
        Calendar calendar = new GregorianCalendar(Integer.valueOf(c[2]), Integer.valueOf(c[1]) -1, Integer.valueOf(c[0]));

        return calendar;
    }

    @Override
    public Period getAge()  {
        if(this.BDAY==null){
            throw new NoSuchElementException();
        }
        if (!this.BDAY.matches("\\d{2}-\\d{2}-\\d{4}")) {
            throw new InputMismatchException();
        }
        String str[];
        str = this.BDAY.split("-");
        Period period = Period.of(Integer.valueOf(str[2]),Integer.valueOf(str[1]) , Integer.valueOf(str[0]));
        return period;
    }

    @Override
    public int getAgeYears() {
        if(this.BDAY==null){
            throw new NoSuchElementException();
        }
        if (!this.BDAY.matches("\\d{2}-\\d{2}-\\d{4}")) {
            throw new InputMismatchException();
        }
        String str[];
        str = this.BDAY.split("-");
        Date date = new Date();
        LocalDate localDate = date.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
        int dat, month, year;
        dat = localDate.getDayOfMonth();
        month = localDate.getMonthValue();
        year = localDate.getYear();
        if(Integer.valueOf(str[1]) < month){

            return year - Integer.valueOf(str[2]);
        }

        if(month == Integer.valueOf(str[1]) &  Integer.valueOf(str[0]) <= dat ){
            return year - Integer.valueOf(str[2]);
        }

        return year - Integer.valueOf(str[2])-1;
    }

    @Override
    public String getPhone(String type) {
        int i=0;
        String s, c;
        if(this.TYPE==null){
            throw new NoSuchElementException();
        }
        Iterator iterator1 = this.TYPE.iterator();
        Iterator iterator2 = this.TEL.iterator();
        while (iterator1.hasNext()){
            s = iterator1.next().toString();

            c = iterator2.next().toString();
            if(s.equals(type)){
                i++;
                return "("+c.substring(0,3)+")"+" "+c.substring(3,6)+"-"+c.substring(6);
            }
        }

        if(i==0){
            throw new NoSuchElementException();
        }
        return null;
    }
}
