import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner=new Scanner(System.in);
		
		double arr[]=new double[scanner.nextInt()]; //배열 선언과 동시에 배열 크기 값을 받음
		double sum=0;
		
		for(int i=0;i<arr.length;i++) {
			arr[i]=scanner.nextDouble(); //점수 값을 저장
		}
		
		Arrays.sort(arr); //배열 정렬
		
		for(int c=0;c<arr.length;c++) {
			sum+=(arr[c]/arr[arr.length-1])*100;
		}
		
		System.out.print(sum/arr.length);
		
	}

}
