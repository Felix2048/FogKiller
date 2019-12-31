<template>
<div>
  <div class="block">
    <span class="demonstration">P</span>
    <el-slider v-model="value1"></el-slider>
  </div>
  <div class="block">
    <span class="demonstration">AMAX</span>
    <el-slider v-model="value2"></el-slider>
  </div>
  <div class="block">
    <span class="demonstration">W</span>
    <el-slider v-model="value3" :show-tooltip="false"></el-slider>
  </div>
  <div class="block">
    <span class="demonstration">PatchSize</span>
    <el-slider v-model="value4" :format-tooltip="formatTooltip"></el-slider>
  </div>
  <div class="block">
    <span class="demonstration">TMin</span>
    <el-slider v-model="value5"></el-slider>
  </div>
</div>
</template>

<script>
export default {
  name: 'Settings',
  data:function(){
    return{
      value1: 20,
      value2: 50,
      value3: 36,
      value4: 48,
      value5: 42
    };
  },
  methods:{
    formatTooltip(val) {
        return val / 100;
      }
  }
}
</script>

<style scoped>

</style>