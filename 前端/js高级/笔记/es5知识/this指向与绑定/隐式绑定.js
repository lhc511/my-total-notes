// 另外一种比较常见的调用方式是通过某个对象进行调用的:
// 也就是它的调用位置中,是通过某个对象发起的函数调用。

var obj = {
    name: "why",
    eating: function () {
        console.log(this.name + "在吃东西")
    },
    running: function () {
        console.log(obj.name + "在跑步")
    }
}
// obj.eating()
//-obj.running()


var fn = obj.eating
fn()//此处由于独立调用无法访问到obj中的this，而是windows中的this

//·3.案例三:
var obj1 = {
    name: "obj1",
    foo: function () {
        console.log(this)
    }
}

var obj2 = {
    name: "obj2",
    bar: obj1.foo
}
obj2.bar()//{name: "obj2", bar: f}