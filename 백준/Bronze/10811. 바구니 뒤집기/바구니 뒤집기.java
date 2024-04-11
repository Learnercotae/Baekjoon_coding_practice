import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner=new Scanner(System.in);
		
		int N=scanner.nextInt();
		int M=scanner.nextInt();
		int del=0; //값을 옮기기 위한 변수 선언
		
		int arr[]=new int[N];
		
		for(int i=0;i<N;i++) {
			arr[i]=i+1;
		}
		for(int j=0;j<M;j++) {
			int a=scanner.nextInt()-1; //배열 0부터 시작
			int b=scanner.nextInt()-1;
			
			while(a<b) { //역순을 위해 while문 사용
				del=arr[a]; //이미-1 했으므로 그냥 a 대입
				arr[a++]=arr[b]; //원래 a값에 b값을 넣어주고 +1
				arr[b--]=del; //원래 b값에 del값을 넣어주고 -1
		//반복
			}
		}
		
		for(int baguni:arr)
			System.out.print(baguni+" ");
		
	}

}
