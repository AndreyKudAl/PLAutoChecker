import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Task2 {
    public static void main (String[] args) {

        String filename1 = args[0];
        String filename2 = args[1];

        try {
            List<String> circle = Files.readAllLines(Paths.get(filename1), StandardCharsets.UTF_8);
            List<String> points = Files.readAllLines(Paths.get(filename2), StandardCharsets.UTF_8);

            String[] center = circle.get(0).split(" ");
            float xCircle = Float.parseFloat(center[0]);
            float yCircle = Float.parseFloat(center[1]);
            float radius = Float.parseFloat(circle.get(1));

            for (int i = 0; i < points.size(); i++) {
                String[] point = points.get(i).split(" ");
                float xPoint = Float.parseFloat(point[0]);
                float yPoint = Float.parseFloat(point[1]);
                float xLength = (Math.max(xPoint, xCircle) - Math.min(xPoint, xCircle));
                float yLength = (Math.max(yPoint, yCircle) - Math.min(yPoint, yCircle));
                float pointDistance = (float) Math.sqrt(Math.pow(xLength,2) + Math.pow(yLength,2));
                if (pointDistance == radius) System.out.println(0);
                else if (pointDistance < radius) System.out.println(1);
                else System.out.println(2);
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }


    }
}
