// const clickHandler = () =>{
//     console.log("window发生了点击")
//     window. removeEventListener("click", clickHandler)
// }
// window. addEventListener("click", clickHandler)

//自己派发一个浏览器原本不存在的事件让游览器进行监听
window. addEventListener("coderwhy", () => {
    console.log("监听到了coderwhy事件")
})

window.dispatchEvent(new Event("coderwhy"))