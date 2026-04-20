// 1.setTimeout
// function hySetTimeout(fn, duration) {
//     fn.call("abc")//this:abc
//     fn()//this:windows
// }
// hySetTimeout (function() {
//console.log(this) // window
// }, 3000)

//setTimeout的指向与上述同理，关键看其内部如何实现调用的，而其在函数内部是进行独立调用因此this指向windows
// setTimeout(function() {
// console. log(this) // window
// }, 2000)

// 3.数组、forEach/map/filter/find
var names = ["abc", "cba", "nba"]
// // 这两个函数第二个参数传递的是绑定的对象，若没有默认为windows
// names. forEach(function(item) {
// console.log(item, this)//abc
// }, "abc")
// names.map(function(item) {
// console. log(item, this)//cba
// }, "cba")

//·apply/call/bind :· 当传入null/undefined时,自动将this绑定成全局对象
foo.apply(null) //window
foo.apply(undefined) //window

var bar = foo.bind(null)
bar() //window