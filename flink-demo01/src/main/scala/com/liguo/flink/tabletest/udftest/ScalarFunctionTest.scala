package com.liguo.flink.tabletest.udftest

import org.apache.flink.table.functions.ScalarFunction

/**
  * @author liguo
  * @date 12/23/20 4:53 PM
  * @description
  */
object ScalarFunctionTest {
  def main(args: Array[String]): Unit = {

  }
}

class HashCode(factor: Int) extends ScalarFunction{

  def eval(s: String) : Int ={

    s.hashCode * factor - 10000
  }

}
