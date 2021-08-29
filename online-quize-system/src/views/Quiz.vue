<template>
  <div class="quiz">
    <div class="navigation">
      <div class="title">Quiz title</div>
      <div class="time">23:15</div>
      <b-button
        class="cancel-button"
        @click="onCancel"
        text="Cancel"
        variant="danger"
        >Cancel</b-button
      >
      <b-button
        class="submit-button"
        @click="onSubmit"
        text="Submit"
        variant="success"
        >Submit</b-button
      >
    </div>
    <hr />
    <div class="questions">
      <b-card
        class="mb-3 text-left"
        v-for="question in questions"
        :key="question.id"
      >
        <div class="question-title mb-2">
          {{ question.number }}. {{ question.text }}
        </div>
        <div class="question-answer">
          <b-form-textarea
            v-model="question.answer"
            id="textarea-rows"
            placeholder="Enter your answer"
            rows="8"
          ></b-form-textarea>
        </div>
      </b-card>
    </div>
  </div>
</template>
<script>
export default {
  methods: {
    onCancel() {
      this.$router.push("/dashboard");
    },
    onSubmit() {
      let answers = [];
      this.questions.forEach((question) => {
        answers.push({ text: question.answer, question: question.id });
      });
      let data = {
        user_profile: this.$store.state.user.id,
        exam: this.quizId,
        answers: answers,
      };
      this.$store.dispatch("submitQuizAnswers", data);
      this.$router.push("/dashboard");
    },
  },
  props: {
    quizId: {
      type: Number,
      required: true,
    },
  },
  computed: {
    questions() {
      return this.$store.state.questions.questions;
    },
  },
  watch: {
    questions(newValue) {
      newValue.forEach((question) => {
        question.answer = "";
      });
      this.quesitons = newValue;
    },
  },
};
</script>
<style scoped>
.quiz {
  width: 100%;
  height: 100vh;
  padding: 50px;
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
.submit-button {
  align-self: flex-end;
  margin-right: 0px;
}
.submit-button {
  align-self: flex-end;
}
.cancel-button {
  align-self: flex-end;
  margin-right: 10px;
  margin-left: auto;
}
hr {
  width: 80%;
  margin: 50px auto;
}
.questions {
  border-top: 1px solid rgba(0, 0, 0, 0.125);
  border-bottom: 1px solid rgba(0, 0, 0, 0.125);
  overflow-y: scroll;
  height: calc(100vh - 200px);
}
.time {
  align-self: center;
  justify-self: center;
  margin-left: auto;
  font-size: 30px;
  font-weight: 500;
}
</style>
