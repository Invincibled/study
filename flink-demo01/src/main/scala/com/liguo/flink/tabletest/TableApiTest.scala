package com.liguo.flink.tabletest

import org.apache.flink.streaming.api.scala._
import org.apache.flink.table.api._
import org.apache.flink.table.api.bridge.scala._
import org.apache.flink.table.descriptors.{Csv, FileSystem, Kafka, Schema}

/**
  * @author liguo
  * @date 12/22/20 11:17 AM
  * @description
  */
object TableApiTest {

  def main(args: Array[String]): Unit = {
    val env = StreamExecutionEnvironment.getExecutionEnvironment

//    env.setParallelism(1)
//    val dataStream = stream1.map(
//      data => {
//        val arr = data.split(",")
//        SensorReading(arr(0), arr(1).toLong, arr(2).toDouble)
//      }
//    )

    //    Table.
    // 首先,创建表执行环境.dd
    val tableEnv = StreamTableEnvironment.create(env)

    /*
    // 1.1 基于老版本planner的流处理

    val  settings  = EnvironmentSettings.newInstance().useOldPlanner().inStreamingMode().build()

    val oldStreamTableEnv = StreamTableEnvironment.create(env, settings)

    // 1.2 基于老版本的批处理.
    val batchEnv = ExecutionEnvironment.getExecutionEnvironment

    val oldBatchTableEnv = BatchTableEnvironment.create(batchEnv)


    // 1.3 基于blink planner 流处理
    val blinkStreamSettings = EnvironmentSettings.newInstance().useBlinkPlanner().inStreamingMode().build()

    val blinkStreamTalbleEnv = StreamTableEnvironment.create(env, blinkStreamSettings)


    // 1.4 基于blink 批处理.

    val blinkBatchSettings = EnvironmentSettings.newInstance().useBlinkPlanner().inBatchMode().build()

    val blinkBatchTalbleEnv = TableEnvironment.create(blinkBatchSettings)

    */

    // 2 链接外部数据,读取数据，注册表,
    // 2.1 读取文件
    val path = "/Users/liguo/Downloads/workspace-web/study/flink-demo01/src/main/resources/sensor.txt"

    tableEnv.connect(new FileSystem().path(path))
      .withFormat(new Csv())
      .withSchema(new Schema().field("id",DataTypes.STRING())
                              .field("timestamp", DataTypes.BIGINT())
                              .field("temperature", DataTypes.DOUBLE()))
      .createTemporaryTable("inputTable")


    // 2.2 从kafka读取文件.

    tableEnv.connect(new Kafka()
      .version("0.11")
      .topic("sensor")
      .property("zookeeper.connect", "localhost:2181")
      .property("bootstrap.servers","localhost:9092"))
      .withFormat(new Csv())
      .withSchema(new Schema().field("id",DataTypes.STRING())
        .field("timestamp", DataTypes.BIGINT())
        .field("temperature", DataTypes.DOUBLE())).createTemporaryTable("kafkaInputTable")


    //3 查询转换
    // 3.1 使用table api
    val sensorTable = tableEnv.from("inputTable")
    val resultTable = sensorTable.select('id,'temperature).filter('id==="sensor_1")

    // 3.2 使用sql api
    val resultSqlTable = tableEnv.sqlQuery(
      """
        select id,temperature from inputTable where id='sensor_1'
      """.stripMargin)



//    val inputTable: Table = tableEnv.from("kafkaInputTable")
//
//    inputTable.toAppendStream[(String, Long, Double)].print()

    resultTable.toAppendStream[(String,Double)].print("result")

    resultSqlTable.toAppendStream[(String, Double)].print("sql")

    env.execute("table api start....")
  }
}
