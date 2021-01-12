package com.liguo.flink

import java.sql.{Connection, Driver, DriverManager, PreparedStatement}

import org.apache.flink.configuration.Configuration
import org.apache.flink.streaming.api.functions.sink.{RichSinkFunction, SinkFunction}
import org.apache.flink.streaming.api.scala._

/**
  * @author liguo
  * @date 12/17/20 3:38 PM
  * @description
  */
object MysqlSinkTest {

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

    dataStream.addSink(new MysqlFunc)

    env.execute("mysql sink.....")

  }
}

class MysqlFunc extends  RichSinkFunction[SensorReading]{

  var conn: Connection = _

  var insertStmt: PreparedStatement = _

  var updateStmt: PreparedStatement = _

  override def open(parameters: Configuration): Unit = {

      conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "123456")
      insertStmt  = conn.prepareStatement("insert into sensor_temp(id,temp) values(?,?)")
      updateStmt = conn.prepareStatement("update sensor_temp set temp = ? where id = ?")
  }

  override def close(): Unit = {
    insertStmt.close()
    updateStmt.close()
    conn.close()
  }

  override def invoke(value: SensorReading, context: SinkFunction.Context[_]): Unit = {
    updateStmt.setDouble(1, value.temperature)
    updateStmt.setString(2, value.id)
    updateStmt.execute()

    insertStmt.setString(1, value.id)
    insertStmt.setString(2, value.temperature.toString)

    insertStmt.execute()
  }
}
