// window.addEventListener('load',function (){
//
//     function a(obj,target){
//          clearInterval(obj.timer)
//         obj.timer=setInterval(function (){
//
//             let step=(target-obj.offsetLeft)/10
//             step=step>0?Math.ceil(step):Math.floor(step)
//
//             if(obj.offsetLeft===target){
//                 clearInterval(obj.timer)
//             }
//
//             obj.style.left=obj.offsetLeft+step+'px'
//
//
//             },20)
//         }
//      //白点跟随转变
//         function dotChangeAuto(){
//             for (let c=0;c<circle.children.length;c++){
//                 circle.children[c].className=''
//             }
//             circle.children[index].className="current"
//         }
//
//      // 自动切换
//     function changeAuto(){
//         ul.changAutoTimer=setInterval(function (){
//             index++
//             if (index>lis.length-1){index=0}
//             a(ul,-index*focus.offsetWidth)
//             dotChangeAuto()
//         },2000)
//     }
//
//     const focus=document.querySelector('.focus')
//     const circle=focus.querySelector('.circle')
//     //页面的翻页箭头
//     const arrow_l=document.querySelector('.arrow-l')
//     const arrow_r=document.querySelector('.arrow-r')
//     //图片列表获取
//     const ul=focus.querySelector('ul')
//     const lis=ul.querySelectorAll('li');
//     let circleIndex=0;
//
//     (function (){
//         for (let i=0;i<lis.length;i++){
//             let li=document.createElement('li')
//             li.setAttribute('li_index',i)
//             circle.appendChild(li)
//
//             li.addEventListener('click',function (){
//                 for (let i=0;i<circle.children.length;i++){
//                     circle.children[i].className=''
//                 }
//                 this.className='current'
//                 let li_index=this.getAttribute('li_index')
//                 a(ul,-li_index*focus.offsetWidth)
//             })
//         }
//         circle.children[0].className='current'
//         }())
//
//
//     changeAuto()
//     focus.addEventListener('mouseenter',function (){
//         arrow_l.style.display='block'
//         arrow_r.style.display='block'
//         clearInterval(ul.changAutoTimer)
//
//     })
//     focus.addEventListener('mouseleave',function (){
//         arrow_l.style.display='none'
//         arrow_r.style.display='none'
//         changeAuto()
//
//     });
//
//     let index=0
//     //向左移动
//     arrow_l.addEventListener('click',function (){
//             index--
//             if (index<0){index=lis.length-1}
//             a(ul,-index*focus.offsetWidth)
//             console.log(focus.offsetWidth)
//             console.log(ul.offsetLeft)
//             dotChangeAuto()
//         })
//     //向右移动
//     arrow_r.addEventListener('click',function (){
//         index++
//         if (index>lis.length-1){index=0}
//         a(ul,-index*focus.offsetWidth)
//         dotChangeAuto()
//     })
//
//
//
//
//     // ******************************直接切换，无动画效果
//     //得到图片的存储地址
//     // function get_src(src_list){
//     //        for (let item=0; item<lis.length;item++){
//     //            src_list.push(lis[item].children[0].children[0].src)
//     //        }
//     //     }
//     // //newAddressArr:存放排序好的新地址顺序  targetArr:存放目标元素/父元素列表
//     // function change_page(newAddressArr){
//     //     for (let i=0;i<newAddressArr.length;i++){
//     //         lis[i].children[0].children[0].src=newAddressArr[i]
//     //     }
//     // }
//     //
//     // function leftMove(pic_list,tmp_list){
//     //     for (let i=0;i<pic_list.length;i++){
//     //         if (i+1<pic_list.length){
//     //             tmp_list.push(pic_list[i+1])
//     //         }
//     //         else {
//     //             tmp_list.push(pic_list[0])
//     //         }
//     //     }
//     // }
//     // //向右移动
//     // function rightMove(pic_list,tmp_list){
//     //     for (let i=pic_list.length;i>0;i--){
//     //         if(i===pic_list.length){
//     //             tmp_list.push(pic_list[i-1])
//     //         }else {
//     //             tmp_list.push(pic_list[pic_list.length-i-1])
//     //         }
//     //     }
//     // }
//
//     // arrow_l.addEventListener('click',function (){
//     //     const pic_list=[];
//     //     const tmp_list=[]
//     //     get_src(pic_list)
//     //     // console.log(pic_list)
//     //     //数据向左移动
//     //     leftMove(pic_list,tmp_list)
//     //     // console.log(tmp_list)
//     //     change_page(tmp_list)//图片换位
//     // })
//     //
//     // arrow_r.addEventListener('click',function (){
//     //     存放的原地址路径
//     //     const pic_list=[];
//     //     get_src(pic_list)
//     //     // console.log(pic_list)
//     //     let tmp_list=[]
//     //     //数据向右滑动
//     //     rightMove(pic_list,tmp_list)
//     //     // console.log(tmp_list)
//     //     change_page(tmp_list)
//     // })
// })