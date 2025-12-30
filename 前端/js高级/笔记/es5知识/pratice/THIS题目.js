/////////////////////////////////////////
// var name = "window";
//
// var person = {
// name: "person",
// sayName: function () {
//     console.log(this.name);
// }}
//
// function sayName (){
//     var sss = person. sayName;
//     sss();// window :· 独立函数调用
//     person.sayName();// person: 隐式调用
//     (person.sayName)();//-person :· 隐式调用 相当于直接调用person.sayName()
//     (b=person.sayName)();//·window :· 赋值表达式(独立函数调用)
// }
// sayName ();
////////////////////////////////////////////////////////////////////
// var name = 'window'
//
// var person1 = { //此处只是定义了一个对象，并未产生作用域，因此foo2函数this指向的作用域是父级作用域window
//     name: 'person1',
//     fool: function () {
//         console.log(this.name)
//     },
//     foo2: ()=> console.log(this.name),
//
//     foo3: function () {
//             return function () {
//             console.log(this.name)
//         }
//     },
//
//     foo4: function () {
//         return () => {
//             console.log(this.name)
//         }
//     }
// }
// var person2 = { name: 'person2' }

//person1.foo1();// person1(隐式绑定)
//person1.foo1.call(person2) ;· // person2(显示绑定优先级大于隐式绑定)

//对返回的箭头函数进行调用，该箭头函数的父级作用域是全局
//person1.foo2();//window(不绑定作用域,上层作用域是全局)
// person1.foo2.call(person2); // window

//对person1的foo3的值(函数) 进行调用 得到一个函数，再对普通函数进行调用，因此为独立调用
//person1.foo3()(); // window(独立函数调用)
//person1.foo3.call(person2)();//·window(独立函数调用)

//person1.foo3的对应的值(函数)执行后 的返回值 绑定person2
//person1.foo3().call(person2);//person2(最终调用返回函数式,使用的是显示绑定)

//foo4中的this指向的是他的父级作用域,即父函数绑定的对象
//因为独立执行的函数的this指向才是windows，而箭头函数中的this指向其父作用域，而该箭头函数的父作用域做隐式调用，所以为person1
// person1.foo4()();//person1(箭头函数不绑定this,上层作用域this是person1)
// //foo4属性的值(函数)绑定person2并执行，再执行其返回值，由于箭头函数this指向父作用域，而其父级函数绑定person2，因此为person2
// person1.foo4.call(person2)();//person2(上层作用域被显示的绑定了-个person2)
// //foo4的值(函数)执行后的 返回值(箭头函数) 绑定person2 并执行，箭头函数指向被 隐式绑定 的父函数
// person1.foo4().call(person2);//person1(上层找到person1)

//*******************************************************************

// var name = 'window'
//
// function Person (name) {
//     this.name = name
//     this.foo1 = function () {
//         console.log(this.name)
//     },
//     this.foo2 = ()=>console.log(this.name),
//     this.foo3 = function () {
//         return function () {
//             console.log(this.name)
//         }
//     },
//
//     this.foo4 = function () {
//         return () => {
//             console.log(this.name)
//         }
//     }
// }
// var person1 = new Person('person1')
// var person2 = new Person('person2')

//person1对foo1调用的隐式绑定
// person1.foo1() //person1
// person1对foo1隐式绑定，然后再对foo1显式绑定再调用和
//person1.foo1.call(person2)//person2(显示高于隐式绑定)

// foo2的父作用域对应构造函数person
// person1对foo2进行隐式绑定，但this指向父作用域，因此指向person1
//person1.foo2()//person1(上层作用域中的this是person1)
// person1.foo2.call(person2)//person1(上层作用域中的this是person1)

// person1.foo3()的执行结果(函数)进行调用，因此为函数独立调用
// person1.foo3() ()//·window(独立函数调用)
// 前面表示对foo3先隐式绑定person1再显式绑定person2再执行，由于返回值是一个函数，最后再进行调用，所以独立函数调用
//person1.foo3.call(person2) ()// window
//对person1.foo3()的返回值(函数，非箭头函数)进行 显式绑定person2 再调用
// person1. foo3().call(person2) //person2

// 其中箭头函数的父作用域对应foo4的值函数
//person1对属性foo4的函数隐式绑定，执行后再执行返回的值(箭头函数)，箭头函数指向父作用域
// person1.foo4()()//person1
//person1调用foo4再把foo4显式绑定person2 得到函数执行返回值(也是函数)，在执行得到的返回值
//而返回值是箭头函数，所以this指向其父级作用域，即foo4属性的值(箭头函数父函数)，foo4已显式绑定person2
// person1.foo4.call(person2)() // person2
//person1隐式绑定foo4的值 得到foo4的值(函数)执行后的结果(箭头函数),将结果(箭头函数)绑定person2，this只指向父作用域，因此为person1
// person1.foo4().call(person2) // person1

//*************************************************************************

var name = 'window'
function Person (name) {
    this.name = name
    this.obj = {
        name: 'obj',
        fool: function () {
            return function () {
                console.log(this.name)
            }
        },
        foo2: function () {
            return () => {
                console.log(this.name)
            }
        }
    }
}
var person1 = new Person('person1')
var person2 = new Person('person2')

person1.obj.fool()()// window
person1.obj.fool.call(person2)() // window
person1.obj.fool().call(person2) //person2

//由于是obj调用foo2中的函数，箭头函数中this指向父作用域，所以是obj
person1.obj.foo2()()//obj
//给obj的foo2显式绑定person2
person1.obj.foo2.call(person2)() //person2
// 给箭头函数显式绑定person2，但是没用，依旧指向父作用域
person1.obj.foo2().call(person2) // obj