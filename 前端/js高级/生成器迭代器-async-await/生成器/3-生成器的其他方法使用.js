function* foo(num) {//函数中的参数只供第一段代码执行使用，其余均由下面的next使用
    console.log("函数开始执行~")
    const value1 = 100
    console.log("第一段代码:", value1)
    //每一段next函数执行时传递的参数会由前一段的yield进行接收，再由下面的去进行调用
    const n=yield value1

    const value2 = 200*n
    console.log("第二段代码:", value2)
    yield value2

    const value3 = 300
    console.log("第三段代码:", value3)
    yield value3

    console.log("函数执行结束~")
    return "123"
}


//生成器next方法传递参数
const generator = foo(5)
console.log(generator.next())
//第二段代码,第二次调用next的时候执行的
console.log(generator.next(10))