package ru.skillbench.tasks.javaapi.collections;

import java.util.*;

public class StringFilterImpl implements StringFilter {


    private interface Filter {
        boolean check(String string, String pattern);
    }

    private Iterator<String> filters(String chars, Filter filter){
        if (chars == null || chars.equals("")) {
            return this.list.iterator();
        }
        String example = chars.toLowerCase();
        ArrayList<String> ans = new ArrayList<>();
        for (String s : this.list) {
            if (filter.check(s, example)) {
                ans.add(s);
            }
        }
        return ans.iterator();
    }

    private HashSet<String> list;

    public StringFilterImpl(){
        this.list = new HashSet<>();
    }

    @Override
    public void add(String s) {
        if (s == null){
            this.list.add(null);
        }
        else {
            this.list.add(s.toLowerCase());
        }
    }

    @Override
    public boolean remove(String s) {
        if (s == null){
           return this.list.remove(null);
        }
        return this.list.remove(s.toLowerCase());
    }

    @Override
    public void removeAll() {
        this.list.clear();
    }

    @Override
    public Collection<String> getCollection() {
        return this.list;
    }

    @Override
    public Iterator<String> getStringsContaining(String chars) {
        Filter filter = new Filter() {
            @Override
            public boolean check(String string, String pattern) {
                if(string != null && string.contains(pattern)){
                    return true;
                }
                else {
                    return false;
                }
            }
        };
        return filters(chars, filter);
    }

    @Override
    public Iterator<String> getStringsStartingWith(String begin) {
        Filter filter = new Filter() {
            @Override
            public boolean check(String string, String pattern) {
                if(string != null && string.startsWith(pattern)){
                    return true;
                }
                else {
                    return false;
                }
            }
        };
        return filters(begin, filter);
    }

    @Override
    public Iterator<String> getStringsByNumberFormat(String format) {
        Filter filter = new Filter() {
            @Override
            public boolean check(String string, String pattern) {
                if (string == null || string.length() != pattern.length()) {
                    return false;
                }
                for (int i = 0; i < string.length(); i++){
                    if (pattern.charAt(i) == '#') {
                        if (!Character.isDigit(string.charAt(i))) {
                            return false;
                        }
                    } else if (pattern.charAt(i) != string.charAt(i)) {
                        return false;
                    }
                }
                return true;
            }
        };
        return filters(format, filter);
    }

    @Override
    public Iterator<String> getStringsByPattern(String pattern) {
        Filter filter = new Filter() {
            @Override
            public boolean check(String string, String pattern) {
                if (string == null) {
                    return false;
                }
                String tmpPattern = pattern;
                String tmpString = string;
                int index;
                boolean first = false;
                while ((index = tmpPattern.indexOf("*")) != -1) {
                    if (index == 0) {
                        tmpPattern = tmpPattern.substring(1);
                        first = true;
                        continue;
                    }
                    int tmpIndex = tmpString
                            .indexOf(tmpPattern.substring(0, index));
                    if (tmpIndex == -1
                            || (!first && tmpIndex != 0)) {
                        return false;
                    }
                    tmpString = tmpString.substring(tmpIndex + index);
                    tmpPattern = tmpPattern.substring(index);
                    first = false;
                }
                return (first && new StringBuilder(tmpString).reverse().toString()
                        .startsWith(new StringBuilder(tmpPattern).reverse().toString()))
                        || tmpString.equals(tmpPattern);
            }
        };
        return filters(pattern, filter);
    }
}
