function* foo(num) {//函数中的参数只供第一段代码执行使用，其余均由下面的next使用
    console.log("函数开始执行~")
    const value1 = 100
    console.log("第一段代码:", value1)
    //每一段next函数执行时传递的参数会由前一段的yield进行接收，再由下面的去进行调用
    try {
       yield value1
    }catch (err){
        console.log('aaaaaaa'+err)
        yield value1//若此处添加yield则该处的yield以上的代码作为第二段代码
    }
    // yield value1

    const value2 = 200
    console.log("第二段代码:", value2)
    yield value2

    const value3 = 300
    console.log("第三段代码:", value3)
    yield value3

    console.log("函数执行结束~")
}

const generator = foo()
// console. log(generator.next())
//在执行完一个next后抛出异常，会由前一个执行的next段代码中的yield进行抛错
//在抛错后如果有try catch进行捕获则继续正常执行，若没有捕获则抛错中断
// console. log(generator.throw())//与前面next的规则一样
const result = generator.next()
if (result.value !== 200) {
    console.log(generator.throw("error message"))
}
console.log(generator.next())//{value: 200, done: false}
