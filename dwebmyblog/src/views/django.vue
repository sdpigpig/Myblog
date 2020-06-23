<template>
  <div id="userlit">
    <div v-for="item in imglist" :key="item.pk" class="user">
      <img :src="'https://api.dweb.club/'+item.pic" alt />
      <p>{{  item.title  }}</p>
    </div>
    <div class="user">
      <img src="../assets/logo.svg" alt />
      <p>test123</p>
    </div>
    <div class="user">
      <img src="../assets/logo.svg" alt />
      <p>test123</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
            imglist:[]
        }
    },
    //用户在看到网页之前,最后Vue提供的一次函数执行
    mounted() {
        this.getData()
    },
    methods: {
        getData(){
            axios({
                url:'http://127.0.0.1:9000/api/',
                type:'json',
                method:'get'
            }).then((res)=>{
                console.log(res)
                // this.imglist = res.data.newsdata
            })
        }
    },
};
</script>

<style>
</style>