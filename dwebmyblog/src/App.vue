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
          <div class="item" style="background: #777; color:#fff">
            <router-link to="/" style="color:#fff">Django框架</router-link>
          </div>
        </div>
        <div class="menu">
          <div class="item">
            <router-link to="/vuecli" >VueCli</router-link>
          </div>
        </div>
        <div class="menu">
          <div class="item">
            <a>实战博客</a>
          </div>
        </div>
        <div class="menu">
          <div class="item">
            <a>项目部署</a>
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

<style>
</style>
