import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int[][] map;
    static int MinLength;
    static int minBreadEatten;
    static Coordinate nest;

    static ArrayList<Coordinate> MinPath;
    static ArrayList<Coordinate> AllBread;

    public static void main(String[] args) throws IOException{
        /*
        DFS -> Time Limit ERror
        헨젤과 그레텔의 부모님이 아이들을 찾는 최소 이동 횟수와 이 때 까마귀가 먹을 수 있는 빵 부스러기의 거리의 합의 최솟값을 구하시오.
        */
        int testcase = Integer.parseInt(br.readLine());
        for(int t = 0; t<testcase; t++){
        String nmrc[] = br.readLine().split(" ");
        int[] NMRC = Arrays.stream(nmrc).mapToInt(Integer::parseInt).toArray();
        map = new int[NMRC[0]][NMRC[1]];
        nest = new Coordinate(NMRC[2]-1, NMRC[3]-1);//까마귀 둥지 좌표
        MinLength = Integer.MAX_VALUE;
        minBreadEatten = Integer.MAX_VALUE;

        AllBread = new ArrayList<Coordinate>();
        MinPath = new ArrayList<Coordinate>();

        for(int n=0; n<NMRC[0]; n++){
            String row[] = br.readLine().split(" ");
            map[n] = Arrays.stream(row).mapToInt(Integer::parseInt).toArray();
            for(int c=0; c<map[0].length; c++){
                if (map[n][c]==1){
                    AllBread.add(new Coordinate(n,c));
                }
            }
        }
        long beforeTime = System.currentTimeMillis(); //코드 실행 전에 시간 받아오기
        ArrayList<Coordinate> CurrentPath = new ArrayList<Coordinate>();
        findRoute(CurrentPath, 0, 0, 0);

        //최소 이동 횟수 + 빵 부스러기 거리합 최솟값
        bw.write("#"+(t+1)+" "+MinLength+" "+minBreadEatten);
        bw.newLine();
        long afterTime = System.currentTimeMillis(); // 코드 실행 후에 시간 받아오기
        long secDiffTime = (afterTime - beforeTime); //두 시간에 차 계산
        System.out.println("시간차이(m) : "+secDiffTime);
        }
        
        bw.flush();
        bw.close();
    }

    public static void findRoute(ArrayList<Coordinate>path, int r, int c, int length){
        //이상치 넘기면 탐색중지
        if(length>MinLength || length>map.length * map[0].length ) return;
        
        Coordinate current = new Coordinate(r,c);
        ArrayList<Coordinate> newPath = new ArrayList<Coordinate>();
        for(Coordinate p:path){
            newPath.add(p);
        }
        newPath.add(current);

        if(r==map.length-1 && c==map[0].length-1){
            if(MinLength>length){
                MinLength = length;
                minBreadEatten = eatupcookie(newPath);
            }
            else if(MinLength==length){
                //최단경로가 2개 이상일 경우
                int newBreadEatten = eatupcookie(newPath);
                if(minBreadEatten>newBreadEatten){
                    minBreadEatten = newBreadEatten;
                }
            }
        }
        //to down -> 이동할 경로가 이전에 있었는지 확인 
        if(r<map.length-1 && map[r+1][c]==1 && (!newPath.contains(new Coordinate(r+1,c)))){
            findRoute(newPath, r+1,c,length+1);
        }
        //to right 
        if(c<map[0].length-1 && map[r][c+1]==1 &&(!newPath.contains(new Coordinate(r,c+1))) ){
            findRoute(newPath, r, c+1, length+1);
        }
        //to left
        if(c>0 && map[r][c-1]==1 && (!newPath.contains(new Coordinate(r,c-1))) ){
            findRoute(newPath, r, c-1, length+1);
        }
        //to upward
        if(r>0 && map[r-1][c]==1 && (!newPath.contains(new Coordinate(r-1,c))) ){
            findRoute(newPath, r-1, c, length+1);
        }
    }

    static int eatupcookie(ArrayList<Coordinate>path){
        int count = 0;
        //count up bread length among AllBread which doesn't exist on path
        ArrayList<Coordinate> eatable = new ArrayList<Coordinate>();
        for(Coordinate bread:AllBread){
            if (!path.contains(bread)){
                // System.out.print("("+bread.row+", "+bread.col+")");
                count += Math.abs(bread.row-nest.row);
                count += Math.abs(bread.col-nest.col);
                // count += nestToBread;
                if(minBreadEatten<count) return count;
            }
        }
        // System.out.println();
        // for(int i=0; i<path.size(); i++){
        //     System.out.print("("+path.get(i).row+", "+path.get(i).col+")");
        // }
        // System.out.println("\nAll bread: ");
        // for(int i=0; i<AllBread.size(); i++){
        //     System.out.print("("+AllBread.get(i).row+", "+AllBread.get(i).col+")");
        // }


        // int margincookie[][] = new int[map.length][map[0].length];
        // for(int i=0; i<margincookie.length; i++){
        //     System.arraycopy(map[i], 0, margincookie[i], 0, map[0].length);
        // }
        // System.out.println("case: before eatup,");
        // for(int r=0; r<margincookie.length; r++){
        //     System.out.println(Arrays.toString(margincookie[r]));
        // }
        // for(int i=0; i<path.size(); i++){
        //     // System.out.print("("+path.get(i).row+", "+path.get(i).col+")");
        //     margincookie[path.get(i).row][path.get(i).col] = 0;
        // }
        // System.out.println("\nafter eatup,");
        // for(int r=0; r<margincookie.length; r++){
        //     // System.out.println(Arrays.toString(margincookie[r]));
        //     for(int c = 0; c<margincookie[0].length; c++){
        //         if(margincookie[r][c]==1){
        //             int nestToBread = Math.abs(r-nest.row) + Math.abs(c-nest.col);
        //             count += nestToBread;
        //         }
        //     }
        // }
        // System.out.println("count: "+count+"\n--------------------------\n");

        return count;
    }

}

class Coordinate implements Cloneable{
    int row, col;
    Coordinate(){
        this.row=0; this.col=0;
    }
    Coordinate(int r, int c){
        this.row = r; this.col = c;
    }

    @Override
    public boolean equals(Object object) {
        boolean sameSame = false;

        if (object != null && object instanceof Coordinate){
            if((this.row == ((Coordinate) object).row) && (this.col == ((Coordinate) object).col)){
                // System.out.println(this.row+"=="+((Coordinate) object).row +", "+this.col+"=="+((Coordinate) object).col);
                sameSame = true;
            }
        }

        return sameSame;
}
    

}
