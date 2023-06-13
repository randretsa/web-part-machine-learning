package services;

public class StringFormatter {
    public String csv_to_array_string(String csv){
        String[] list = csv.split(",");
        String representation = "[";

        for(int i = 0; i< list.length;i++){
            if(i==list.length-1) representation = representation + "'"+list[i]+"']";
            else representation = representation + "'"+list[i]+"',";
        }

        return  representation;
    }

    public String[] interpretPython(String pythonOutput){
        String[] list = pythonOutput.split(";");
        return list;
    }
}
