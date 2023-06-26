<template>
  <div class="footer">
    <ul>
      <li v-for="item in nav.footer_nav_list">
        <a v-if="item.is_http" :href="item.link">{{ item.name }}</a>
        <router-link v-else :to="item.link">{{ item.name }}</router-link>
      </li>
    </ul>
    <p>Copyright © mingde.com版权所有 | 京ICP备17072161号-1</p>
  </div>
</template>

<script setup lang="ts">
import nav from "../api/nav";

nav.get_footer_nav().then((response: { data: any }) => {
  nav.footer_nav_list = response.data;
});

</script>

<style scoped>
.footer {
  width: 100%;
  height: 128px;
  color: #545C63;
}

.footer ul {
  margin: 0 auto 16px;
  padding-top: 38px;
  width: 930px;
}

.footer ul li {
  float: left;
  width: 112px;
  margin: 0 10px;
  text-align: center;
  font-size: 14px;
}

.footer ul::after {
  content: "";
  display: block;
  clear: both;
}

.footer p {
  text-align: center;
  font-size: 12px;
}
</style>
