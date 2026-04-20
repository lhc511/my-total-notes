var obj = {
    name: "why"
}
console.log(obj.__proto__ )

// 对象里面是有一个 __ proto __ 对象:隐式原型对象

//Foo是一个函数,那么它会有一个显示原型对象:Foo.prototype
//、Foo.prototype来自哪里?
// 答案:创建了一个函数,Foo.prototype={-constructor:Foo}

//·Foo是一个对象,那么它会有一个隐式原型对象:Foo .__ proto_
//Foo .__ proto __ 来自哪里?
// new Function() . Foo .__ proto __= Function.prototype
// Function.prototype = { constructor: Function }

// var Foo =new.Function()
function Foo() {}