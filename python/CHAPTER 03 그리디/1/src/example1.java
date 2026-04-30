import java.util.Scanner;
import java.io.IOException;

public class example1 {
  public static void main(String[] args) throws IOException {
    Scanner sc = new Scanner(System.in);
    int pay = sc.nextInt();

//    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    // br.readLine()으로 한 줄을 통째로 읽어온 뒤 int로 변환
//    int pay = Integer.parseInt(br.readLine());

    int[] coins = {500, 100, 50, 10};
    int result = 0;

    for (int coin : coins) {
      result += pay / coin;
      pay %= coin;
    }

    System.out.println(result);
  }
}
