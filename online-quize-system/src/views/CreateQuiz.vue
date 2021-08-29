<template>
  <div class="create-quiz">
    <div class="navigation">
      <div class="title">Create a New Quiz</div>
      <b-button
        @click="onCancel"
        class="cancel-button"
        text="Cancel"
        variant="danger"
        >Cancel</b-button
      >
      <b-button
        class="reset-button"
        @click="onReset"
        text="Reset"
        variant="primary"
        >Reset</b-button
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
      <b-card class="text-left">
        <b-form @submit="onSubmit" @reset="onReset" v-if="show">
          <b-form-group
            id="input-group-1"
            label="Quiz Label"
            label-for="input-1"
          >
            <b-form-input
              id="input-1"
              v-model="form.name"
              required
              placeholder="Enter quiz label"
            >
            </b-form-input>
          </b-form-group>

          <label for="start-datepicker">Choose start date</label>
          <b-form-datepicker
            id="start-datepicker"
            v-model="form.startDate"
            class="mb-2"
          ></b-form-datepicker>

          <label for="start-timepicker">Choose start time</label>
          <b-form-timepicker
            id="start-timepicker"
            v-model="form.startTime"
            locale="en"
          ></b-form-timepicker>

          <label for="end-datepicker">Choose end date</label>
          <b-form-datepicker
            id="end-datepicker"
            v-model="form.endDate"
            class="mb-2"
          ></b-form-datepicker>

          <label for="end-timepicker">Choose end time</label>
          <b-form-timepicker
            id="end-timepicker"
            v-model="form.endTime"
            locale="en"
          ></b-form-timepicker>

          <div v-for="question in form.questions" :key="question.number">
            <label for="inline-form-input-name"
              >Question {{ question.number }}</label
            >
            <b-input
              id="inline-form-input-name"
              placeholder="Write your question ..."
              v-model="question.text"
            ></b-input>
          </div>
          <b-button
            @click="onAddQuestion"
            variant="primary"
            class="add-question-button"
            >Add Question</b-button
          >
        </b-form>
      </b-card>
    </div>
  </div>
</template>
<script>
export default {
  name: "createQuiz",
  data() {
    return {
      form: {
        name: "",
        startDate: "",
        endDate: "",
        startTime: "",
        endTime: "",
        questions: [
          {
            number: "1",
            text: "",
          },
        ],
      },
      show: true,
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      let data = {
        title: this.form.name,
        start_time: this.form.startDate + "T" + this.form.startTime,
        end_time: this.form.endDate + "T" + this.form.endTime,
        class_room: this.classId,
        questions: this.form.questions,
      };
      this.$store.dispatch("createQuiz", data);
      this.$router.push("/dashboard");
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.name = "";
      this.form.startDate = "";
      this.form.endDate = "";
      this.form.startTime = "";
      this.form.endTime = "";
      this.form.questions = [
        {
          number: "1",
          text: "",
        },
      ];
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    onCancel() {
      this.$router.push("/dashboard");
    },
    onAddQuestion() {
      this.form.questions.push({
        number: this.form.questions.length + 1,
        text: "",
      });
    },
  },
  props: {
    classId: {
      type: Number,
      required: true,
    },
  },
};
</script>
<style scoped>
.create-quiz {
  width: 100%;
  height: 100vh;
  padding: 50px;
  overflow: hidden;
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
  margin-left: 10px;
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
.add-question-button {
  margin-top: 15px;
}
.questions {
  border-top: 1px solid rgba(0, 0, 0, 0.125);
  border-bottom: 1px solid rgba(0, 0, 0, 0.125);
  overflow-y: scroll;
  height: calc(100vh - 200px);
}
</style>
