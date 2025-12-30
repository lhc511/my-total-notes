window.addEventListener('load',function (){
    let focus=document.querySelector('.focus')
    //ul相对于父元素设置为500%大小，即是focus的五倍
    let ul=focus.children[0]
    let ol=focus.children[1]
    let w=focus.offsetWidth
    let index=0;
    //添加定时器自动切图
    function a(){
        timer=setInterval(function (){
        index++
        let translateX=-index*w
        ul.style.transition='all .3s'
        ul.style.transform='translateX('+translateX+'px)'
        console.log(ul.style.transform)
    },2000)
    }
    a()
    function moveXAn(index){
        let translatex=-index*w
        ul.style.transition='all .3s'
        ul.style.transform='translateX('+translatex+'px)'
    }


    //添加监听移动结束事件，ul移动结束后立刻切换图片元素位置
    ul.addEventListener('transitionend',function (){
        if (index>=ul.children.length-2){
            index=0
            let translateX=-index*w
            ul.style.transition=''
            ul.style.transform='translateX('+translateX+'px)'

        }else if(index<0){
            index=ul.children.length-3
            let translateX=-index*w
            ul.style.transition=''
            ul.style.transform='translateX('+translateX+'px)'
        }
        //选中ol的元素中带有的current类的li，然后一处类名，不移除元素
        ol.querySelector('li.current').classList.remove('current')
        // 给当前前元素加上current类
        ol.children[index].classList.add('current')
    })
    let startX=0
    let move=0 //移动的距离
    ul.addEventListener('touchstart',function (e){
        clearInterval(timer)
        // console.log('aaaa')
        //手指触摸时的初始坐标
        startX=e.targetTouches[0].pageX
        // elementX=ul.offsetLeft
    })

    //手指滑动轮播图
    ul.addEventListener('touchmove',function (e){
        // console.log('bbbb')
        //此处的e.targetTouches[0]得到的是在移动中的触摸的水平距离
        move=e.targetTouches[0].pageX-startX
        // console.log(move)
        //每一个图片的索引号*图片的宽度得到他的位置
        let tranlatex=-index*w+move
        ul.style.transition=''
        // this.style.left=tranlatex+'px'
        this.style.transform='translateX('+tranlatex+'px)'
        flag=true
        // e.preventDefault()//
    })
    let flag=false
    ul.addEventListener('touchend',function (){
        if(flag){
            flag=false
            if (move>50){
            index--
            moveXAn(index)
            }else if (move<-50){
                index++
                moveXAn(index)
            }else {
                moveXAn(index)
            }
        }
        a()
    })
    let slideBar=document.querySelector('.goBack')
    let nav=document.querySelector('nav');
    window.addEventListener('scroll',function (e){
        console.log(e)
        if (window.pageYOffset>=nav.offsetTop){
            slideBar.style.display='block'
        }else {
            slideBar.style.display='none'
        }
    })

    slideBar.addEventListener('click',function (){
        window.scroll(0,0)
    })

    // ul.addEventListener('touchend',function (e){
    //     console.log(move)
    //     if (Math.abs(move) > 50) {
    //         // 如果是右滑就是 播放上一张 moveX 是正值
    //         if (move > 0) {
    //             index--;
    //         } else {
    //             // 如果是左滑就是 播放下一张 moveX 是负值
    //             index++;
    //         }
    //         let translatex = -index * w;
    //         ul.style.transition = 'all .3s';
    //         ul.style.transform = 'translateX(' + translatex + 'px)';
    //         } else {
    //             // (2) 如果移动距离小于50像素我们就回弹
    //             let translatex = -index * w;
    //             ul.style.transition = 'all .1s';
    //             ul.style.transform = 'translateX(' + translatex + 'px)';
    //         }
    //
    //     a()
    // })
})