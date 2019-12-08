package ru.skillbench.tasks.basics.math;


import java.util.Arrays;

public class ArrayVectorImpl implements ArrayVector {

    public static double[] arr = null;


    @Override
    public void set(double... elements) {
        arr = new double[elements.length];
        for(int i=0; i < elements.length; i++){
            arr[i] = elements[i];
        }
    }

    @Override
    public double[] get() {
        return arr;
    }

    @Override
    public ArrayVector clone() {

        ArrayVector A = new ArrayVectorImpl();
        A.set(arr.clone());
        return A;
    }

    @Override
    public int getSize() {
        if (arr == null)
            return 0;
        else
            return arr.length;
    }

    @Override
    public void set(int index, double value) {
        if (index < 0) return;
        if(index < this.getSize()){
            arr[index]=value;
            return;
        }
        else {
            double[] newarr;
            newarr = new double[index + 1];
            for (int i = 0; i < newarr.length; i++) {
                newarr[i] = 0;
            }
            for (int i = 0; i < arr.length; i++) {
                newarr[i] = arr[i];
            }
            newarr[index] = value;
            arr = newarr;
            return;
        }
    }

    @Override
    public double get(int index) throws ArrayIndexOutOfBoundsException {
        if((index>=0) & (index < arr.length)){
            return arr[index];
        }
        else throw new ArrayIndexOutOfBoundsException();
    }

    @Override
    public double getMax() {
        double max;
        max = arr[0];
        for (int i=0;i<arr.length;i++){
            if(max < arr[i]){
                max = arr[i];
            }
        }
        return max;
    }

    @Override
    public double getMin() {
        double min;
        min = arr[0];
        for (int i=0; i < arr.length; i++){
            if(min > arr[i]){
                min = arr[i];
            }
        }
        return min;
    }

    @Override
    public void sortAscending() {
        Arrays.sort(arr);
    }

    @Override
    public void mult(double factor) {
        for (int i=0; i < this.getSize(); i++){
            arr[i] = arr[i] * factor;
        }
    }

    @Override
    public ArrayVector sum(ArrayVector anotherVector) {
        if(anotherVector.getSize() > this.getSize()){
            for (int i = 0;i < this.getSize(); i++){
                arr[i]=arr[i] + anotherVector.get(i);
            }
            return this;
        }
        else {
            for (int i = 0; i < anotherVector.getSize(); i++){
                arr[i]=arr[i] + anotherVector.get(i);
            }
            return this;
        }
    }

    @Override
    public double scalarMult(ArrayVector anotherVector) {

        double ans = 0;
        if(anotherVector.getSize() > this.getSize()){
            for (int i = 0;i < this.getSize(); i++){
                ans = ans + arr[i]*anotherVector.get(i);
            }
            return ans;
        }
        else {
            for (int i = 0; i < anotherVector.getSize(); i++){
                ans = ans + arr[i]*anotherVector.get(i);
            }
            return ans;
        }
    }

    @Override
    public double getNorm() {
        return Math.sqrt(scalarMult(this));
    }
}
