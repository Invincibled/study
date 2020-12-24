package com.liguo.flink.tabletest.udftest

import org.apache.flink.table.functions.TableFunction

/**
  * @author liguo
  * @date 12/23/20 5:11 PM
  * @description
  */
object TableFunctionTest {

  def main(args: Array[String]): Unit = {

  }
}

class Split(seperator: String) extends TableFunction[(String, Int)]{

  def eval(str:String): Unit ={
    str.split(seperator).foreach(
      word=>collect((word, word.length))
    )
  }
}
