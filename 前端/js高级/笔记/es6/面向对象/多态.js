//此处严格意义上的多态，有继承有也有重写
//Shape形状
// class Shape {
//     getArea() {
//     }
// }
// class Rectangle extends Shape {
//     getArea() {
//         return 100
//     }
// }
// class Circle extends Shape {
//     getArea() {
//         return 200
//     }
// }
//
// var r = new Rectangle()
// var c = new Circle()
// //此处是对shape参数进行类型限制，只能传入Shape类型的
// //多态 :· 当对不同的数据类型执行同一个操作时,如果表现出来的行为(形态)不一样,那么就是多态的体现.
// // function calcArea (shape: Shape){//此处是ts中的写法，浏览器不支持ts
// function calcArea (shape){
//     console.log(shape.getArea())
// }
// //由于r和c继承了Shape，所以也算是Shape类型
// calcArea(r)
// calcArea(c)


//多态: js中的多态:与严格意义上的多态区别是此处没有继承也没有重写，但是
//当对不同的数据类型执行同一个操作时,如果表现出来的行为(形态)不一样,那么就是多态的体现.
function calcArea(foo) {
    console.log(foo.getArea())
}
var obj1 = {
    name: "why",
    getArea: function () {
        return 1000
    }
}
class Person{
    getArea() {
        return 100
    }
}

var p = new Person()

calcArea(obj1)
calcArea(p)