package ru.skillbench.tasks.text.regex;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class CurriculumVitaeImpl implements CurriculumVitae {

    private String text;
    public static final String FULL_NAME_PATTERN = "([A-Z][a-z]+\\.?\\s?){2,3}";
    public static final String NAME_PATTERN = "(\\w+\\.?)\\s(\\w+\\.?)\\s?(\\w+\\.?)?";
    private List<Phone> phones;
    private  List<String> hid = new ArrayList<>();
    private String fullName;
    private String firstName;
    private String middleName;
    private String lastName;




    public CurriculumVitaeImpl(){
        this.text = null;
        this.phones = null;
        this.fullName = null;
        this.firstName = null;
        this.middleName = null;
        this.lastName = null;
        this.hid = null;
    }

    @Override
    public void setText(String text) {
        this.text = text;
    }

    @Override
    public String getText() {
        if (text == null) {
            throw new IllegalStateException();
        }
        return this.text;
    }

    @Override
    public List<Phone> getPhones() throws IllegalStateException{

        phones = new ArrayList<>();
        Pattern p = Pattern.compile(PHONE_PATTERN);
        Matcher m = p.matcher(getText());
        while (m.find()) {
            int aCode = -1;
            int ext = -1;
            if (m.group(2) != null) {
                aCode = Integer.parseInt(m.group(2));
            }
            if (m.group(7) != null) {
                ext = Integer.parseInt(m.group(7));
            }
            Phone phone = new Phone(m.group(), aCode, ext);
            phones.add(phone);
        }
        return phones;
    }

    @Override
    public String getFullName() {
        Pattern p = Pattern.compile(FULL_NAME_PATTERN);
        Matcher m = p.matcher(getText());
        String s;
        if(m.find()){
            s = m.group();
        }
        else {
            throw new NoSuchElementException();
        }
        this.fullName = s;
        String str[] = new String[3];
        str = s.split(" ");
        if (str.length==2){
                this.firstName = str[0];
                this.middleName = null;
                this.lastName = str[1];
                return s;
            }
        this.firstName=str[0];
        this.middleName=str[1];
        this.lastName=str[2];

        return this.fullName;
    }

    @Override
    public String getFirstName() {
        getFullName();

        return this.firstName;
    }

    @Override
    public String getMiddleName() {
        getFullName();
        return this.middleName;
    }

    @Override
    public String getLastName() {
        getFullName();
        return this.lastName;
    }

    @Override
    public void updateLastName(String newLastName) {
        String s;
        if (this.middleName!=null){
            s = this.firstName+' '+this.middleName+' '+newLastName;
        }
        else {
            s = this.firstName +' '+newLastName;
        }

        setText(getText().replaceAll(getFullName(),s));
    }

    @Override
    public void updatePhone(Phone oldPhone, Phone newPhone) {
        Pattern p = Pattern.compile(PHONE_PATTERN);
        Matcher m = p.matcher(getText());
        int i=0;
        while (m.find()) {
            if (m.group().equals(oldPhone.getNumber())){
                setText(getText().replaceAll(oldPhone.getNumber(), newPhone.getNumber()));
                i++;
            }
        }
        if(i==0){
            throw new IllegalArgumentException();
        }

    }

    @Override
    public void hide(String piece) {


        String s;
        s = piece.replaceAll("[^ .@]","X");

        if(getText().lastIndexOf(piece)==-1){
            throw new IllegalArgumentException();
        }
        setText(getText().replaceAll(piece, s));
        if(this.hid==null){
            this.hid =new ArrayList<>();
        }
        this.hid.add(piece);
    }

    @Override
    public void hidePhone(String phone) {
        String s;
        s = phone.replaceAll("[\\d]","X");
        if(getText().lastIndexOf(phone)==-1){
            throw new IllegalArgumentException();
        }
        setText(getText().replaceAll(phone, s));
        if(this.hid==null){
            this.hid =new ArrayList<>();
        }
        hid.add(phone);
    }


    @Override
    public int unhideAll() {
        Pattern p = Pattern.compile(PHONE_PATTERN);
        Matcher m;
        String s, c;
        int i;
        for (i = 0; i < this.hid.size(); i++) {
            s = this.hid.get(i);
            m = p.matcher(s);
            if (m.find()){
                c = s.replaceAll("[\\d]","X");
                setText(getText().replaceAll(c, s));
            }
            else {
                c = s.replaceAll("[^ .@]","X");
                setText(getText().replaceAll(c, s));
            }
        }
        return i;
    }
}
