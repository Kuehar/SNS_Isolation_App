public class UnionFind{
    public static void main(String[] args){
        int N = StdIn.readInt();
        while(!StdIn.isEmpty()){
            int p = StdIn.readInt();
            int q = StdIn.readInt();
            if(!uf.connected(p,q)){
                uf.union(p,q);
                StdOut.print
            }
        }
    }
}