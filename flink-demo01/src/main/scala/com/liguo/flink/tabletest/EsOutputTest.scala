package com.liguo.flink.tabletest
import org.apache.flink.streaming.api.scala._
import org.apache.flink.table.api._
import org.apache.flink.table.api.bridge.scala._
import org.apache.flink.table.descriptors._
/**
  * @author liguo
  * @date 12/22/20 5:40 PM
  * @description
  */
object EsOutputTest {

  def main(args: Array[String]): Unit = {
    val env = StreamExecutionEnvironment.getExecutionEnvironment

    env.setParallelism(1)

    // 首先,创建表执行环境.dd
    val tableEnv = StreamTableEnvironment.create(env)

    // 输入.
    tableEnv.connect(new Kafka()
      .version("0.11")
      .topic("sensor")
      .property("zookeeper.connect", "localhost:2181")
      .property("bootstrap.servers","localhost:9092"))
      .withFormat(new Csv())
      .withSchema(new Schema().field("id",DataTypes.STRING())
        .field("timestamp", DataTypes.BIGINT())
        .field("temperature", DataTypes.DOUBLE())).createTemporaryTable("kafkaInputTable")


    val sensorTable = tableEnv.from("kafkaInputTable")

    // 简单转换
    val resultTable = sensorTable.select('id,'temperature).filter('id==="sensor_1")

    // 聚合转换.
    val aggTable  = sensorTable.groupBy('id).select('id, 'id.count() as 'count) // 基于ID分组


    // 输出
    tableEnv.connect( new Elasticsearch().version("6")
    .host("locahost", 9092 ,"http").documentType("temperature")).inUpsertMode()
      .withFormat(new Json()).withSchema(new Schema().field("id",DataTypes.STRING())
      .field("count", DataTypes.BIGINT())).createTemporaryTable("esOutputTable")

    aggTable.insertInto("esOutputTable")

    env.execute("es pipeline start....")
  }
}
