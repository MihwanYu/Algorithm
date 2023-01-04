import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int[][] map, dis;
    static int minLength;
    static int minBreadEatten;
    static Coordinate nest;

    /*
    bfs로 푼 헨젤과 그레텔 묹
    */
    public static void main(String[] args) throws IOException{
        int testcase = Integer.parseInt(br.readLine());
        for(int t = 0; t<testcase; t++){
        String nmrc[] = br.readLine().split(" ");
        int[] NMRC = Arrays.stream(nmrc).mapToInt(Integer::parseInt).toArray();
        map = new int[NMRC[0]][NMRC[1]];
        dis = new int[NMRC[0]][NMRC[1]]; //BFS
        nest = new Coordinate(NMRC[2]-1, NMRC[3]-1);//까마귀 둥지 좌표
        minLength = Integer.MAX_VALUE;
        minBreadEatten = Integer.MAX_VALUE;

        for(int n=0; n<NMRC[0]; n++){
            String row[] = br.readLine().split(" ");
            map[n] = Arrays.stream(row).mapToInt(Integer::parseInt).toArray();
        }
        
        // long beforeTime = System.currentTimeMillis(); //코드 실행 전에 시간 받아오기
        BFSroute(0,0);//BFS시도

        ArrayList<Coordinate> CurrentPath = new ArrayList<Coordinate>();
        findRoute(CurrentPath, 0, 0, 0);

        // System.out.println("distance: "+dis[map.length-1][map[0].length-1]);
        // System.out.println("min bread eatten: "+minBreadEatten);
        minLength = dis[map.length-1][map[0].length-1];

        //최소 이동 횟수 + 빵 부스러기 거리합 최솟값
        bw.write("#"+(t+1)+" "+minLength+" "+minBreadEatten);
        bw.newLine();
        // long afterTime = System.currentTimeMillis(); // 코드 실행 후에 시간 받아오기
        // long secDiffTime = (afterTime - beforeTime); //두 시간에 차 계산
        // System.out.println("시간차이(m) : "+secDiffTime);
        }
        bw.flush();
        bw.close();
    }


    static void BFSroute(int r, int c){
        Queue<Coordinate> Q = new LinkedList<Coordinate>();
        Coordinate current = new Coordinate(r,c);
        Q.offer(current);
        map[r][c] = -1; //지나온 곳 표시
        int[] dx = {-1, 0, 1, 0};
	    int[] dy = {0, 1, 0, -1};

        while(!Q.isEmpty()){
			Coordinate cv = Q.poll();
			for(int i=0; i<4; i++){
				int ncol = cv.col + dx[i];
				int nrow = cv.row + dy[i];
				
				if(ncol>=0&&ncol<map[0].length&&nrow>=0&&nrow<map.length && map[nrow][ncol]==1){
                	// 방문 체크 (재방문 하지 않기 위해)
					map[nrow][ncol]=-1;
					Q.offer(new Coordinate(nrow, ncol));
					dis[nrow][ncol] = dis[cv.row][cv.col]+1;
				}				
			}
    }}

    public static void findRoute(ArrayList<Coordinate>path, int r, int c, int length){
        
        Coordinate current = new Coordinate(r,c);
        ArrayList<Coordinate> newPath = new ArrayList<Coordinate>();
        for(Coordinate p:path){
            newPath.add(p);
        }
        newPath.add(current);

        if(length==dis[map.length-1][map[0].length-1]){
            // System.out.println("path에 없는 곳들 둥지와의 거리 구하기, "+path.size());
            int newBreadEatten = eatupcookie(newPath);
            if(minBreadEatten>newBreadEatten){
                minBreadEatten = newBreadEatten;
            }
            return ;
        }

        //to down: 다음 숫자가 아래쪽에 있으면 아래로 이동 
        if(r<map.length-1 && dis[r+1][c]==length+1){
            findRoute(newPath, r+1, c, length+1);
        }

        //to right 
        if(c<map[0].length-1 && dis[r][c+1]==length+1 ){
            findRoute(newPath, r, c+1, length+1);
        }
        //to left
        if(c>0 && dis[r][c-1]==length+1 ){
            findRoute(newPath, r, c-1, length+1);
        }
        //to upward
        if(r>0 && dis[r-1][c]==length+1 ){
            findRoute(newPath, r-1, c, length+1);
        }
    }

    static int eatupcookie(ArrayList<Coordinate>path){
        int count = 0;

        for(int r=0; r<map.length; r++){
            for(int c = 0; c<map[0].length; c++){
                // System.out.print(map[r][c]+" ");
                if(map[r][c]==1){
                    int rc_to_nest = Math.abs(r-nest.row) + Math.abs(c-nest.col);
                    count += rc_to_nest;
                }else if(map[r][c]==-1 && (!path.contains(new Coordinate(r,c)))){
                    // System.out.print("("+r+","+c+") ");
                    int rc_to_nest = Math.abs(r-nest.row) + Math.abs(c-nest.col);
                    count += rc_to_nest;
                }
            }
            // System.out.println();
        }
        // System.out.println(count+"\n----------------\n");

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

    @Override
    public String toString(){
        return "("+this.row+","+this.col+") ";
    }
    

}
