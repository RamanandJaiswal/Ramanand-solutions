  #
 

"""
author- Ramanand jaiswal
 Parse Tweets from  from Kafka in every 10 seconds.
 Usage: direct_kafka_sstreaming.py  

 To run this on your local machine, you need to setup Kafka and create a producer first, see
 http://kafka.apache.org/documentation.html#quickstart

 and then run the example
    `$ bin/spark-submit --jars external/kafka-assembly/target/scala-*/\
      spark-streaming-kafka-assembly-*.jar \
      examples/src/main/python/streaming/direct_kafka_wordcount.py \
      localhost:9092 test`
"""
import re
import ConfigParser
import sys
import json
import os
from pyspark import SQLContext
from pyspark.sql import SQLContext, Row
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import time
os.environ["SPARK_HOME"] = "/usr/hdp/2.3.3.1-7/spark"

 
def processTweet(tweet):
    rest_tweets=tweet[1:]
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet[0])
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    tweet=tuple([tweet])+rest_tweets
    return tweet
	   
        


if __name__ == "__main__":
	
    sc = SparkContext(appName="PythonStreamingDirectFromTwitter")
    ssc = StreamingContext(sc, 10)
    sql=SQLContext(sc)

    #brokers, topic,hdfsPath = sys.argv[1:]
    #reading inputs from properties file
    brokers=""
    topic=""
    hdfsPath=""
    config = ConfigParser.RawConfigParser()
    config.read("twitter_kafka_realtime_ingestion.properties")
    brokers=config.get('TwitterKeys','kafka-broker');
    topic=config.get('TwitterKeys','topic');
    hdfsPath=config.get('TwitterKeys','Blob-path');
    print brokers
    print topic
    print hdfsPath
    kvs = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list":brokers})
    df=kvs.map(lambda (k, v): json.loads(v))
    try:
        
    	parsed=df.map(lambda x :(x['text'].encode('ascii','ignore'),x['id'],x['user']['name'],x['created_at'],x['source'],x['truncated'],x['in_reply_to_status_id'],x['in_reply_to_user_id'],x['favorited'],x['retweeted'],x['user']['favourites_count'],x['geo'],x['coordinates'],x['place'],x['user']['location'],x['retweet_count'],x['possibly_sensitive'],x['lang']))
    	parsed.pprint()
	    cleaned_rdd=parsed.map(processTweet)
      cleaned_rdd.pprint()
      cleaned_rdd.saveAsTextFiles(hdfsPath +str(int(round(time.time() * 1000))))
	    print('written to hdfs file....')
    	 
    except BaseException, e:
	    print 'failed on_data,', str(e)
	    pass
    
     
    ssc.start()
    ssc.awaitTermination()
