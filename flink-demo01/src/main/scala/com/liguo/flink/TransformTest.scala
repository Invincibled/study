package com.liguo.flink
import org.apache.flink.api.common.functions.{FilterFunction, ReduceFunction, RichMapFunction}
import org.apache.flink.configuration.Configuration
import org.apache.flink.streaming.api.functions.source.SourceFunction
import org.apache.flink.streaming.api.scala._
/**
  * @author liguo
  * @date 12/15/20 2:21 PM
  * @description
  */
object TransformTest {

  def main(args: Array[String]): Unit = {
    // 创建虚拟环境.
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
//    dataStream.print("---")
//    val aggStream = dataStream.keyBy(0).min(2)
//    val resultStream = dataStream.keyBy("id").reduce(new MyReduce())
//    resultStream.print()

    val splitStream  = dataStream.split(
      data => if (data.temperature > 30.0) Seq("high") else Seq("low")
    )

    val hightStream = splitStream.select("high")
    val lowStream = splitStream.select("low")
    val allStream = splitStream.select("high", "low")

//    hightStream.print()
//    lowStream.print()

    val warningStream = hightStream.map(data=>(data.id, data.temperature))
    val connectedStream = warningStream.connect(lowStream)
//
//    val colMapResultStream: DataStream[Product] = connectedStream.map(
//      warningData => (warningData._1, warningData._2, "warning"),
//      lowData =>(lowData.id,"healthy")
//    )
//    colMapResultStream.print()

    // union 相同类型的.
    val unionStream = hightStream.union(lowStream)
    unionStream.print("union")
    env.execute("transform test....")
  }
}

class  MyReduce extends ReduceFunction[SensorReading]{
  override def reduce(t1: SensorReading, t2: SensorReading): SensorReading = {
    SensorReading(t1.id, t2.timestamp, t1.temperature.min(t2.temperature))
  }
}

  // 有生命周期和运行上下文.
class MyFilter extends  RichMapFunction[SensorReading, String] {

  override def open(parameters: Configuration): Unit = {
    // 做一些初始化操作，比如链接数据库.
//    getRuntimeContext()  获取上下文,
  }

  override def map(in: SensorReading): String = in.id +" temperature"

  override def close(): Unit = {
    // 收尾工作
    // 关闭连接.
  }
}
