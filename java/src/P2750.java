import java.util.Arrays;
import java.util.Scanner;

public class P2750 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int[] numArr = new int[n];

        for (int i = 0; i < n; i++) {
            numArr[i] = s.nextInt();
        }
        Arrays.sort(numArr);

        for (int num : numArr) {
            System.out.println(num);
        }

        s.close();
    }
}
