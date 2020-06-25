<template>
  <div id="login">
    <div id="loginbox">
      <div class="form">
        <div class="item">
          <div class="span">用户名:</div>

          <input v-model="username" type="text" placeholder="请输入用户名" />
        </div>
        <div class="item">
          <div class="span">密码:</div>
          <input v-model="password" type="text" placeholder="请输入密码" />
        </div>
        <button @click="toLogin">登录</button>
      </div>
    </div>
  </div>
</template>




<script>
import axios from "axios";
import Qs from "qs"
export default {
  name: "LogiBox",
  data() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    toLogin() {
      console.log(this.username, this.password);
      var username = this.username;
      var password = this.password;
      axios({
        url: 'http://127.0.0.1:9000/login/',
        // type: 'json',
        data:Qs.stringify( {
          username,
          password
        }),
        method: 'post',
        headers:{
            "Content-Type":"application/x-www-form-urlencoded"
        }
      }).then((res) => {
        console.log(res)
      })
    }
  }
};
</script>




<style>
#login {
  position: absolute;
  top: 0;
  width: 700px;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
#loginbox {
  width: 300px;
  height: 300px;
  border: 1px solid #000;
  background: #00000090;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #fff;
}

#loginbox .form .item {
  font-weight: 700;
  margin: 10px auto;
}

#loginbox .form .item .span {
  float: left;
  width: 80px;
}
</style>