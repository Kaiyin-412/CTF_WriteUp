public class test{
    public static void main(String[] args) {
        String word ="lfqc~opvqZdkjqm`wZcidbZfm`fn`wZd6130a0`0``761gdx";
        StringBuilder sb = new StringBuilder();
       for(int i=0;i<=47;i++){
            char temp = (char)(word.charAt(i) ^5);
            sb.append(temp);

       }
       System.out.println(sb.toString());
    }
}