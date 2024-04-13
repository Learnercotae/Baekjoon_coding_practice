import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner=new Scanner(System.in);
		
		int n=scanner.nextInt();
		String arr[]=new String[n];
		
		for(int i=0;i<arr.length;i++) {
			arr[i]=scanner.next(); //문자열 입력받기
		}
		
		for(int j=0;j<arr.length;j++) {
			if(arr[j].length()<1) { //문자열의 길이가 한자리라면
				System.out.println(arr[j]+""+arr[j]); //같은 문자열 출력
			}
			else {
				System.out.print(arr[j].substring(0,1)); //0번쨰 출력
			}
			System.out.println(arr[j].substring(arr[j].length()-1,arr[j].length()));
			//마지막 문자 출력
		}
		
	}

}