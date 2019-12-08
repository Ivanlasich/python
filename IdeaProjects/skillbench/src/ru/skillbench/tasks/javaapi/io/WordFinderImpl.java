package ru.skillbench.tasks.javaapi.io;
import java.nio.charset.Charset;
import java.util.*;
import java.io.*;
import java.util.List;
import java.util.stream.Stream;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.nio.charset.StandardCharsets;
public class WordFinderImpl implements WordFinder{


    private String texts = null;
    private Set<String> words = null;
    private Stream<String> an = null;

    public WordFinderImpl(){

        this.words = words;
        this.texts = texts;
    }


    private void checkNull(Object object) {
        if (object == null) {
            throw new IllegalArgumentException();
        }
    }

    @Override
    public String getText() {
        return texts;
    }

    @Override
    public void setText(String text) {
        checkNull(text);
        texts = text;
        words = new HashSet<String>(Arrays.asList(text.toLowerCase().split("[\\s]+")));
    }


    @Override
    public void setInputStream(InputStream is) throws IOException {


        checkNull(is);
        BufferedReader br = new BufferedReader(new InputStreamReader(is));
        String line;
        String ans="";
        while((line = br.readLine()) != null) {
            ans = ans + line + "\n";
        }
        setText(ans);
    }

    @Override
    public void setFilePath(String filePath) throws IOException {
        checkNull(filePath);
        File file = new File(filePath);
        FileReader fileReader = new FileReader(file);
        BufferedReader bufferedReader = new BufferedReader(fileReader);
        String line;
        String ans="";
        while((line = bufferedReader.readLine()) != null) {
            ans = ans + line + "\n";
        }
        setText(ans);
    }

    @Override
    public void setResource(String resourceName) throws IOException {
        checkNull(resourceName);
        InputStream is = this.getClass().getResourceAsStream(resourceName);
        setInputStream(is);
    }

    @Override
    public Stream<String> findWordsStartWith(String begin) {

        List<String> list = new ArrayList<String>();

        if(begin == null || begin.equals("")){
            for (String word : words) {
                    list.add(word);
            }
            an = list.stream();
            return an;
        }

        for (String word : words) {

            if (word.startsWith(begin.toLowerCase())) {

                list.add(word);
            }
        }
        an = list.stream();
        return an;
    }

    @Override
    public void writeWords(OutputStream os) throws IOException {
        String s="";
        List<String> list = new ArrayList<String>();
        an.sorted().forEach(x -> list.add(x));
        for (String word : list) {
                s=s+word+" ";
            }
        os.write(s.getBytes(Charset.forName("UTF-8")));
       // an.forEach(x -> System.out.println(x));
    }
}
