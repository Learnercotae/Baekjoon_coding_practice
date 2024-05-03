import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner=new Scanner(System.in);
		
		int[]arr=new int[26];
		
		//int형 배열 생성 및 모두 -1로 초기화
		//문자열 a에 각 문자의 위치를 가리킬 배열임.
		for(int i=0;i<arr.length;i++) {
			arr[i]=-1; 
		}
		
		String a=scanner.next();
		
		// A=65, a=97, 0=48
		
		for(int i=0;i<a.length();i++) {
			char ch=a.charAt(i); //charAt() => String으로 저장된 문자열 중 한 글자를 선택하여 char타입으로 변환해준다.
			
		if(arr[ch-'a']==-1) { //arr 원소 값이 -1인  경우에만 초기화
			arr[ch-'a']=i; //arr[0]=0, arr[1]=1;
		}
	}
		
		for(int val:arr) { //배열 출력
			System.out.print(val+" ");
		}
		
	}

}