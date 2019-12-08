package ru.skillbench.tasks.basics.math;


import java.util.Arrays;

import static java.lang.Math.pow;
import static java.lang.StrictMath.sqrt;

public class ComplexNumberImpl implements ComplexNumber {


    double im = 0;
    double re = 0;

    public ComplexNumberImpl(double re, double im){
        this.re = re;
        this.im = im;

    }

    public ComplexNumberImpl(){
        this.re = 0;
        this.im = 0;

    }

    public ComplexNumberImpl(String s){
        this.im=0;
        this.re=0;

        if (s.lastIndexOf("+")!=-1) {
            if (s.lastIndexOf("i")!=-1){

                this.re = Double.valueOf(s.substring(0, s.lastIndexOf("+")));
                this.im = Double.valueOf(s.substring(s.lastIndexOf('+') + 1, s.lastIndexOf("i")));
                return;

            }
            this.re = Double.valueOf(s);
            return;
        }

        if (s.lastIndexOf("-")!=-1) {
            if (s.lastIndexOf("i") != -1) {

                if (s.substring(0, s.lastIndexOf("-")).equals("") == false) this.re = Double.valueOf(s.substring(0, s.lastIndexOf("-")));
                this.im = -Double.valueOf(s.substring(s.lastIndexOf('-') + 1, s.lastIndexOf("i")));
                return;
            }
            this.re = Double.valueOf(s);
            return;
        }
        this.im = Double.valueOf(s);

    }


    @Override
    public double getRe() {
        return this.re;
    }

    @Override
    public double getIm() {
        return this.im;
    }

    @Override
    public boolean isReal() {
        if(this.im == 0){
            return true;
        }
        return false;
    }

    @Override
    public void set(double re, double im) {

        this.re = re;
        this.im = im;
    }

    @Override
    public void set(String value) throws NumberFormatException {

        try {
            this.im=0;
            this.re=0;
            if (value.lastIndexOf("+")!=-1 & value.lastIndexOf("-")!=-1){
                if (value.lastIndexOf("+")>value.lastIndexOf("-")){
                    if (value.lastIndexOf("i")!=-1){

                        this.re = Double.valueOf(value.substring(0, value.lastIndexOf("+")));
                        if(value.substring(value.lastIndexOf('+') + 1, value.lastIndexOf("i")).equals("")){
                            this.im=1;
                            return;
                        }
                        this.im = Double.valueOf(value.substring(value.lastIndexOf('+') + 1, value.lastIndexOf("i")));
                        return;

                    }
                    this.re = Double.valueOf(value);
                    return;
                }
                else {
                    if (value.lastIndexOf("i") != -1) {

                        if (value.substring(0, value.lastIndexOf("-")).equals("") == false) this.re = Double.valueOf(value.substring(0, value.lastIndexOf("-")));
                        if(value.substring(value.lastIndexOf('-')+1, value.lastIndexOf("i")).equals("")){
                            this.im=-1;
                            return;
                        }
                        this.im = -Double.valueOf(value.substring(value.lastIndexOf('-') + 1, value.lastIndexOf("i")));
                        return;
                    }
                    this.re = Double.valueOf(value);
                    return;
                }

            }





            if (value.lastIndexOf("+")!=-1) {
                if (value.lastIndexOf("i")!=-1){

                    this.re = Double.valueOf(value.substring(0, value.lastIndexOf("+")));
                    if(value.substring(value.lastIndexOf('+') + 1, value.lastIndexOf("i")).equals("")){
                        this.im=1;
                        return;
                    }
                    this.im = Double.valueOf(value.substring(value.lastIndexOf('+') + 1, value.lastIndexOf("i")));
                    return;

                }
                this.re = Double.valueOf(value);
                return;
            }

            if (value.lastIndexOf("-")!=-1) {
                if (value.lastIndexOf("i") != -1) {

                    if (value.substring(0, value.lastIndexOf("-")).equals("") == false) this.re = Double.valueOf(value.substring(0, value.lastIndexOf("-")));
                    if(value.substring(value.lastIndexOf('-')+1, value.lastIndexOf("i")).equals("")){
                        this.im=-1;
                        return;
                    }
                    this.im = -Double.valueOf(value.substring(value.lastIndexOf('-') + 1, value.lastIndexOf("i")));
                    return;
                }
                this.re = Double.valueOf(value);
                return;
            }
            if(value.lastIndexOf("i") != -1){
                if(value.substring(0, value.lastIndexOf("i")).equals("")){
                    this.im=1;
                    return;
                }
                this.im = Double.valueOf(value.substring(0, value.lastIndexOf("i")));
                return;
            }
            this.re = Double.valueOf(value);
            } catch (NumberFormatException e){
            throw new NumberFormatException();

        }

    }

    @Override
    public ComplexNumber copy() {
        double a, b;
        a = this.re;
        b = this.im;
        ComplexNumberImpl A = new ComplexNumberImpl(a, b);

        return A;
    }

    @Override
    public ComplexNumber clone() throws CloneNotSupportedException {

            double a, b;
            a = this.re;
            b = this.im;
            ComplexNumberImpl A = new ComplexNumberImpl(a, b);
            return A;

    }

    @Override
    public String toString(){
        String s="";
        if (this.re == 0 & this.im == 0){
            return "0";
        }
        if (this.im == 0){
            s = s + this.re;
            return s;
        }

        if (this.re == 0){
            s = s + this.im+"i";
            return s;
        }
        s = s + this.re +"+" + this.im +"i";

        return s;
    }

    @Override
    public boolean equals(Object other) {

        if (other instanceof ComplexNumber) {
            return (this.getIm() == ((ComplexNumber)other).getIm() & this.getRe() == ((ComplexNumber)other).getRe());
        } else {
            return false;
        }
    }


    @Override
    public int compareTo(ComplexNumber other) {
        Double a = sqrt(pow(this.getRe(), 2) + pow(this.getIm(), 2));
        Double b = sqrt(pow(other.getRe(), 2) + pow(other.getIm(), 2));
        if(a>b) return 1;
        if (a==b) return 0;
        return -1;
    }

    @Override
    public void sort(ComplexNumber[] array) {
        Arrays.sort(array);

    }

    @Override
    public ComplexNumber negate() {
        this.re = -this.re;
        this.im = -this.im;
        return this;
    }

    @Override
    public ComplexNumber add(ComplexNumber arg2) {
        this.re = this.re + arg2.getRe();
        this.im = this.im + arg2.getIm();
        return this;
    }

    @Override
    public ComplexNumber multiply(ComplexNumber arg2) {
        double a, b, c, d;
        a = this.re;
        b = this.im;
        c = arg2.getRe();
        d = arg2.getIm();
        this.re = a*c - d*b;
        this.im = a*d +b*c;
        return this;
    }
}
