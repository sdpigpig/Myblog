<template>
  <div id="home">
    <div>
      <div class="header">
        <h1>网页标签</h1>
        <img src="./assets/logo.png" alt />
      </div>

      <hr />
      <div class="content">
        <div class="menu">
          <div v-for="item in menulist" :key="item.id" class="item">
            <div 
            v-if="item.id == choosed"
            style="background: #777; color:#fff"
            >
              <router-link to="/" style="color:#fff">{{  item.text  }}</router-link>
            </div>
            <div 
            v-else
            style="color:#000"
            @click="chooseMenu(item.id)"
            >
              <router-link to="/" style="color:#000">{{  item.text  }}</router-link>
            </div>
          </div>
        </div>

        <div class="userlist">
          <p>Django框架</p>

          <hr />
          <router-view />
        </div>
      </div>
      <hr />
    </div>

    <div class="foot">Copyright© 2020 个人练习</div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data(){
    return{
      menulist:[],
      choosed:1
    }
  },
  mounted() {
    this.getMenuList()
  },
  methods: {
    getMenuList(){
      console.log('开始获取分类')
      axios({
        url:'http://127.0.0.1:9000/get-menu-list/',
        type:'json',
        method:'get'
      }).then((res)=>{
        console.log(res)
        this.menulist = res.data
      })
    },
    chooseMenu(id){
      console.log(id)
      this.choosed = id
    }
  }
}
</script>

<style>
</style>
