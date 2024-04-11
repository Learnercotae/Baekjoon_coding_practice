import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner=new Scanner(System.in);
		
		int arr[]=new int[10];
		boolean bl; //n번째와 n+1번째랑 비교하기 위한 변수
		int count=0; //서로 다른 나머지들의 개수를 측정하기 위한 변수
		
		
		for(int j=0;j<10;j++) {
			arr[j]=scanner.nextInt()%42;
		}
		//모든 배열 값들을 다 한번씩 비교해야함. 할 수는 있는데 그럼 카운트를 어케함?
		for(int c=0;c<arr.length;c++) {
			bl=false; //기본값을 false로 설정
			for(int d=c+1;d<arr.length;d++) {
				if(arr[c]==arr[d]) { //배열의 n번째와 n+1번째 값을 비교
					bl=true; //같다면 bl값을 true로 변경
					break; //한번만 비교하면 되니 조건이 성립하면 벗어나기
				}
			}
			if(bl==false) {
				count++; //bl의 값이 false일때 카운트 1증가
			} //만약 true면 나머지가 서로 같으므로 카운트 증가할 필요 x.
		}
		
		System.out.print(count);
		
	}

}