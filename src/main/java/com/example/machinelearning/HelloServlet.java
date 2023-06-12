package com.example.machinelearning;

import java.io.*;

import javax.servlet.ServletContext;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import services.CommandExecutor;

@WebServlet(name = "helloServlet", value = "/hello-servlet")
public class HelloServlet extends HttpServlet {
    private String message;

    public void init() {
        message = "Hello World!";
    }

    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        response.setContentType("text/html");
        ServletContext context = getServletContext();
        String context_path = context.getRealPath("/");
        // Hello
        PrintWriter out = response.getWriter();
        CommandExecutor cmd = null;
        String script_path = context_path+"/python/Prediction.py";
        String model_path = context_path+"/python/model_saved.joblib";
        String argument = "['011', '01000', '1110110', '11', '101']";
        try{
            cmd = new CommandExecutor();
            out.print(cmd.executePythonScript(script_path,model_path,argument));

        }catch (Exception exception){
            out.print(exception.getMessage());
        }

    }

    public void destroy() {
    }
}