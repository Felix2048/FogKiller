<template>
    <div class="section">
        <div class="img-box" @mousemove="OnMoseMove" @mouseup="is_mouse_down=false" ref="imgbox">
            <div class="part-l" :style="{ width:left_pic_width +'px'}">
                <div class="img-before">
                    <img :src="rawFilePath" ref="pic" alt="">
                </div>
            </div>
            <span class="toolbar" :style="{ left:left_pic_width +'px'}">
                <span class="toolbar_button" @mousedown="is_mouse_down=true"
                ></span>
            </span>
            <div class="part-r" ref="part2">
                <div class="img-after">
                    <img  src="../assets/after.jpg" alt="">
                </div>
            </div>
            <div class="tags">
                <a href="#">去雾前</a>
                <a href="#">去雾后</a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'PicShow',
  created: function () {
    document.onselectstart = function () { return false }
  },
  props:{
    rawFilePath:"",
    newFilePath:""
  },
  data: function () {
    return {
      is_mouse_down: false,
      left_pic_width: 600
    }
  },
  computed: {
    pic_width: function () {
      let pic_width = this.$refs.pic.width
      return pic_width
    }
  },
  methods: {
    OnMoseMove: function (e) {
      if (this.is_mouse_down === false) return
      let left = this.$refs.imgbox.offsetLeft
      let offsetNO = e.pageX - left
      let per10 = this.pic_width * 0.01
      let per90 = this.pic_width * 0.99
      if (offsetNO < per10) {
        this.left_pic_width = per10
      } else if (offsetNO > per90) {
        this.left_pic_width = per90
      } else {
        this.left_pic_width = offsetNO
      }
    }
  }
}
</script>

<style scoped>
.section {
    position: relative;
    height:1200px
}

.section img {
    vertical-align: top;
}

.section a {
    text-decoration: none;
}

.img-box {
    width: 1240px;
    height: 668px;
    position: absolute;
    top: 20px;
    left: 50%;
    margin-left: -620px;
    overflow: hidden;
}

.part-l {
    position: absolute;
    width: 100px;
    overflow: hidden;
    z-index: 1;
}

.part-r {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}

.tags {
    position: absolute;
    bottom: 20px;
    left: 0;
    width: 100%;
    height: 40px;
    z-index: 2;
}

.tags a {
    position: absolute;
    display: block;
    width: 136px;
    height: 36px;
    font-size: 14px;
    text-align: center;
    line-height: 36px;
    border: 1px solid #fff;
    border-radius: 20px;
}

.tags a:nth-child(1) {
    bottom: 0;
    left: 20px;
    color: #fff;
}

.tags a:nth-child(2) {
    bottom: 0;
    right: 20px;
    color: #000;
    background-color: #fff;
}

.toolbar {
    position: absolute;
    height: 100%;
    left: 200px;
    top: 0;
    border-right: 1px solid rgba(255, 255, 255, 0.4);
    z-index: 3;
}

.toolbar_button {
    content: "";
    position: absolute;
    top: 50%;
    left: -32px;
    height: 66px;
    width: 66px;
    background: url(../assets/mz-bar.png) repeat;
}
</style>