import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P11659 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuffer sb = new StringBuffer();
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] numArr = new int[N];
        st = new StringTokenizer(br.readLine());
        numArr[0] = Integer.parseInt(st.nextToken());

        for (int i = 1; i < N; i++) {
            numArr[i] = Integer.parseInt(st.nextToken()) + numArr[i - 1];
        }

        for (int k = 0; k < M; k++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken()) - 2;
            int j = Integer.parseInt(st.nextToken()) - 1;

            if (i == -1) {
                sb.append(numArr[j]);
            } else {
                sb.append(numArr[j] - numArr[i]);
            }
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }
}
