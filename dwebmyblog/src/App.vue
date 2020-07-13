<template>
  <div id="home">
    <div>
      <button v-if="loginType == false" @click="showLoginRegisterBox(1)">登录</button>
      <button v-if="loginType == false" @click="showLoginRegisterBox(2)">注册</button>
      <button @click="toHome" v-if="loginType">首页</button>
      <button @click="toUserinfo" v-if="loginType">个人中心</button>
      <button v-if="loginType" @click="showLoginRegisterBox(3)">修改</button>
      <div class="header">
        <h1>{{  siteinfo.sitename  }}</h1>
        <img :src="siteinfo.logo" alt />
      </div>

      <hr />
      <div class="content">
        <div class="menu">
          <div v-for="item in menulist" :key="item.id" class="item">
            <div v-if="item.id == choosed" style="background: #777; color:#fff">
              <a style="color:#fff">{{ item.text }}</a>
            </div>
            <div v-else style="color:#000" @click="chooseMenu(item.id)">
              <a style="color:#000">{{ item.text }}</a>
            </div>
          </div>
        </div>

        <div class="userlist">
          <p>{{ choosed_text }}</p>

          <hr />
          <router-view />
        </div>
      </div>
      <hr />
    </div>

    <LogiBox v-if="boxtarget" :target="boxtarget" @hideBox="hideLoginRegsiterBox"></LogiBox>
    <div class="foot">Copyright© 2020 个人练习</div>
  </div>
</template>



<script>
import axios from "axios";
import LogiBox from "../src/components/LoginBox";

export default {
  components: {
    LogiBox
  },
  data() {
    return {
      menulist: [],
      choosed: 1,
      choosed_text: "Dango后端",
      boxtarget: 0,
      siteinfo:{},
      loginType:false

    };
  },
  mounted() {
    try {
      if(window.localStorage.getItem('token').length>0){
        this.loginType = true;
      }
    } catch (error) {
      console.log(error)
    }

    this.getMenuList();
  },
  methods: {
    toHome(){
      this.$router.push({path:'/'})
    },
    toUserinfo(){
      this.$router.push({path:'/userinfo'})
    },
    //获取分类列表
    getMenuList() {
      console.log("开始获取分类");
      axios({
        url: "http://127.0.0.1:9000/get-menu-list/",
        type: "json",
        method: "get"
      }).then(res => {
        console.log(res);
        this.menulist = res.data.menu_data;
        this.siteinfo = res.data.siteinfo
      });
    },
    chooseMenu(id) {
      console.log(id);
      this.choosed = id;
      for (let i = 0; i < this.menulist.length; i++) {
        if (id == this.menulist[i].id) {
          this.choosed_text = this.menulist[i].text;
        }
      }
      //进行ID传参跳转
      this.$router.push({ path: "/", query: { menuId: id } });
    },
    //展示登录窗体
    showLoginRegisterBox(value) {
      this.boxtarget = value;
      // console.log(this.boxtarget)
    },
    //隐藏父组件
    hideLoginRegsiterBox(){
      this.boxtarget = 0;
    }
  }
};
</script>

<style>
</style>
