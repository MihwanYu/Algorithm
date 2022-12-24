import java.io.*;
import java.util.*;
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)); // 선언
    static int maxPowerSum;

    public static void main(String[] args) throws IOException {
        /*
        서로 다른 NNN개의 자연수가 주어졌을 때 거의 제곱 고리에 존재하는 연속된 두 수의 합이 제곱수가 되는 개수를 구하여라.
        */

        int testcase = Integer.parseInt(br.readLine());
        for(int t = 0; t<testcase; t++){
            maxPowerSum = 0;
            int n =  Integer.parseInt(br.readLine());
            String s[] = br.readLine().split(" ");
            Integer[] numbers = Arrays.stream(s)
                .map(Integer::parseInt)
                .toArray(Integer[]::new);

            // int[] arr = {1, 2, 3};
            Integer[] output = new Integer[n];
            boolean[] visited = new boolean[n];
            permutation(numbers,output,visited,0,n);




            bw.write("#"+(t+1)+" "+maxPowerSum); // 출력
            bw.newLine(); // 줄바꿈
        }
        bw.flush(); // 남아있는 데이터 모두 출력
        bw.close();
    }

    static void permutation(Integer[] arr, Integer[] output, boolean visited[], int depth, int n) throws IOException {
        if(depth==n){
            int powersum = findPowerSum(output);
            if(maxPowerSum<powersum){
                maxPowerSum = powersum;
                // bw.write("maxPowersum: "+maxPowerSum);
            } 
            return;
        }
 
        for(int i=0;i<n;i++){
            if(!visited[i]){
                visited[i]=true;
                output[depth]=arr[i];
                if(output[0]!=arr[0]) return;
                permutation(arr,output,visited,depth+1,n);
                visited[i]=false;
            }
        }
    }

    static int findPowerSum(Integer[] output){
        int count = 0; int twosum;
        for(int i = 0; i<output.length; i++){
            if(i==output.length-1){
                twosum = output[i]+output[0];
            }else{
                twosum = output[i]+output[i+1];
            }
            if((int)Math.pow((int)Math.sqrt(twosum), 2) == twosum) {
                count ++;
            }
        }
        // System.out.println(Arrays.toString(output)+" has count number "+count);
        return count;
    }

}
