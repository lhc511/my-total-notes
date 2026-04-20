function* foo() {
    //yield以上的代码为一段，有几个yield分为几段，next执行每一段代码后返回的对象自动给value和done赋值
    //并在最后一段代码执行后yield以下的代码若再次调用next函数则done置为true，value为函数返回值
    console.log('aaaaaaaaaaaa')
    const value1 = 100
    console.log(value1)
    // return 'aaa'//return在这里代码已经完全结束，下面的yield已经无效，所以调用next全部为true

    //yield中的返回值是函数中每一段执行完后函数的返回值
    yield  //在生成器中将函数中的每一段代码分隔开，将其在后续的调用中可以分段执行

    // return 'aaa' //在yield下面，第一个yield生效，所以第一个返回对象中的done属性为false。其余为true
    //return生效后的yield返回对象中的value属性是函数/return返回的值

    const value2 = 200
    console.log(value2)
    yield value2 //生成器返回的对象中的value属性的值就是 yield暂停返回的值

    const value3 = 300
    console.log(value3)
    yield

    console.log('eeeeeeeeeeeeeeeeeeee')
    // yield
    // return undefined  //此处返回后下面结果不变
    // return '123'  //{value: '123', done: true}  用返回的值作
}

const generator = foo()
console.log(generator.next())
console.log(generator.next())
console.log(generator.next())
console.log(generator.next())
// 以下为结果
/*
    aaaaaaaaaaaa
    100
    {value: undefined, done: false}
    200
    {value: undefined, done: false}
    300
    {value: undefined, done: false}
*/

