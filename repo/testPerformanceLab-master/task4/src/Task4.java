import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Task4 {
    public static void main (String[] args) {
        String filename1 = args[0];

        try {
            List<String> data = Files.readAllLines(Paths.get(filename1), StandardCharsets.UTF_8);
            int [] nums = new int [data.size()];
            int sum = 0;
            int turns = 0;

            for (String s : data) {
                nums [data.indexOf(s)] = Integer.parseInt(s);
                sum += nums[data.indexOf(s)];
            }
            int average = sum/data.size();

            for (int n : nums) {
                turns += (Math.abs (average - n));
            }

            System.out.println(turns);


        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
