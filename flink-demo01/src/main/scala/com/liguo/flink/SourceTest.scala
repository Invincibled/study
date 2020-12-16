package com.liguo.flink

import java.util.{Properties, Random}

import org.apache.flink.api.common.serialization.SimpleStringSchema
import org.apache.flink.streaming.api.functions.source.SourceFunction
import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer

//import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment

/**
  * @author liguo
  * @date 12/14/20 2:50 PM
  * @description
  *
  *
  */

case class SensorReading(id: String, timestamp: Long, temperature: Double)

object SourceTest {

  def main(args: Array[String]): Unit = {
    // 创建虚拟环境.
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    // 从集合中读取数据.
//    val dataList = List(
//      SensorReading("sensor_1", 1607929087405L, 35.8),
//      SensorReading("sensor_5", 1607929087405L, 15.4),
//      SensorReading("sensor_7", 1607929087405L, 6.7),
//      SensorReading("sensor_10", 1607929087405L, 38.1)
//    )
//    val stream1 = env.fromCollection(dataList)
//    val path = "/Users/liguo/Downloads/workspace-web/study/flink-demo01/src/main/resources/sensor.txt"
//    val stream1 = env.readTextFile(path)
//    stream1.print()
//    val property = new Properties()
//    property.setProperty("bootstrap.servers","localhost:9092")
//    property.setProperty("group.id", "consumer-group")
//    property.setProperty("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer")
//    property.setProperty("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer")
//    property.setProperty("auto.offset.reset","latest")
//    env.addSource( new FlinkKafkaConsumer[String]("sensor", new SimpleStringSchema(), property))
    val uds: DataStream[SensorReading] = env.addSource(new MySensorSource())
    uds.print("sensor reading....")
    env.execute("source test")
  }
}

class MySensorSource() extends SourceFunction[SensorReading]{

  var running:Boolean = true

  override def run(sourceContext: SourceFunction.SourceContext[SensorReading]): Unit = {
    val random = new Random()
    // 随机生成10个传感器的初始温度.
    var curTemp = 1.to(10).map{i=>("sensor_"+i, random.nextDouble() * 100)}
    while (running){
       // 在上次基础上更新微调温度值.
       curTemp = curTemp.map{
         data => (data._1, data._2 + random.nextGaussian())
       }
       // 获取当前时间戳.
       val curTime = System.currentTimeMillis()
       curTemp.foreach(data=> sourceContext.collect(SensorReading(data._1, curTime, data._2)))

       Thread.sleep(100)
    }
  }

  override def cancel(): Unit = running = false
}