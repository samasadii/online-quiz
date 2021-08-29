import Vue from "vue";
import Vuex from "vuex";
import mixin from "../mixin";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: {
      id: "",
      name: "",
      email: "",
    },
    admins: [],
    members: [],
    loggedIn: false,
    quizes: [],
    questions: [],
  },
  mutations: {
    setUserData(state, payload) {
      state.user.email = payload.user.username;
      state.user.name = payload.user.first_name;
      state.user.id = payload.id;
      state.loggedIn = true;
    }, //change admin and membership names
    setClassesData(state, payload) {
      state.admins = [];
      state.members = [];
      state.admins.push(...payload.admin);
      state.members.push(...payload.membership);
    },
    setQuizesData(state, payload) {
      state.quizes.push(payload);
    },
    setQuizQuestionsData(state, payload) {
      state.questions = payload;
    },
  },
  actions: {
    signup(context, payload) {
      mixin.methods
        .baseRequest({
          url: "user/create/",
          method: "POST",
          data: { user: payload },
        })
        .then((res) => {
          context.commit("setUserData", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    login(context, payload) {
      mixin.methods
        .baseRequest({
          url: "user/login/",
          method: "POST",
          data: payload,
        })
        .then((res) => {
          console.log(res);
          context.commit("setUserData", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    addClass(context, payload) {
      let data = {
        name: payload,
        admin: [context.state.user.id],
      };

      mixin.methods
        .baseRequest({
          url: "class/create/",
          method: "POST",
          data: data,
        })
        .then((res) => {
          context.dispatch("getClasses", context.state.user.id);
          console.log(res);
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    getClasses(context) {
      mixin.methods
        .baseRequest({
          url: "classes/" + context.state.user.id + "/",
          method: "GET",
        })
        .then((res) => {
          console.log(res);
          context.commit("setClassesData", res.data);
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    joinClass(context, payload) {
      mixin.methods
        .baseRequest({
          url:
            "user/" +
            context.state.user.id +
            "/join/class-room/" +
            payload.trim() +
            "/",
          method: "POST",
        })
        .then((res) => {
          console.log(res);
          context.state.members.push(res.data);
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    createQuiz(context, payload) {
      mixin.methods
        .baseRequest({
          url: "exam/create/",
          method: "POST",
          data: payload,
        })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    addAdminToClass(context, payload) {
      mixin.methods
        .baseRequest({
          url:
            "user/" +
            payload.userId +
            "/admin/class-room/" +
            payload.classId +
            "/",
          method: "POST",
        })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    getQuizesOfClass(context, payload) {
      mixin.methods
        .baseRequest({
          url: "exams/" + payload + "/",
          method: "GET",
        })
        .then((res) => {
          console.log(res);
          context.commit("setQuizesData", res.data);
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    getQuizQuestions(context, payload) {
      mixin.methods
        .baseRequest({
          url: "exam/" + payload + "/questions/",
          method: "GET",
        })
        .then((res) => {
          console.log(res);
          context.commit("setQuizQuestionsData", res.data);
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    submitQuizAnswers(context, payload) {
      mixin.methods
        .baseRequest({
          url: "take-exam/",
          method: "POST",
          data: payload,
        })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
  },
  modules: {},
});
