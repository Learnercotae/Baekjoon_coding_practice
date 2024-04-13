import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner=new Scanner(System.in);
		
		
		String a=scanner.next();
		int n=scanner.nextInt()-1; 
		//charAt()함수를 사용할 것이므로 -1을 미리 해줌.
		
		System.out.print(a.charAt(n));
		//charAt() 함수를 사용하여 출력
	}

}
