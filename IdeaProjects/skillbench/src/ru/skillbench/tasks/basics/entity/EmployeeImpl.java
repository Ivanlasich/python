package ru.skillbench.tasks.basics.entity;

public class EmployeeImpl implements Employee {

    private String first_name = null;
    private String last_name = null;
    private Employee manager = null;
    private int salary;


    public EmployeeImpl() {

        this.first_name = first_name;
        this.last_name = last_name;
        this.manager = manager;
        this.salary =1000;

    }



    @Override
    public int getSalary() {
        return this.salary;
    }

    @Override
    public void increaseSalary(int value) {
        this.salary=this.salary+value;
    }

    @Override
    public String getFirstName() {
        return this.first_name;
    }

    @Override
    public void setFirstName(String firstName) {
        this.first_name=firstName;

    }

    @Override
    public String getLastName() {
        return this.last_name;
    }

    @Override
    public void setLastName(String lastName) {
        this.last_name=lastName;
    }

    @Override
    public String getFullName() {
        return this.first_name + " " + this.last_name;
    }

    @Override
    public void setManager(Employee manager) {
            this.manager=manager;
    }

    @Override
    public String getManagerName() {
        if (this.manager == null) {
            return "No manager";
        } else {
            return this.manager.getFullName();
        }
    }

    @Override
    public Employee getTopManager() {
        if (this.manager == null) {
            return this;
        } else {
            return this.manager.getTopManager();
        }
    }
}
