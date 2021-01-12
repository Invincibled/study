package com.liguo.flink.tabletest.udftest

import org.apache.flink.table.functions.TableAggregateFunction
import org.apache.flink.util.Collector

/**
  * @author liguo
  * @date 12/23/20 6:10 PM
  * @description
  */
object TableAggregateFunctionTest {

  def main(args: Array[String]): Unit = {

  }
}

class Top2Acc{
  var highestTemp: Double = Double.MinValue

  var secondHestTemp: Double = Double.MinValue


}

class Top2Temp extends TableAggregateFunction[(Double, Int), Top2Acc]{
  override def createAccumulator(): Top2Acc = new Top2Acc()

  def emitValue(accumulator: Top2Acc, out: Collector[(Double, Int)]): Unit = {
    out.collect((accumulator.highestTemp, 1 ))
    out.collect((accumulator.secondHestTemp, 2 ))
  }


  def accumulate(accumulator: Top2Acc, temp:Double): Unit ={

    if (temp>accumulator.highestTemp){
      accumulator.secondHestTemp = accumulator.highestTemp
      accumulator.highestTemp = temp
    }else if(temp>accumulator.secondHestTemp){
      accumulator.secondHestTemp = temp
    }
  }

}
