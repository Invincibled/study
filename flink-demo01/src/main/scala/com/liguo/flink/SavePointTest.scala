package com.liguo.flink

import org.apache.flink.streaming.api.scala._

/**
  * @author liguo
  * @date 12/21/20 4:48 PM
  * @description
  */
object SavePointTest {

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
    ).uid("1")// 设置UID

    env.execute("savepoint start.....")
  }
}
