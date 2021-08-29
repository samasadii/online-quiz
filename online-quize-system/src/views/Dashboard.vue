<template>
  <div class="wrapper">
    <div class="sidebar">
      <sidebar
        :selectedItem="selectedItem"
        :changeSelectedItem="changeSelectedItem"
      />
    </div>
    <div class="content">
      <classes v-if="selectedItem == 'classes'" />
      <quizes v-if="selectedItem == 'quizes'" />
    </div>
  </div>
</template>
<script>
import sidebar from "../components/SideBar.vue";
import classes from "../components/Classes.vue";
import quizes from "../components/Quizes.vue";
export default {
  name: "dashboard",
  components: {
    sidebar,
    classes,
    quizes,
  },
  data() {
    return {
      selectedItem: "classes",
    };
  },
  methods: {
    changeSelectedItem: function(title) {
      this.selectedItem = title;
    },
  },
};
</script>
<style scoped>
.wrapper {
  background-color: rgb(238, 238, 229);
  display: flex;
  margin: 0 !important;
  padding: 0;
  height: 100vh;
  width: 100%;
}
.sidebar {
  border-radius: 0 15px 15px 0;
  margin: 5px;
  width: 300px;
  height: cal(100% - 5px);
}
.content {
  width: 100%;
  height: 100vh;
  padding: 50px;
  margin: 0 10px 0 10px;
}
</style>
