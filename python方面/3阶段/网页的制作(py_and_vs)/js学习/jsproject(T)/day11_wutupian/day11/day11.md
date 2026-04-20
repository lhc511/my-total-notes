## 1.jQuery hover() 方法
  hover() 方法规定当鼠标指针悬停在被选元素上时要运行的两个函数。
  方法触发 mouseenter 和 mouseleave 事件。

  $(selector).hover(handlerIn, handlerOut)
## 2.jQuery stop() 方法
  stop() 方法为被选元素停止当前正在运行的动画。
  $(selector).stop(stopAll,goToEnd)

  stopAll	可选。布尔值，规定是否停止被选元素的所有加入队列的动画。默认是 false。
  goToEnd	可选。布尔值，规定是否立即完成当前的动画。默认是 false。
## 3.动画加载页面效果
  1. html页面引入文件scrollReveal.js
  2. 在需要加载动画效果的div或者其他标签中添加 
     data-scroll-reveal属性
  3. <div data-scroll-reveal="enter left and move 50px over 1.33s">
          dowebok.com
     </div> 
  4. 然后在js区域加入以下代码：
     window.scrollReveal = new scrollReveal({reset: true});
##4.data-scroll-reveal属性
    enter

    说明: 动画起始方向
    值: top | right | bottom | left
  move
    说明: 动画执行距离
    值: 数字，以 px 为单位
  over
    说明: 动画持续时间
  值: 数字，以秒为单位
    after/wait
    说明: 动画延迟时间
  值: 数字，以秒为单位

### 自己保存数据

   