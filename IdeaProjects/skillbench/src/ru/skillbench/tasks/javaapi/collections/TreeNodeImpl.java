package ru.skillbench.tasks.javaapi.collections;

import java.util.*;

public class TreeNodeImpl implements TreeNode {


    private Object data;

    private boolean expanded;

    private TreeNode parent;

    private Set<TreeNode> children;


    public TreeNodeImpl() {
        this.expanded = false;
    }

    public TreeNodeImpl(TreeNode parent, Object data) {

        this.data = data;
        this.parent = parent;
        this.expanded = false;
        if (this.parent != null)
            this.parent.addChild(this);

    }

    @Override
    public TreeNode getParent() {
        return parent;
    }

    @Override
    public void setParent(TreeNode parent) {
        this.parent = parent;
    }

    @Override
    public TreeNode getRoot() {
        if (this.parent == null) {
            return null;
        } else {
            TreeNode tmp = this;
            while (true) {
                if (tmp.getParent() == null) {
                    //tmp = this;
                    break;
                } else {
                    tmp = tmp.getParent();
                }
            }
            return tmp;
        }
    }

    @Override
    public boolean isLeaf() {
        if(children == null || children.size() == 0){
            return true;
        }
        else {
            return false;
        }
    }

    @Override
    public int getChildCount() {
        if (children == null) {
            return 0;
        }
        else {
            return children.size();
        }
    }

    @Override
    public Iterator<TreeNode> getChildrenIterator() {
        if (getChildCount() != 0) {
            return this.children.iterator();
        } else {
            return null;
        }
    }

    @Override
    public void addChild(TreeNode child) {
        if (child.getRoot() != child && this != child && this.parent != child) {
            if (children == null) {
                children = new HashSet<>();
            }
            children.add(child);

            if (child.getParent() == null) {
                child.setParent(this);
            }
        }
    }

    @Override
    public boolean removeChild(TreeNode child) {
        if (children != null && this.children.contains(child)) {
            this.children.remove(child);
            child.setParent(null);
            return true;
        }

        return false;
    }

    @Override
    public boolean isExpanded() {
        return expanded;
    }

    @Override
    public void setExpanded(boolean expanded) {
        this.expanded = expanded;
        if (this.children != null && this.children.size() != 0) {
            for (TreeNode child : this.children) {
                child.setExpanded(expanded);
            }
        }
    }

    @Override
    public Object getData() {
        return this.data;
    }

    @Override
    public void setData(Object data) {
        this.data = data;
    }

    @Override
    public String toString() {
        if (getData() != null)
            return getData().toString();
        else
            return "empty";
    }

    private List<String> pathSearch() {
        List<String> path = new ArrayList<>();

        if (this.parent != null) {
            path.add(parent.getTreePath());
        }

        path.add(this.toString());
        return path;
    }

    @Override
    public String getTreePath() {
        StringBuilder path = new StringBuilder();
        for (int i = 0; i < this.pathSearch().size() - 1; i++) {
            path.append(this.pathSearch().get(i)).append("->");
        }
        path.append(this.pathSearch().get(pathSearch().size() - 1));

        return path.toString();
    }

    @Override
    public TreeNode findParent(Object data) {

        if ((this.getData() == null && this.getData() == data) || (this.getData() != null && this.getData().equals(data))) {
            return this;
        } else if (this.parent == null) {
            return null;
        } else {
            return parent.findParent(data);
        }
    }

    @Override
    public TreeNode findChild(Object data) {
        TreeNode tmp = null;

        if (this.children != null) {
            for (TreeNode tree : this.children) {
                if (tmp != null) {
                    break;
                } else if ((data == null && tree.getData() == null) || (data != null && tree.getData() != null && tree.getData().equals(data))) {
                    tmp = tree;
                } else {
                    tmp = null;
                }
            }

            if (tmp == null) {
                for (TreeNode t : this.children) {
                    if (tmp != null) {
                        break;
                    }
                    tmp = t.findChild(data);
                }
            }
        }

        return tmp;
    }
}