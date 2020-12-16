package com.liguo.flink

import org.apache.flink.streaming.api.scala._
/**
  * @author liguo
  * @date 12/16/20 3:47 PM
  * @description
  */
object KafkaSinkTest {
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

    dataStream.addSink(Flinkk)
    env.execute("kafka sink start.....")
  }
}
