package com.liguo.flink

import org.apache.flink.api.java.utils.ParameterTool
import org.apache.flink.streaming.api.scala._
/**
  * @author liguo
  * @date 12/4/20 3:45 PM
  * @description
  */
object StreamWordCount {
  def main(args: Array[String]): Unit = {
    val env = StreamExecutionEnvironment.getExecutionEnvironment

    val paramTool = ParameterTool.fromArgs(args)
    val host:String = paramTool.get("host")
    val port:Int = paramTool.get("port").toInt

    val inputData:DataStream[String] = env.socketTextStream(host, port)

    val result = inputData.flatMap(_.split(" ")).filter(_.nonEmpty).map((_,1)).keyBy(0).sum(1)

    result.print()

    env.execute("stream word count")


  }
}
