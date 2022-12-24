import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static char[][] area;
    static int minTime;

    /*
    모든 인홤 물질까지 소화제를 터뜨리는 최소의 시간
    */
    public static void main(String[] args) throws IOException{
        int testcase = Integer.parseInt(br.readLine());
        long beforeTime = System.currentTimeMillis();
        for(int t = 0; t<testcase; t++){
            String s[] = br.readLine().split(" ");
            int[] info = Arrays.stream(s).mapToInt(Integer::parseInt).toArray();
            minTime = Integer.MAX_VALUE;

            area = new char[info[0]][info[1]];
            for(int r=0; r<info[0]; r++){
                area[r] = br.readLine().toCharArray();
            }
            int rsum=0, csum=0;
            for(int i=0; i<info[2]; i++){
                String rc[] = br.readLine().split(" ");
                rsum += (Integer.parseInt(rc[0])-1);
                csum += (Integer.parseInt(rc[1])-1);
                area[Integer.parseInt(rc[0])-1][Integer.parseInt(rc[1])-1]='x';
            }

            int rinit = (rsum/info[2]);
            int cinit = (csum/info[2]);
            assignExtinguish(rinit, cinit, info[2]);
            
            if(minTime==Integer.MAX_VALUE){
                minTime = -1;
            }
            
            bw.write("#"+(t+1)+" "+minTime);
            bw.newLine();
        }
        long afterTime = System.currentTimeMillis(); // 코드 실행 후에 시간 받아오기
        long secDiffTime = (afterTime - beforeTime); //두 시간에 차 계산
        System.out.println("시간차이(m) : "+secDiffTime);
        bw.flush();
        bw.close();
    }

    //소화제 위치 bfs로 지정해가면서 해당 위치에서 위험물질까지 거리 구하기(bfs) 후 최솟값 없데이트
    static void assignExtinguish(int r, int c, int xnum){
        Queue<Coordinate> Q = new LinkedList<Coordinate>();
        Coordinate current = new Coordinate(r,c);
        Q.offer(current);

        char extMap[][] = new char[area.length][area[0].length];
        int dis[][] = new int[area.length][area[0].length];

        for(int i=0; i<extMap.length; i++){
            System.arraycopy(area[i], 0, extMap[i], 0, area[0].length);
        }

        int[] dx = {-1, 0, 1, 0};
	    int[] dy = {0, 1, 0, -1};

        if(extMap[r][c] !='#'){
            
            minTime = bfs(r,c, xnum);
        }
        extMap[r][c] = '*'; //지나온 곳 표시

        while(!Q.isEmpty()){
			Coordinate cv = Q.poll();
			for(int i=0; i<4; i++){
				int ncol = cv.col + dx[i];
				int nrow = cv.row + dy[i];
				
				if(ncol>=0&&ncol<extMap[0].length&&nrow>=0&&nrow<extMap.length && extMap[nrow][ncol]!='*'  ){
                    
                    if(extMap[nrow][ncol]!='#'){
                        int time = bfs(nrow, ncol, xnum);
                        if(time<minTime){
                            minTime = time; 
                        }
                    }

                    extMap[nrow][ncol]='*';
                    
                    
					Q.offer(new Coordinate(nrow, ncol));
					dis[nrow][ncol] = dis[cv.row][cv.col]+1;
				}				
			}
        }
    }

    //위험물질까지의 거리 구하기: 현재 위치에서 각 위험물질까지의 최단거리 구함, 최단거리 중 가장 긴 거리 = 모두 인화에 걸리는 시간
    static int bfs(int r, int c, int xnum){
        Queue<Coordinate> Q = new LinkedList<Coordinate>();
        Coordinate current = new Coordinate(r,c);
        Q.offer(current);
        
        char newMap[][] = new char[area.length][area[0].length];
        int distance[][] = new int[area.length][area[0].length];
        int timeComplete = 0;
        int xcount = 0;

        for(int i=0; i<newMap.length; i++){
            System.arraycopy(area[i], 0, newMap[i], 0, area[0].length);
        }
        if(newMap[r][c]=='x') xcount ++;
        newMap[r][c] = '*'; //지나온 곳 표시

        int[] dx = {-1, 0, 1, 0};
	    int[] dy = {0, 1, 0, -1};

        while(!Q.isEmpty()){
			Coordinate cv = Q.poll();
			for(int i=0; i<4; i++){
				int ncol = cv.col + dx[i];
				int nrow = cv.row + dy[i];
				
				if(ncol>=0&&ncol<newMap[0].length&&nrow>=0&&nrow<newMap.length && ( newMap[nrow][ncol]=='x' || newMap[nrow][ncol]=='.') ){
                	
                    // System.out.println("coordinate: ("+nrow+","+ncol+"), "+newMap[nrow][ncol]);
                    if(newMap[nrow][ncol]=='x'){
                        if(timeComplete< distance[cv.row][cv.col]+1 ){
                            timeComplete = distance[cv.row][cv.col]+1;
                            if(timeComplete>minTime) return timeComplete;
                        }
                        xcount ++;
                    }
					newMap[nrow][ncol]='*';
                    // if(xcount == xnum) return timeComplete;
					Q.offer(new Coordinate(nrow, ncol));
					distance[nrow][ncol] = distance[cv.row][cv.col]+1;
				}				
			}
        }
        if (xcount != xnum ) return Integer.MAX_VALUE;
        return timeComplete;
        }
}


class Coordinate{
    int row, col;
    Coordinate(int r, int c){
        this.row = r; this.col = c;
    }
}