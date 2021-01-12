package com.liguo.flink

import org.apache.flink.api.common.serialization.SimpleStringEncoder
import org.apache.flink.core.fs.Path
import org.apache.flink.streaming.api.functions.sink.filesystem.StreamingFileSink
import org.apache.flink.streaming.api.scala._


/**
  * @author liguo
  * @date 12/16/20 3:35 PM
  * @description
  */
object FileSinkTest {

  def main(args: Array[String]): Unit = {
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    val path = "/Users/liguo/Downloads/workspace-web/study/flink-demo01/src/main/resources/sensor.txt"
    val stream1 = env.readTextFile(path)
    env.setParallelism(1)
    val dataStream = stream1.map(
      data=>{
        val arr = data.split(",")
        SensorReading(arr(0), arr(1).toLong, arr(2).toDouble)
      }
    )

//    dataStream.writeAsCsv("/Users/liguo/Downloads/workspace-web/study/flink-demo01/src/main/resources/file_sink.csv")

    dataStream.addSink(StreamingFileSink.forRowFormat(
      new Path("/Users/liguo/Downloads/workspace-web/study/flink-demo01/src/main/resources/file_sink.csv"),
      new SimpleStringEncoder[SensorReading]()
    ).build())

    env.execute("start ....")
  }
}
