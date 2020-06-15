<template>
  <layout-default>

  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
  </layout-default>
</template>

<script>
// @ is an alias to /src
import LayoutDefault from '@/components/layouts/LayoutDefault.vue';
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Home",
  components: {
  	LayoutDefault,
    HelloWorld
  }
};
</script>
