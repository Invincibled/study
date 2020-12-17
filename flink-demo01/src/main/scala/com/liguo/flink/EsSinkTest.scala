package com.liguo.flink

import java.util

import org.apache.flink.api.common.functions.RuntimeContext
import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.connectors.elasticsearch.{ElasticsearchSinkFunction, RequestIndexer}
import org.apache.flink.streaming.connectors.elasticsearch6.ElasticsearchSink
import org.apache.http.HttpHost
import org.elasticsearch.client.Requests

/**
  * @author liguo
  * @date 12/16/20 4:41 PM
  * @description
  */
object EsSinkTest {

  def main(args: Array[String]): Unit = {
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    val path = "/Users/liguo/Downloads/workspace-web/study/flink-demo01/src/main/resources/sensor.txt"
    val stream1 = env.readTextFile(path)
    env.setParallelism(1)
    val dataStream = stream1.map(
      data => {
        val arr = data.split(",")
        SensorReading(arr(0), arr(1).toLong, arr(2).toDouble)
      }
    )
    val httpHosts = new util.ArrayList[HttpHost]()
    httpHosts.add(new HttpHost("localhost", 9200))

    val esSinkFunc = new ElasticsearchSinkFunction[SensorReading] {
      override def process(t: SensorReading, runtimeContext: RuntimeContext, requestIndexer: RequestIndexer): Unit ={
            val dataSource = new util.HashMap[String, String]()
            dataSource.put("id", t.id)
            dataSource.put("temperature", t.temperature.toString)
            dataSource.put("ts", t.timestamp.toString)

            val indexRequest = Requests.indexRequest().index("sensor_index").`type`("readingdata").source(dataSource)

            requestIndexer.add(indexRequest)
      }

    }
    dataStream.addSink( new ElasticsearchSink.Builder[SensorReading](httpHosts,  esSinkFunc).build())
    env.execute("es sink start.....")
  }
}
