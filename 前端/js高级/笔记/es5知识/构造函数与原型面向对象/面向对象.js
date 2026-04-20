// 创建一个对象,对某一个人进行抽象(描述)
//1.创建方式一:通过new Object()创建
// var obj = new Object()
// obj.name = "why"
// obj.age = 18
// obj.height = 1.88
// obj.running = function() {
//     console.log(this.name + "跑步~")
// }
// //2.创建方式二:字面量形式
// var info = {
//     name: "kobe",
//     age: 40,
//     height: 1.98,
//     eating: function () {
//         console.log(this.name + "在吃东西~")
//     },
// }

// 创建方式3 工厂模式    (不推荐)
// function createDog(){
//     var p = {}
//     return p
// }
// function createPerson(name, age, height, address){
//     var p = {}
//     p.name = name
//     p.age = age
//     p.height = height;
//     p.address = address
//
//     p.eating = function() {
//         console.log(this.name + "在吃东西~")
//     }
//     p.running = function () {
//         console.log(this.name + "在跑步~")
//     }
//     return p
// }
//
// var p1 = createPerson("张三”,18,1.88,“广州市")
// var p2 =createPerson("李四”,20,1.98,“上海市")
// // 工厂模式的缺点(获取不到对象最真实的类型)都只能知道是obj类型，没有具体分类，定位太宽泛
// //比如上面的createDog和createPerson都只按照对象类型分类，但却是创建人和狗两个不同的功能
// console.log(p1, p2)




// //操作对象
// var obj = {
//     name: "why",
//     age: 1,
// }
//
// // 获取属性
// console. log(obj.name)
//
// // 给属性赋值
// obj.name = "kobe"
// console.log(obj.name)
//
// //·删除属性
// delete obj.name
// console.log(obj)

// 需求:对属性进行操作时,进行一些限制
//、限制 :· 不允许某一个属性被赋值

// var obj = {
//     name: "why",
//     age: 18
// }
//
// //属性描述符是一个对象
// Object.defineProperty(obj, "height", {
//     //很多的配置
//     value: 1.88
// })
//
// //无法在控制台中打印出添加的属性(其实已经添加进去)，但是可以通过 . 来访问该属性的值
// console.log(obj)//obj = {name: "why", age: 18}
// console.log(obj.height)//1.88