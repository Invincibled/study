package com.liguo.flink

import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.connectors.elasticsearch.ElasticsearchSinkBase

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

//    dataStream.addSink(new ElasticsearchSinkBase[]() {})

    env.execute("es sink start.....")
  }
}
