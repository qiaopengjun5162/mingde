<template>
    <div class="home">
        <Header></Header>

        <Footer></Footer>
    </div>
</template>

<script setup lang="ts">
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"

// 测试CORS的跨域配置是否有问题
import axios from "axios"
const http = axios.create()

// 测试服务端的跨域是否配置成功
http.get("/api/home/demo/").then(response=>{
  console.log(response.data);
})

// // 测试服务端的跨域是否配置成功
// http.get("http://api.mingde.cn:8000/home/demo/").then(response=>{
//   console.log(response.data);
// })

</script>

<style scoped>
</style>
