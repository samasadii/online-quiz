<template>
  <div class="sidebar">
    <div class="dashboard-title">{{ $store.state.user.name }}</div>
    <div class="sidebar-items">
      <div
        class="sidebar-item"
        :class="{ selected: selectedItem == item.component }"
        v-for="item in items"
        :key="item.id"
        @click="changeSelectedItem(item.component)"
      >
        <b-icon class="icon" :icon="item.icon"></b-icon>
        <div class="title">{{ item.title }}</div>
      </div>
      <div @click="onLogout" class="sidebar-item red logout">
        <b-icon class="icon" icon="box-arrow-right"></b-icon>
        <div class="title red">Logout</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "sidebar",
  data() {
    return {
      items: [
        {
          id: 1,
          title: "Classes",
          component: "classes",
          icon: "collection",
        },
        {
          id: 2,
          title: "Quizes",
          component: "quizes",
          icon: "card-text",
        },
        {
          id: 3,
          title: "Profile",
          component: "profile",
          icon: "person",
        },
        {
          id: 4,
          title: "Settings",
          component: "setting",
          icon: "gear",
        },
      ],
    };
  },
  props: {
    selectedItem: {
      type: String,
      required: true,
    },
    changeSelectedItem: {
      type: Function,
      required: true,
    },
  },
  methods: {
    onLogout() {
      this.$store.state.loggedIn = false;
      this.$router.push("/signup");
    },
  },
  watch: {
    selectedItem(newValue) {
      if (newValue == "classes") {
        this.$store.dispatch("getClasses");
      } else if (newValue == "quizes") {
        this.$store.state.quizes = [];
        this.$store.state.admins.forEach((element) => {
          this.$store.dispatch("getQuizesOfClass", element.id);
        });
        this.$store.state.members.forEach((element) => {
          this.$store.dispatch("getQuizesOfClass", element.id);
        });
      }
    },
  },
};
</script>

<style scoped>
.sidebar {
  background-color: #083535;
  /*background-color: rgb(245, 245, 240); */
  padding: 10px;
  height: calc(100% - 10px);
  color: #fff;
  width: 100%;
}
.dashboard-title {
  color: white;
  margin-bottom: 20px;
  padding: 20px 30px 20px 30px;
  border-radius: 10px;
  text-align: left;
}
.sidebar-items {
  display: flex;
  flex-direction: column;
  padding: 0 20px 20px 20px;
  height: calc(100% - 55px);
}
.sidebar-item {
  height: 75px;
  width: 100%;
  padding: 0 10px 0 10px;
  align-items: center;
  display: flex;
}
.title {
  margin-left: 20px;
}
.logout {
  margin-top: auto;
  margin-bottom: 10px;
  align-self: flex-end;
}
.red {
  color: rgb(202, 105, 118);
}
.sidebar-item:hover {
  background-color: rgb(238, 238, 229);
  border-radius: 10px;
  cursor: pointer;
  color: #000;
}
.selected {
  background-color: rgb(238, 238, 229);
  border-radius: 10px;
  cursor: pointer;
  color: #000;
}
</style>
