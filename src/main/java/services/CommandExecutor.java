package services;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class CommandExecutor {
    public String executePythonScript(String scriptPath, String modelPath, String argument) throws IOException {
        List<String> command = new ArrayList<String>();
        command.add("py");
        command.add(scriptPath);
        command.add(modelPath);
        command.add(argument);
        // Create the process builder
        ProcessBuilder processBuilder = new ProcessBuilder(command);

        // Redirect the error stream to the standard output
        processBuilder.redirectErrorStream(true);

        // Start the process
        Process process = processBuilder.start();

        // Read the output from the process
        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        StringBuilder output = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            output.append(line).append("\n");
        }

        // Wait for the process to finish
        try {
            process.waitFor();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        return output.toString();
    }
}
