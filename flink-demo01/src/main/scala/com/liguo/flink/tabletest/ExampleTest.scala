package com.liguo.flink.tabletest

import com.liguo.flink.SensorReading
import org.apache.flink.streaming.api.scala._
import org.apache.flink.table.api.Table
import org.apache.flink.table.api.bridge.scala._

/**
  * @author liguo
  * @date 12/22/20 10:38 AM
  * @description
  */
object ExampleTest {

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

//    Table.
    // 首先,创建表执行环境.dd
    val tableEnv = StreamTableEnvironment.create(env)

    // table api
    val data  = tableEnv.fromDataStream(dataStream)
    val resultTable = data.select("id, temprature").filter("id == 'sensor_1'")

    resultTable.toAppendStream[(String, Double)].print("result")

    // sql

    tableEnv.createTemporaryView("dataTable", data)

    val sql:String = "select id temperature from dataTable wher eid='sensor_1'"
    val resultSqlTable = tableEnv.sqlQuery(sql)
    resultSqlTable.toAppendStream[(String, Double)].print("result sql")



    env.execute("table example start....")

  }
}
