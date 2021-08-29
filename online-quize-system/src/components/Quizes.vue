<template>
  <div class="quizes">
    <div class="navigation">
      <div class="title">Quizes</div>
    </div>
    <hr />
    <div class="quiz-list">
      <div v-for="cls in $store.state.quizes" :key="cls.id">
        <div class="quiz-info" v-for="quiz in cls.exams" :key="quiz.id">
          <div class="item quiz-name">{{ quiz.title }}</div>
          <div class="item">Class: {{ cls.name }}</div>
          <div class="item">
            Time:
            {{
              new Date(quiz.start_time).toLocaleDateString(undefined, options)
            }}
            -
            {{ new Date(quiz.end_time).toLocaleDateString(undefined, options) }}
          </div>
          <div class="item">
            <b-button
              @click="onStartQuiz(quiz.id)"
              class="start-button"
              size="sm"
              text="Create"
              variant="success"
              >Start</b-button
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "quizes",
  data() {
    return {
      options: {
        hour: "numeric",
        minute: "numeric",
      },
    };
  },
  methods: {
    onStartQuiz(quizId) {
      this.$store.dispatch("getQuizQuestions", quizId);
      this.$router.push({
        name: "quiz",
        params: {
          quizId: quizId,
        },
      });
    },
  },
};
</script>
<style scoped>
.quizes {
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
  margin-right: 0px;
  margin-left: auto;
}
hr {
  width: 80%;
  color: rgb(61, 61, 56);
  margin-bottom: 50px;
  margin-top: 50px;
}
.quiz-list {
  height: 90%;
  width: 100%;
  overflow-y: scroll;
}
.quiz-info {
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
.quiz-name {
  color: rgb(61, 61, 56);
  font-size: 18px;
}
.start-button {
  color: white;
}
</style>
