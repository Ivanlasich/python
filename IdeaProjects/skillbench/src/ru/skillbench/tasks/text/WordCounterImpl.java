package ru.skillbench.tasks.text;

import java.io.PrintStream;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.*;

public class WordCounterImpl implements WordCounter {
    String text = null;
    Map<String,Long> dict = null;

    public WordCounterImpl(){
        this.text = null;
        this.dict = null;
    }
    @Override
    public void setText(String text) {
        this.text=text;
    }

    @Override
    public String getText() {
        return this.text;
    }

    @Override
    public Map<String, Long> getWordCounts() {
        if(this.text == null){
            throw new IllegalStateException();
        }
        if (this.dict==null){
            this.dict = new HashMap<String, Long>();
            String[] list;
            String s;
            Long l;
            list = this.text.split("[ \\t\\n]+");
            for(int i = 0;i < list.length; i++){
                s = list[i].toLowerCase();
                if (s.matches("<.*>") || s.length() == 0)
                    continue;
                if(this.dict.containsKey(s)){
                    l = this.dict.get(s) + 1;
                    this.dict.put(s, l);
                }
                else {
                    l = new Long(1);
                    this.dict.put(s, l);
                }

            }

        }
        return new HashMap<String, Long>(this.dict);
    }

    @Override
    public List<Map.Entry<String, Long>> getWordCountsSorted() {
        if (this.text == null)
            throw new IllegalStateException();

        return sort(this.dict,this::compare);
    }

    public int compare(Map.Entry<String, Long> a, Map.Entry<String, Long> b) {
        if (b.getValue() > a.getValue())
            return 1;
        else if (b.getValue() < a.getValue())
            return -1;
        else
            return a.getKey().compareTo(b.getKey());
    }

    @Override
    public <K extends Comparable<K>, V extends Comparable<V>> List<Map.Entry<K, V>> sort(Map<K, V> map, Comparator<Map.Entry<K, V>> comparator) {
        List<Map.Entry<K, V>> newList = new ArrayList<Map.Entry<K, V>>();
        for (Map.Entry<K, V> entry : map.entrySet()) {
            newList.add(new AbstractMap.SimpleEntry<K, V>(entry));
        }
        Collections.sort(newList, comparator);

        return newList;
    }

    @Override
    public <K, V> void print(List<Map.Entry<K, V>> entries, PrintStream ps) {
        if (this.text == null){
            throw new IllegalStateException();
        }


        for (Map.Entry<K, V> entry : entries) {
            ps.format("%s %d\n", entry.getKey(), entry.getValue());
        }
    }
}
