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

//第二段代码的执行,使用了return
//那么就意味着相当于在第一段代码的后面加上return,就会提前终止生成器函数代码继续执行
const generator = foo()
console.log(generator.next())
console.log(generator.return(10))//第二段代码不会执行，但是会将其中的value设置为返回的值
