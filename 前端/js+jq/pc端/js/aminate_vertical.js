
    function a_vertical(obj,target,callback) {   //callback的参数用来传递一个函数
        let flag=true
        clearInterval(obj.timer)
        if(flag){
            flag=false
            obj.timer=setInterval(function (){
            // 当传进来的值小于现在所在位置，就会往负方向移动，做到往回走
            let step=(target-window.pageYOffset)/10
            step=step>0?Math.ceil(step):Math.floor(step)
            //设置最小值使结果收敛
            if (window.pageYOffset===target){
                clearInterval(obj.timer)
                if(callback){callback()}
            }
            //此处若对象的左边距小于传来目标距离则执行，但时当已经走到八百像素往五百像素走时(左边距>目标距离)就不满足，不会执行
            // else {
            //     obj.style.left=obj.offsetLeft+step+'px'
            //     console.log(obj.style.left)
            // }
            // obj.style.left=window.pageYOffset+step+'px'
            window.scroll(0,window.pageYOffset+step)
        },10)

        }
        }
