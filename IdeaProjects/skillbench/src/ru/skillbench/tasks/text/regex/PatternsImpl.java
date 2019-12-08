package ru.skillbench.tasks.text.regex;

import java.util.ArrayList;
import java.util.regex.Pattern;
import java.util.List;
import java.util.regex.Matcher;


public class PatternsImpl implements Patterns {
    @Override
    public Pattern getSQLIdentifierPattern() {
        Pattern pattern = Pattern.compile("[A-Za-z][\\w]{0,29}");
        return pattern;
    }

    @Override
    public Pattern getEmailPattern() {
        Pattern pattern = Pattern.compile("[A-Za-z0-9][\\w.-]{0,20}[A-Za-z0-9]?" + "@" + "([A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])+[.])+" + "(ru|com|net|org)");
        return pattern;
    }

    @Override
    public Pattern getHrefTagPattern() {
        Pattern pattern = Pattern.compile("<(a|A)(\\s)*([Hh][Rr][Ee][Ff])(\\s)*="+"(\\s)*(([\\w@.#/\\\\]+)|(\"([\\s\\w.@#])*\"))(\\s)*>");
        return pattern;
    }

    @Override
    public List<String> findAll(String input, Pattern pattern) {
        List<String> list = new ArrayList<String>();
        Pattern p = Pattern.compile(pattern.toString());
        Matcher m = p.matcher(input);
        while (m.find()) {
            list.add(m.group());
        }
        return list;
    }

    @Override
    public int countMatches(String input, String regex) {
        int i=0;
        Pattern p = Pattern.compile(regex);
        Matcher m = p.matcher(input);
        while (m.find()) {
            i++;
        }
        return i;
    }
}
