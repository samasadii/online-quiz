<template>
  <div class="classes">
    <div class="navigation">
      <div class="title">Classes</div>
      <div class="join-button">
        <b-input-group class="mb-3">
          <b-form-input v-model="classLink" placeholder="Link"></b-form-input>
          <b-input-group-append>
            <b-button @click="onJoinClass" text="Join" variant="success"
              >Join</b-button
            >
          </b-input-group-append>
        </b-input-group>
      </div>
      <div class="create-button">
        <b-input-group class="mb-3">
          <b-form-input v-model="className" placeholder="Name"></b-form-input>
          <b-input-group-append>
            <b-button @click="onCreateClass" text="Create" variant="success"
              >Create</b-button
            >
          </b-input-group-append>
        </b-input-group>
      </div>
    </div>
    <hr />
    <div class="class-list">
      <div class="class-info" v-for="cls in $store.state.admins" :key="cls.id">
        <div class="item class-name">{{ cls.name }}</div>
        <div class="item">
          <b-dropdown
            id="dropdown-form"
            :text="' Members'"
            variant="outline-secondary"
            ref="dropdown"
            size="sm"
            class="m-2"
          >
            <b-dropdown-form>
              <b-form-checkbox
                v-for="member in cls.admin"
                :key="member.user.id"
                v-model="checked"
                value="true"
                unchecked-value="false"
                checked
                @change="onAdminChange(member, cls.id)"
              >
                {{ member.user.first_name }}
              </b-form-checkbox>
              <b-form-checkbox
                v-for="member in cls.student"
                :key="member.user.id"
                value="1"
                unchecked-value="0"
                @change="onAdminChange(member, cls.id)"
              >
                {{ member.user.first_name }}
              </b-form-checkbox>
            </b-dropdown-form>
          </b-dropdown>
        </div>
        <div class="item link">{{ cls.address }}</div>
        <div class="item">
          <b-button
            @click="onAddQuiz(cls.id)"
            class="button"
            text="Add Quiz"
            variant="success"
            size="sm"
            >Add Quiz</b-button
          >
        </div>
      </div>
      <div class="class-info" v-for="cls in $store.state.members" :key="cls.id">
        <div class="item class-name">{{ cls.name }}</div>
        <div class="item">
          <b-dropdown
            id="dropdown-form"
            :text="' Members'"
            variant="outline-secondary"
            ref="dropdown"
            size="sm"
            class="m-2"
          >
            <b-dropdown-form>
              <b-form-checkbox
                v-for="member in cls.admin"
                :key="member.user.id"
                v-model="checked"
                value="true"
                unchecked-value="false"
                checked
                @change="onAdminChange(member, cls.id)"
                disabled
              >
                {{ member.user.first_name }}
              </b-form-checkbox>
              <b-form-checkbox
                v-for="member in cls.student"
                :key="member.user.id"
                value="1"
                unchecked-value="0"
                @change="onAdminChange(member, cls.id)"
                disabled
              >
                {{ member.user.first_name }}
              </b-form-checkbox>
            </b-dropdown-form>
          </b-dropdown>
        </div>
        <div class="item link">{{ cls.address }}</div>
        <div class="item">
          <b-button
            @click="onAddQuiz(cls.id)"
            class="button"
            text="Add Quiz"
            variant="success"
            size="sm"
            disabled
            >Add Quiz</b-button
          >
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "classes",
  data() {
    return {
      className: "",
      classLink: "",
      checked: true,
    };
  },
  methods: {
    onCreateClass() {
      this.$store.dispatch("addClass", this.className);
    },
    onJoinClass() {
      this.$store.dispatch("joinClass", this.classLink);
    },
    onAddQuiz(classId) {
      this.$router.push({
        name: "createQuiz",
        params: {
          classId: classId,
        },
      });
    },
    onAdminChange(userId, classId) {
      let data = {
        userId: userId,
        classId: classId,
      };
      this.$store.dispatch("addAdminToClass", data);
    },
  },
};
</script>
<style scoped>
.classes {
  height: calc(100% - 10px);
  width: 100%;
}
.navigation {
  display: flex;
  width: 100%;
}
.title {
  font-weight: 500;
  font-size: 25px;
  color: black;
}
.create-button {
  align-self: flex-end;
  margin-left: 10px;
  margin-right: 0px;
}
.join-button {
  align-self: flex-end;
  margin-left: auto;
}
hr {
  width: 80%;
  color: rgb(61, 61, 56);
  margin-bottom: 50px;
  margin-top: 50px;
}
.class-list {
  height: 85%;
  width: 100%;
  overflow-y: scroll;
}
.class-info {
  padding: 0 20px 0 2px;
  height: 60px;
  display: flex;
  justify-content: space-ev;
  background-color: rgb(245, 245, 240);
  border-radius: 5px;
  align-items: center;
  margin-bottom: 20px;
}
.item {
  color: grey;
  font-size: 14px;
  flex: 1;
}
.class-name {
  color: rgb(61, 61, 56);
  font-size: 18px;
}
.icon {
  color: rgb(187, 6, 6);
}
.link {
  font-size: 10px;
}
.button {
  color: white;
}
</style>
