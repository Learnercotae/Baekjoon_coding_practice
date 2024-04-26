import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner=new Scanner(System.in);
		
		int a=scanner.nextInt();
		//공백 없이 출력이면.. 공백을 강제로 없애나?
		String b=scanner.next();
		
		int sum=0;
		
		for(int i=0 ;i<a;i++) {
			sum+=b.charAt(i)-'0'; //charAt()은 해당 문자의 아스키코드값을 반환하므로 반드시 -48 or-'0'을 해주어야 입력받은 숫자 값 그대로 사용 가능하다.
		}
		System.out.print(sum);
		
		
	}

}
