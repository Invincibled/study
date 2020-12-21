package com.liguo.flink

import org.apache.flink.api.common.restartstrategy.RestartStrategies
import org.apache.flink.runtime.executiongraph.restart.RestartStrategy
import org.apache.flink.streaming.api.CheckpointingMode
import org.apache.flink.streaming.api.scala._
/**
  * @author liguo
  * @date 12/21/20 4:05 PM
  * @description
  */
object CheckPointTest {

  def main(args: Array[String]): Unit = {
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    val path = "/Users/liguo/Downloads/workspace-web/study/flink-demo01/src/main/resources/sensor.txt"
    val stream1 = env.readTextFile(path)
    env.setParallelism(1)

    // 启用checkpoint.
    env.enableCheckpointing(1000L)
    env.getCheckpointConfig.setCheckpointingMode(CheckpointingMode.AT_LEAST_ONCE)
    env.getCheckpointConfig.setCheckpointTimeout(60000L)
    env.getCheckpointConfig.setMaxConcurrentCheckpoints(2)
    env.getCheckpointConfig.setMinPauseBetweenCheckpoints(100L)
    env.getCheckpointConfig.setPreferCheckpointForRecovery(true)

    env.setRestartStrategy(RestartStrategies.fixedDelayRestart(3, 1000L))

    val dataStream = stream1.map(
      data => {
        val arr = data.split(",")
        SensorReading(arr(0), arr(1).toLong, arr(2).toDouble)
      }
    )

    env.execute("checkpoint start.....")
  }
}
