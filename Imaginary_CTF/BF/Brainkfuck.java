import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Stack;

public class Brainkfuck {
    public static void main(String[] args) {
        try {
            BufferedReader br = new BufferedReader(new FileReader("C:\\Users\\USER\\Desktop\\Imaginary_CTF\\Imaginary_CTF\\BF\\final.txt"));
            String s ;
            String word [];
            while((s=br.readLine())!=null){
                word=s.split(",");
                ex(word[0]);
            }
            
        } catch (Exception e) {
            e.printStackTrace();
        }
     
    }
    public static void ex(String ex){
        String bf = ex;
        int[] list = {0, 0, 0};
        int temp = 0;
        Stack<Integer> loopStack = new Stack<>();

        for (int i = 0; i < bf.length(); i++) {
            char command = bf.charAt(i);

            switch (command) {
                case '>':
                    temp += 1;
                    if (temp >= list.length) {
                        temp = 0; // wrap around
                    }
                    break;
                case '<':
                    temp -= 1;
                    if (temp < 0) {
                        temp = list.length - 1; // wrap around
                    }
                    break;
                case '+':
                    list[temp] += 1;
                    break;
                case '-':
                    list[temp] -= 1;
                    break;
                case '[':
                    if (list[temp] == 0) {
                        int openBrackets = 1;
                        while (openBrackets != 0) {
                            i++;
                            if (bf.charAt(i) == '[') openBrackets++;
                            else if (bf.charAt(i) == ']') openBrackets--;
                        }
                    } else {
                        loopStack.push(i);
                    }
                    break;
                case ']':
                    if (list[temp] != 0) {
                        i = loopStack.peek();
                    } else {
                        loopStack.pop();
                    }
                    break;
                default:
                    break;
            }
        }

       
        System.out.print((char)(list[0]*-1));
    }
}

