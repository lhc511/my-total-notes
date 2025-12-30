window.addEventListener('load',function (){
    const preview_img=document.querySelector('.preview_img')
    const mask=document.querySelector('.mask')
    const big=document.querySelector('.big')
    preview_img.addEventListener('mouseover',function (e){
        mask.style.display='block'
        big.style.display='block'
    })
    preview_img.addEventListener('mouseout',function (){
        mask.style.display='none'
        big.style.display='none'
    })


   preview_img.addEventListener('mousemove',function (e){
       //鼠标的在框内的相对距离
        let x=e.pageX-this.offsetLeft
        let y=e.pageY-this.offsetTop

       //遮挡层离左边的距离
        let maskX=x-mask.offsetWidth/2
       //遮挡层离上边的距离
        let maskY=y-mask.offsetHeight/2
       // 遮挡层的最大移动距离(向右，向下)
        let maskMax = preview_img.offsetWidth - mask.offsetWidth;
        if (maskX<=0){
            maskX=0
        }
        if (maskY<=0){
            maskY=0
        }
        if (maskY>=maskMax){
            maskY=maskMax
        }
        if (maskX>=maskMax){
            maskX=maskMax
        }
        mask.style.left=maskX+'px'
        mask.style.top=maskY+'px'

        let bigIMG=document.querySelector('.bigImg')
        //大图片比较大所以用大图片宽度减去显示框的宽度
        let bigMax=bigIMG.offsetWidth-big.offsetWidth
        // 鼠标原本能移动的距离 * (放大后移动的最大距离/原本移动的最大距离)
        let bigMaskX=maskX*(bigMax/maskMax)
        let bigMaskY=maskY*(bigMax/maskMax)
       //操纵的是大的图片.而不是框,所以要相反的方向
        bigIMG.style.left = -bigMaskX + 'px';
        bigIMG.style.top = -bigMaskY + 'px';

    })

})


