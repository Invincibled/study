package com.liguo.flink.tabletest

import org.apache.flink.streaming.api.scala._
import org.apache.flink.table.api._
import org.apache.flink.table.api.bridge.scala._
import org.apache.flink.table.descriptors._

/**
  * @author liguo
  * @date 12/22/20 3:39 PM
  * @description
  */
object FileOutputTest {

  def main(args: Array[String]): Unit = {

    val env = StreamExecutionEnvironment.getExecutionEnvironment

    env.setParallelism(1)

    // 首先,创建表执行环境.dd
    val tableEnv = StreamTableEnvironment.create(env)

    val path = "/Users/liguo/Downloads/workspace-web/study/flink-demo01/src/main/resources/sensor.txt"

    tableEnv.connect(new FileSystem().path(path))
      .withFormat(new Csv())
      .withSchema(new Schema().field("id",DataTypes.STRING())
        .field("timestamp", DataTypes.BIGINT())
        .field("temperature", DataTypes.DOUBLE()))
      .createTemporaryTable("inputTable")

    val sensorTable = tableEnv.from("inputTable")
    // 简单转换.
    val resultTable = sensorTable.select('id,'temperature).filter('id==="sensor_1")
    // 聚合转换.
    val aggTable  = sensorTable.groupBy('id).select('id, 'id.count() as 'count) // 基于ID分组

    resultTable.toAppendStream[(String, Double)].print("result")
    aggTable.toRetractStream[(String, Long)].print()


    val path2 = "/Users/liguo/Downloads/workspace-web/study/flink-demo01/src/main/resources/sensor2.txt"

    tableEnv.connect(new FileSystem().path(path2))
      .withFormat(new Csv())
      .withSchema(new Schema().field("id",DataTypes.STRING())
        .field("timestamp", DataTypes.BIGINT())
        .field("temperature", DataTypes.DOUBLE()))
      .createTemporaryTable("outputTable")


    val result = tableEnv.from("outputTable")

    result.executeInsert("outputTable")

    env.execute("file out start.....")

  }
}
