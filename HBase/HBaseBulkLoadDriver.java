package hbase;
import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.io.ImmutableBytesWritable;
import org.apache.hadoop.hbase.mapreduce.HFileOutputFormat;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

import java.util.logging.Level;
import java.util.logging.Logger;
@SuppressWarnings("deprecation")
public class HBaseBulkLoadDriver extends Configured implements Tool {	
    private static final String DATA_SEPERATOR = ",";	
    private static final String TABLE_NAME = "user";	
    private static final String COLUMN_FAMILY_1="personalDetails";	
    private static final String COLUMN_FAMILY_2="contactDetails";	
    /**
     * HBase bulk import example
     * Data preparation MapReduce job driver
     * 
     * args[0]: HDFS input path
     * args[1]: HDFS output path
     * 
     */
    public static void main(String[] args) {		
         try {
            int response = ToolRunner.run(HBaseConfiguration.create(), new HBaseBulkLoadDriver(), args);
            //Logger.getRootLogger().=DEBUG, DebugAppender; 
            //Logger.getRootLogger().setLevel(Level.OFF);
            if(response == 0) {				
                System.out.println("Job is successfully completed...");
            } else {
                System.out.println("Job failed...");
            }
        } catch(Exception exception) {
            exception.printStackTrace();
        } 
         
    }

    @Override
    public int run(String[] args) throws Exception {
        int result=0;
        String outputPath = args[1];		
        Configuration configuration = getConf();
        //Configuration configuration =HBaseConfiguration.create();
        //configuration.set("hbase.zookeeper.quorum","brilliohdpm.brilliohdp.brillio.com,brilliohdpw1.brilliohdp.brillio.com,brilliohdpw2.brilliohdp.brillio.com");
        configuration.set("hbase.zookeeper.quorum","zookeeper0.brilliohdinsight.g1.internal.cloudapp.net,zookeeper1.brilliohdinsight.g1.internal.cloudapp.net,zookeeper2.brilliohdinsight.g1.internal.cloudapp.net");
        configuration.set("zookeeper.znode.parent", "/hbase");
        //configuration.set("hbase.master","brilliohdpm.brilliohdp.brillio.com:60000");
        configuration.set("hbase.master","zookeeper1.brilliohdinsight.g1.internal.cloudapp.net:60000");
        configuration.set("hbase.zookeeper.property.clientPort", "2181");
        configuration.set("data.seperator", DATA_SEPERATOR);		
        configuration.set("hbase.table.name",TABLE_NAME);		
        configuration.set("COLUMN_FAMILY_1",COLUMN_FAMILY_1);		
        configuration.set("COLUMN_FAMILY_2",COLUMN_FAMILY_2);		
        Job job = Job.getInstance(configuration);		
        job.setJarByClass(HBaseBulkLoadDriver.class);		
        job.setJobName("Bulk Loading HBase Table::"+TABLE_NAME);		
        job.setInputFormatClass(TextInputFormat.class);		
        job.setMapOutputKeyClass(ImmutableBytesWritable.class);		
        job.setMapperClass(HBaseBulkLoadMapper.class);		
        FileInputFormat.addInputPaths(job, args[0]);		
        FileSystem.getLocal(getConf()).delete(new Path(outputPath), true);		
        FileOutputFormat.setOutputPath(job, new Path(outputPath));		
        job.setMapOutputValueClass(Put.class);		
        HFileOutputFormat.configureIncrementalLoad(job, new HTable(configuration,TABLE_NAME));		
        job.waitForCompletion(true);		
        if (job.isSuccessful()) {
           LoadIncrementalHFiles loader = new LoadIncrementalHFiles(configuration);
           loader.doBulkLoad(new Path(outputPath),new HTable(configuration,TABLE_NAME));
        } else {
            result = -1;
        }
        return result;
    }
}
