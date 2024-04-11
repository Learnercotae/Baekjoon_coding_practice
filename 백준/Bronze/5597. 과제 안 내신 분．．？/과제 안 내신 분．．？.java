import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner=new Scanner(System.in);
		
		int arr[]=new int[30];
		
		//일단 배열로 저장한 후, 값을 받은 애들은 1로 표시 후, 0인 애들만 색출
		for(int i=0;i<28;i++) {
			int a=scanner.nextInt();
			arr[a-1]=1;
		}
		//if) 모든 배열에 각 배열에 맞게 숫자를 줌.
		for(int j=0;j<30;j++) {
			if(arr[j]==0) {
				System.out.println(j+1); //j+1을 해줌으로써 문제 해결
			}
		}
	}

}
