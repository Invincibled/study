package com.liguo.flink
import org.apache.flink.api.common.functions.{RichFlatMapFunction, RichMapFunction}
import org.apache.flink.api.common.state._
import org.apache.flink.configuration._
import org.apache.flink.streaming.api.scala._
import org.apache.flink.util.Collector

/**
  * @author liguo
  * @date 12/18/20 4:20 PM
  * @description
  */
object StateTest {

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
    // 对于温度传感器，温度跳变超过10度进行报警.
    //    val alertStream = dataStream.keyBy(_.id).flatMap(new TempChangeAlert(10.0))
    val alertStream = dataStream.keyBy(_.id).flatMapWithState {
      case (data: SensorReading, None) => (List.empty, Some(data.temperature))
      case (data: SensorReading, lastTemp: Some[Double]) => {
        val diff = (data.temperature - lastTemp.get).abs

        if (diff > 10.0) {
          (List((data.id, lastTemp.get, data.temperature)), Some(data.temperature))
        }
        else {
          (List.empty, Some(data.temperature))
        }
      }
    }


    alertStream.print()

    env.execute(" state start.....")
  }
