<template>
  <div id="app">
    <div id="nav"></div>
    <router-view />
  </div>
</template>
<script>
export default {
  computed: {
    loggedIn() {
      return this.$store.state.loggedIn;
    },
  },
  watch: {
    loggedIn(newValue) {
      if (!newValue) {
        this.$router.push("/signup");
      } else {
        this.$store.dispatch("getClasses");
      }
    },
  },
};
</script>
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
