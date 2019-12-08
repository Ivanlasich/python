package ru.skillbench.tasks.javaapi.reflect;

import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.util.stream.Stream;

public class ReflectorImpl implements Reflector{


    @Override
    public void setClass(Class<?> clazz) {

    }

    @Override
    public Stream<String> getMethodNames(Class<?>... paramTypes) {
        return null;
    }

    @Override
    public Stream<Field> getAllDeclaredFields() {
        return null;
    }

    @Override
    public Object getFieldValue(Object target, String fieldName) throws NoSuchFieldException, IllegalAccessException {
        return null;
    }

    @Override
    public Object getMethodResult(Object constructorParam, String methodName, Object... methodParams) throws IllegalAccessException, InstantiationException, NoSuchMethodException, InvocationTargetException {
        return null;
    }
}
