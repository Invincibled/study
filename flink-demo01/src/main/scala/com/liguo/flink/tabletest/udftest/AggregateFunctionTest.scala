package com.liguo.flink.tabletest.udftest

import org.apache.flink.table.functions.AggregateFunction

/**
  * @author liguo
  * @date 12/23/20 5:38 PM
  * @description
  */
object AggregateFunctionTest {

  def main(args: Array[String]): Unit = {

  }
}


class AvgTempCC{
  var sum: Double = 0.0

  var count:Int = 0
}

class AvgTemp extends  AggregateFunction[Double, AvgTempCC]{
  override def getValue(accumulator: AvgTempCC): Double = accumulator.sum/accumulator.count

  override def createAccumulator(): AvgTempCC = new AvgTempCC

  def accumulate(accumulator: AvgTempCC, temp:Double): Unit ={
      accumulator.sum +=temp
      accumulator.count +=1
  }
}