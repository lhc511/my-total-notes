// window.addEventListener('load', function() {
//     // 1. 获取元素
//     let arrow_l = document.querySelector('.arrow-l');
//     let arrow_r = document.querySelector('.arrow-r');
//     let focus = document.querySelector('.focus');
//
//     let timer=setInterval(function (){
//         arrow_r.click()
//     },2000)
//     focus.addEventListener('mouseenter', function() {
//         clearInterval(timer)
//         arrow_l.style.display = 'block';
//         arrow_r.style.display = 'block';
//
//
//     });
//
//     focus.addEventListener('mouseleave', function() {
//         arrow_l.style.display = 'none';
//         arrow_r.style.display = 'none';
//         timer=setInterval(function (){
//             arrow_r.click()
//         },2000)
//
//     });
//
//     // 3. 动态生成小圆圈 有几张图片,我就生成几个小圆圈
//     var ul = focus.querySelector('ul');
//     var ol = focus.querySelector('.circle');
//     // console.log(ul.children.length);
//     for (var i = 0; i < ul.children.length; i++) {
//         // 创建一个小li
//         var li = document.createElement('li');
//         //给每一个li元素设置索引
//         li.setAttribute('index',i)
//
//         // 把小1i插入到o1 里面
//         ol.appendChild(li);
//         li.addEventListener('click', function () {
// // 干掉所有人 把所有的小1i 清除 current 类名
//             for (var i = 0; i < ol.children.length; i++) {
//                 ol.children[i].className = '';
//             }
//             // 留下我自己 当前的小1i 设置current 类名
//             this.className = 'current';
//             //点击后拿到当前位置li的索引号
//             let index=this.getAttribute('index')
//             a=index
//             circle=index
//             const focusWidth=focus.offsetWidth
//
//             animate(ul,-index*focusWidth)
//         })
//     }
//     //此处的初始赋值只会
//     ol.children[0].className = 'current'
//
//     let first=ul.children[0].cloneNode(true)//true表示深克隆
//     ul.appendChild(first)
//     let a=0
//     let circle=0
//
//     //节流阀
//     let flag=true
//     arrow_r.addEventListener('click',function (){
//         //节流阀
//         if (flag){
//             flag=false
//             if (a===ul.children.length-1){
//                 a=0
//                 ul.style.left=0+'px'
//             }
//             a++
//             animate(ul,-a*focus.offsetWidth,function (){
//                 //在动画结束之后吧flag设置为true，让点击事件再次生效
//                 flag=true
//             })
//             circle++
//             if(circle===ol.children.length){
//                 circle=0
//             }
//             for (let i=0;i<ol.children.length;i++){
//                 ol.children[i].className=''
//             }
//             ol.children[circle].className='current'
//             }
//
//     })
//
//
//     arrow_l.addEventListener('click',function (){
//         if(flag){
//             if (a===0){
//             a=ul.children.length-1
//             ul.style.left=-a*focus.offsetWidth+'px'
//         }
//         a--
//         circle--
//         if(circle<0){
//             circle=ol.children.length-1
//         }
//         for (let i=0;i<ol.children.length;i++){
//             ol.children[i].className=''
//         }
//         ol.children[circle].className='current'
//         animate(ul,-a*focus.offsetWidth,function (){
//             flag=false
//         })
//         }
//
//     })
//
// })
//
