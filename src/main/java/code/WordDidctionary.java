package main.java.code;

import java.util.HashMap;
import java.util.Map;

class WordDictionary {

    private static class Node {
        Map<Character, Node> children;

        Node() {
            this.children = new HashMap<>();
        }

        void addWord(String word) {
            if (word.isEmpty()) {
                children.put('*', new Node());
                return;
            }
            children.computeIfAbsent(word.charAt(0), ket -> new Node());
            children.get(word.charAt(0)).addWord(word.substring(1));
        }

        boolean search(String word) {
            if (word.isEmpty()) {
                return children.containsKey('*');
            }
            if (children.containsKey(word.charAt(0))) {
                return children.get(word.charAt(0)).search(word.substring(1));
            }
            if (word.charAt(0) == '.') {
                return children.values().stream().anyMatch(node -> node.search(word.substring(1)));
            }
            return false;
        }
    }

    private Node root;

    /**
     * Initialize your data structure here.
     */
    public WordDictionary() {
        root = new Node();

    }

    /**
     * Adds a word into the data structure.
     */
    public void addWord(String word) {
        root.addWord(word);
    }

    /**
     * Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
     */
    public boolean search(String word) {
        if (word.isEmpty()) {
            return false;
        }
        return root.search(word);
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
