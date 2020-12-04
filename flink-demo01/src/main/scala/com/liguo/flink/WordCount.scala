package com.liguo.flink

import org.apache.flink.api.scala.ExecutionEnvironment
import org.apache.flink.api.scala._
/**
  * @author liguo
  * @date 12/4/20 3:24 PM
  * @description
  */
object WordCount {

  def main(args: Array[String]): Unit = {
      // 创建可执行的虚拟环境.
      val env = ExecutionEnvironment.getExecutionEnvironment
      val filePath="/Users/liguo/Downloads/workspace-web/study/flink-demo01/src/main/resources/wordcount.txt"

      val inputData = env.readTextFile(filePath)

      val result = inputData.flatMap(_.split(" ")).map((_,1)).groupBy(0).sum(1)

      result.print()
  }
}
