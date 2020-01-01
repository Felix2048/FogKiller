<template>
    <div class="navbar">
        
        <div class="navbar-title">FogKiller</div>
    </div>
</template>

<script>
export default {
  name: 'NavBar'
}
</script>

<style scoped>
.navbar {
    height: 100%;
    border-width: 0px;
    border-bottom-width: 1px;
    border-style: solid;
    border-bottom-color: rgb(220, 220, 220);
    box-shadow: 0px 5px 5px #f2f2f2;
    position: relative;
    
}

.navbar-title {
    height: 100%;
    position: relative;
    font-size: 28px;
    padding:0px auto 0px auto;
    top:10px;
    text-align: center
}

</style>