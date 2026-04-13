import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int result = Integer.MIN_VALUE; // 각 행 최솟값들 중 최댓값

        for (int i=0; i<n; i++) {
            int rowMin = Integer.MAX_VALUE; // 현재 행의 최솟값

            for (int j=0; j<m; j++){
                int num = sc.nextInt();
                rowMin = Math.min(rowMin, num); // 현재 행에서 가장 작은 수 갱신
            }
            
            result = Math.max(result, rowMin); // 행의 최솟값들 중 가장 큰 수 갱신
        }

        System.out.println(result);
    }
}