package com.liguo.flink

import org.apache.flink.streaming.api.functions.KeyedProcessFunction
import org.apache.flink.streaming.api.scala._
import org.apache.flink.util.Collector

/**
  * @author liguo
  * @date 12/18/20 5:24 PM
  * @description
  */
object ProcessFunctionTest {

  def main(args: Array[String]): Unit = {
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    val path = "/Users/liguo/Downloads/workspace-web/study/flink-demo01/src/main/resources/sensor.txt"
    val stream1 = env.readTextFile(path)


    val dataStream = stream1.map(
      data => {
        val arr = data.split(",")
        SensorReading(arr(0), arr(1).toLong, arr(2).toDouble)
      }
    )

    dataStream.keyBy(_.id).process(new MyKeyedProcessFunction)

    env.execute(" process function start.....")
  }
}


class MyKeyedProcessFunction extends KeyedProcessFunction[String, SensorReading, String]{
  override def processElement(value: SensorReading, ctx: KeyedProcessFunction[String, SensorReading, String]#Context, out: Collector[String]): Unit = {
    ctx.timerService().registerEventTimeTimer(ctx.timestamp() + 60000L) // 注册定时器.
    ctx.timerService().deleteEventTimeTimer(ctx.timestamp() + 60000L)  // 删除定时器.
  }

  // 定时器执行就是这一个方法，定义多个定时器，也就是这一个方法，通过if else 自己判断哪个定时器到了，执行哪个部分代码.
  override def onTimer(timestamp: Long, ctx: KeyedProcessFunction[String, SensorReading, String]#OnTimerContext, out: Collector[String]): Unit = super.onTimer(timestamp, ctx, out)
}
