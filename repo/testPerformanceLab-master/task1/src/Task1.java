import java.util.ArrayList;

public class Task1 {
        public static void main (String[] args)
        {
            int n = Integer.parseInt(args[0]);
            int m = Integer.parseInt(args[1]);

            ArrayList <Integer> roundArray = new ArrayList<>();
            for (int i = 0; i < n; i++) roundArray.add(i + 1);

            int position = 0;
            int mEnd = 0;

            while (mEnd != 1) {
                System.out.print(roundArray.get(position));
                for (int i = 0; i < m; i++) {
                    if (position >= n) {
                        position = 0;
                    }
                    mEnd = roundArray.get(position);
                    if (i != (m - 1)) position++;
                }


            }
        }
    }
