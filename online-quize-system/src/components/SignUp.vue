<template>
  <div class="SignUp">
    <div class="leftSide">
      <div class="welcome">Welcome to Classify</div>
      <img class="img" src="../assets/backg.png" alt="logo" />
      <div class="footer"></div>
    </div>
    <div class="rightSide">
      <h3>Sign up to Classify</h3>
      <p class="sign-up text-center">
        Already have an account?
        <router-link to="/login">Log In!</router-link>
      </p>
      <div class="form-input">
        <input
          type="text"
          v-model="signup.first_name"
          class="sign-up-name"
          placeholder="Name"
        />
      </div>

      <div class="form-input">
        <input
          type="email"
          class="sign-up-email"
          id="email"
          v-model="signup.username"
          placeholder="Email"
          required
        />
      </div>

      <div class="form-input">
        <input
          type="password"
          v-model="signup.password"
          class="sign-up-password"
          placeholder="Password"
          required
        />
      </div>
      <button class="btn-submit dark-green" @click="signupUser">
        Get Started!
      </button>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      signup: {
        username: "",
        password: "",
        first_name: "",
      },
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.loggedIn;
    },
  },
  methods: {
    signupUser() {
      this.$store.dispatch("signup", this.signup);
    },
  },
  watch: {
    loggedIn(newValue) {
      if (newValue) {
        this.$router.push("/dashboard");
      }
    },
  },
};
</script>
<style scoped>
.SignUp {
  display: flex;
}
.leftSide {
  width: 50%;
  position: relative;
  display: flex;
  flex-direction: column;
  background-color: #eef3f3;
  height: 100%;
  padding-top: 50px;
}
.logo {
  position: absolute;
  margin-left: 50px;
  text-align: left;
}
.welcome {
  position: absolute;
  width: 100%;
  font-size: 32px;
  justify-content: center;
  color: #083535;
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
  margin: 20px auto 50px auto;
  text-align: center;
}
.img {
  margin-top: 150px;
  display: block;
  background-blend-mode: color;
  background-color: #eef3f3;
  height: 420px;
  color: #083535;
}
.footer {
  background-color: #eef3f3;
  height: 200px;
}

.rightSide {
  width: 50%;
  display: flex;
  flex-direction: column;
  margin-top: 70px;
  text-align: left;
  height: auto;
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
}
.rightSide h3 {
  margin-bottom: 15px;
  font-size: 36px;
  text-align: center;
}
.form-input input {
  display: table;
  background-color: #eef3f3;
  border-radius: 50px !important;
  padding-top: 10px;
  padding-bottom: 10px;
  width: 50%;
  border: none !important;
  border: 1px solid #eef3f3 !important;
  font-size: 20px !important;
  color: #000 !important;
  font-weight: 400;
  margin: 0 auto;
  padding-left: 28px;
  align-self: center;
  margin-bottom: 16px;
}
.btn-submit {
  display: table;
  border-radius: 50px !important;
  padding-top: 10px;
  padding-bottom: 10px;
  width: 50%;
  border: 1px solid #083535 !important;
  font-size: 20px !important;
  color: #eef3f3;
  margin: 0 auto;
  margin-top: 50px;
  text-align: center;
  align-self: center;
}

input:focus,
textarea:focus {
  box-shadow: none !important;
  border: 2px solid #083535 !important;
  background-color: #eef3f3;
  outline-width: 0;
  font-weight: 400;
}
::placeholder {
  font-size: 20px;
  margin-left: 20px;
  text-align: left;
}
::placeholder:focus {
  color: #000;
}
.sign-up.text-center {
  font-size: 20px;
  color: #083535;
  margin-bottom: 100px;
}
.dark-green {
  background-color: #083535;
}
</style>
