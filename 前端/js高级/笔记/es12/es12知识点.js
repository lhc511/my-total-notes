// ES12: FinalizationRegistry类，该类创建的对象中监控目标对象在销毁后触发执行代码，但不会立即执行，因为GC不定期扫描回收
// const finalRegistry = new FinalizationRegistry((value) => {//value是传递的值
//     console.log("注册在finalRegistry的对象,某一个被销毁",value)
// })
// let obj = { name: "why" }
// let info=new WeakRef(obj) //对obj进行弱引用，obj在销毁一并销毁
// //在注册的时候可以传递一个值(第二个参数)
// finalRegistry.register(obj,'aaa')
//
// // console.log(info.deref().name)//通过deref来访问弱引用中的对象以此访问属性
// obj = null
//
// setTimeout(() => {//原因是此时obj已经被销毁，弱引用也指向失效所以undefined报错
//     console.log(info.deref().name)// Cannot read properties of undefined (reading 'name')
// }, 5000)

// ES12 - logical assignment operators逻辑运算符
//1.逻辑或运算符
// let message = ""  //以下两个效果一样
// // message =message || "hello world"
// message ||= "Hello World"
// console.log(message)
//
// //·2.逻辑与操作符  如果前面存在，就执行后面的代码
// let obj = {
//     name: "why"
// }
//
// // obj = obj && obj.foo()//如果obj存在，就执行后面的函数
// obj &&= obj.name
// console.log(obj)
//
// //3.逻辑空运算符
// let foo = null
// // foo =foo?? "默认值"
// foo ??= "默认值"
// console.log(foo)

// StringreplaceAll:字符串替换;