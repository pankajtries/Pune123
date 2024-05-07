/*
If Hadoop is already installed on your system, you can follow these steps to run the WordCount program:

1. **Prepare Input Data**:
   - Create input text files containing the data you want to analyze. You can create a directory for your input files and place them there.

2. **Compile the Java Code**:
   - Compile your WordCount Java code into a JAR file. Assuming your Java code is in a file named `WordCount.java`, you can compile it using the `javac` command:
     ```bash
     javac -classpath $(hadoop classpath) WordCount.java
     ```

3. **Package the Compiled Classes into a JAR**:
   - Package the compiled classes into a JAR file. You can use the `jar` command:
     ```bash
     jar cvf WordCount.jar *.class
     ```

4. **Create Input and Output Directories in HDFS**:
   - Before running the program, create input and output directories in HDFS (Hadoop Distributed File System) using the following commands:
     ```bash
     hdfs dfs -mkdir -p /input
     hdfs dfs -mkdir -p /output
     ```

5. **Upload Input Data to HDFS**:
   - Upload your input text files to the input directory in HDFS:
     ```bash
     hdfs dfs -put /path/to/input/* /input
     ```

6. **Run the WordCount Program**:
   - Run the WordCount program using the `hadoop jar` command, providing the input and output directories as arguments:
     ```bash
     hadoop jar WordCount.jar WordCount /input /output
     ```

7. **View Output**:
   - Once the program completes successfully, you can view the output by reading the contents of the output directory in HDFS:
     ```bash
     hdfs dfs -cat /output/*
     ```

These steps assume that Hadoop is already installed and configured properly on your system. Adjust the paths and commands as necessary based on your specific Hadoop setup and requirements.



 */





import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {
 public static void main(String[] args) throws Exception {
   Configuration conf = new Configuration();
   Job job = Job.getInstance(conf, "word count");
   job.setJarByClass(WordCount.class);
   job.setMapperClass(WordCountMapper.class);
   job.setCombinerClass(WordCountReducer.class);
   job.setReducerClass(WordCountReducer.class);
   job.setOutputKeyClass(Text.class);
   job.setOutputValueClass(IntWritable.class);
   FileInputFormat.addInputPath(job, new Path(args[0]));
   FileOutputFormat.setOutputPath(job, new Path(args[1]));
   System.exit(job.waitForCompletion(true) ? 0 : 1); }
 
 public static class WordCountMapper extends Mapper<Object, Text, Text, IntWritable> {
  private final static IntWritable one = new IntWritable(1);
  private Text word = new Text();
  public void map(Object key, Text value, Context context) throws IOException,
  InterruptedException {
   StringTokenizer itr = new StringTokenizer(value.toString());
   while (itr.hasMoreTokens()) {
    word.set(itr.nextToken());
    context.write(word, one);
   }
  }
 }
 
 public static class WordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
  private IntWritable result = new IntWritable();
  public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
   int sum = 0;
   for (IntWritable val : values) {
    sum += val.get();
   }
   result.set(sum);
   context.write(key, result);
  }
 }
}
