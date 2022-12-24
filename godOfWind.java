import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static String[] dirs = {"E", "W", "S", "N"};
    static int[][] Mat;
    static int mostDense;

    public static void main(String[] args) throws IOException{
        /*
        바람의 신이 KKK번 바람을 보낼 때, 사람이 가장 많은 구역의 사람 수를 출력하시오.
        */
        int testcase = Integer.parseInt(br.readLine());
        for(int t = 0; t<testcase; t++){
            mostDense = 0;
            String s[] = br.readLine().split(" ");
            int[] info = Arrays.stream(s).mapToInt(Integer::parseInt).toArray();
            Mat = new int[info[0]][info[1]];
            for(int row= 0; row<info[0]; row++){
                String lineInput[] =  br.readLine().split(" ");
                Mat[row] = Arrays.stream(lineInput).mapToInt(Integer::parseInt).toArray();
            }
            //1<=K<=5

            String[] direction = new String[info[2]];
            combination(direction, 0, info[2]);

            bw.write("#"+(t+1)+" "+mostDense);
            bw.newLine();
        }
        bw.flush();
        bw.close();
    }
    static void combination(String[] result, int cnt, int k) {
		if (cnt == k) {
			// System.out.println(Arrays.toString(result));
            Set<String> set = new HashSet<String>(Arrays.asList(result));
            if(set.size()>2) return;
            int densed = countPeople(result);
            if(densed>mostDense) mostDense = densed;
			return;
		}
		for (int i = 0; i < 4; i++) {
			result[cnt] = dirs[i];
			combination(result, cnt + 1, k);
		}
	}

    static int countPeople(String[] direction){
        int count = 0;
        // int[][] mat =  Mat.clone();
        int mat[][] = new int[Mat.length][Mat[0].length];
	    
        for(int i=0; i<mat.length; i++){
            System.arraycopy(Mat[i], 0, mat[i], 0, Mat[0].length);
        }

        for(String dir: direction){
        switch(dir){
            case "W":
                for(int r = 0; r<mat.length; r++){
                    int c = 0;
                    while (mat[r][c] ==0){
                        if(c==mat[0].length-1) break;
                        c++;
                    }
                    if(c==mat[0].length-1) continue;
                    mat[r][c+1] += mat[r][c];
                    mat[r][c]=0;
                }
                break;
            case "E":
                for(int r = 0; r<mat.length; r++){
                        int c = mat[0].length-1;
                        while (mat[r][c] ==0){
                            if(c==0) break;
                            c--;
                        }
                        if(c==0) continue;
                        mat[r][c-1] += mat[r][c];
                        mat[r][c]=0;
                    }
                break;
            case "S":
                for(int c = 0; c<mat[0].length; c++){
                    int r = mat.length-1;
                    while(mat[r][c]==0){
                        if(r==0) break;
                        r--;
                    }
                    if(r==0) continue;
                    mat[r-1][c] += mat[r][c];
                    mat[r][c] = 0;
                }
            break;
            case "N":
                for(int c = 0; c<mat[0].length; c++){
                    int r = 0;
                    while(mat[r][c]==0){
                        if(r==mat.length-1) break;
                        r++;
                    }
                    if(r==mat.length-1) continue;
                    mat[r+1][c] += mat[r][c];
                    mat[r][c] = 0;
                }
            break;
        }
            // System.out.println("After Switching,");
            // for(int r = 0; r<mat.length; r++){
            //     System.out.println(Arrays.toString(mat[r]));
            // }
            // System.out.println();
        }

        for(int r = 0; r<mat.length; r++){
                // System.out.println(Arrays.toString(mat[r]));
                Arrays.sort(mat[r]);
                if(count<mat[r][mat[0].length-1]) count = mat[r][mat[0].length-1];
            }
        // System.out.println(count+"\n----------------\n");
        return count;
    }

}
