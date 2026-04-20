//、高阶函数在使用时,·也可以传入箭头函数
var nums = [10, 20, 45, 78]
nums. forEach((item, index, arr) =>{})

//箭头函数有一些常见的简写:
//-简写一;如果参数只有一个,()可以省略
nums. forEach(item => {console.log(item)})

//简写二:如果函数执行体只有一行代码,那么{}也可以省略
//·强调:并且它会默认将这行代码的执行结果作为返回值
nums.forEach(item => console.log(item))
var newNums = nums. filter(item => item % 2 === 0)
console.log(newNums)

// filter/map/reduce      先过滤偶数，将过滤后得到的数组中所有元素*100，最后累加所有元素
var result = nums. filter(item => item % 2 === 0)
            .map(item => item * 100)
            .reduce ((preValue, item) => preValue + item)
console.log(result)

//简写三:如果一个箭头函数,只有一行代码,并且返回一个对象,这个时候如何编写简写
// var bar = () => { return { name: "why", age: 18 }}

//此处无法识别{ name: "why", age: 18 }是函数体还是对象，所以会发生错误，因此要加括号
// var bar = () => { name: "why", age: 18 }
var bar = () => ({ name: "why", age: 18 })


// 2.应用场景
var obj = {
    data: [],
    getData: function (){
//、发送网络请求,将结果放到上面data属性中
// 在箭头函数之前的解决方案   做一个闭包
// var this = this
// setTimeout(function() {
//     var result = ["abc", "cba", "nba"]
//     _this.data = result
//}, 2000);
//     箭头函数之后
    setTimeout(()=>{
    var result = ["abc", "cba", "nba"]
    this.data = result
},2000)
}}//setTimeout的箭头函数指向父级作用域，由于是obj调用，所以指向obj。
obj.getData()  //在调用时指向obj对象