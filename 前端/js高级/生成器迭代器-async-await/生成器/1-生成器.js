// 生成器函数需要在function的后面加一个符号 :*   (这是一种语法规范)
//生成器本身就越是一个特殊的迭代器
function* foo() {
    console.log('aaaaaaaaaaaa')
    const value1 = 100
    console.log(value1)
    yield  //在生成器中将函数中的每一段代码分隔开，将其在后续的调用中可以分段执行

    const value2 = 200
    console.log(value2)
    yield

    const value3 = 300
    console.log(value3)
    yield
    console.log('eeeeeeeeeeeeeeeeeeee')
}

// foo()//调用生成器函数的时候不会执行该函数中的内容

// 调用生成器函数时,会给我们返回一个生成器对象
const generator = foo()  //generator就是一个生成器，可以当作迭代器来使用

//·开始执行第一段代码
generator.next()

//开始执行第二端代码
console.log('------------------')
generator.next()
generator.next()
generator.next()

