import java.util.Scanner;
import java.util.Arrays; // 정렬

public class example2 {
  public static void main(String[] args){
    Scanner scanner = new Scanner(System.in);

    // nextInt()로 공백을 기준으로 숫자를 하나씩 가져옴
    int n = scanner.nextInt();
    int m = scanner.nextInt();
    int k = scanner.nextInt();

    int[] arr = new int[n]; // n개의 크기를 가진 배열 생성
    for (int i = 0; i < n; i++){
      arr[i] = scanner.nextInt();
    }
    
    Arrays.sort(arr); // 배열 오름차순 정렬
    int first = arr[n-1];
    int second = arr[n-2];
    
    // 가장 큰 수가 더해지는 횟수 계산
    int count = (m / (k + 1)) * k;
    count += m % (k + 1); // 나누어떨어지지 않고 남은 횟수만큼 가장 큰 수 추가
    
    int sum = 0;
    sum += count * first; // 가장 큰 수 더하기
    sum += (m-count) * second; // 남은 횟수만큼 두번째로 큰 수 더하기

    System.out.println(sum);
  }
}
