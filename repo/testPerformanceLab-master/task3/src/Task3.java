import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.List;

public class Task3 {
    public static void main (String[] args) {
        String filename1 = args[0];
        String filename2 = args[1];

        try {
            List<String> tests = Files.readAllLines(Paths.get(filename1), StandardCharsets.UTF_8);
            List<String> values = Files.readAllLines(Paths.get(filename2), StandardCharsets.UTF_8);

            for (int i = 0; i < values.size(); i++) {

                if (values.get(i).contains("id")) {
                    rewriter(values.get(i), values.get(i + 1), tests);
                }
            }

            Files.write(Paths.get(filename1), tests, StandardOpenOption.CREATE);

        } catch (IOException e) {
            e.printStackTrace();
        }


    }
    public static void rewriter (String id, String value, List<String> list) {
        for (int i = 0; i < list.size(); i++) {
            int startIndex = value.indexOf(":");
            int endIndex = value.lastIndexOf("\"");
            String replacement = value.substring(startIndex, endIndex + 1);

            if (list.get(i).contains(id)) {
                int startIndexReplace = list.get(i + 2).indexOf(":");
                int endIndexReplace = list.get(i + 2).lastIndexOf("\"");
                String toBeReplace = list.get(i + 2).substring(startIndexReplace, endIndexReplace + 1);
                String replaced = list.get(i + 2).replace(toBeReplace, replacement);
                list.set((i + 2), replaced);
            }
        }
    }


}
