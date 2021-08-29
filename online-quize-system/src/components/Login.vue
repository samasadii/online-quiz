<template>
  <div class="SignUp">
    <div class="leftSide">
      <div class="welcome">Welcome to Classify</div>
      <img class="img" src="../assets/backg.png" alt="logo" />
      <dir class="footer"></dir>
    </div>
    <div class="rightSide">
      <h3>Welcome Back!</h3>

      <div class="form-input">
        <input
          type="email"
          class="sign-up-email"
          id="email"
          v-model="login.username"
          placeholder="Email"
          required
        />
      </div>

      <div class="form-input">
        <input
          type="password"
          v-model="login.password"
          class="sign-up-password"
          placeholder="Password"
          required
        />
      </div>
      <button @click="loginUser" class="btn-submit">Sign In</button>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      login: {
        username: "",
        password: "",
      },
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.loggedIn;
    },
  },
  methods: {
    loginUser() {
      this.$store.dispatch("login", this.login);
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
:root {
  --gren: #083535;
}
.SignUp {
  display: flex;
}
.leftSide {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 50%;
  background-color: #eef3f3;
  padding-top: 50px;
  height: 100%;
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
  height: 420px;
}
.footer {
  background-color: #eef3f3;
  height: 200px;
}

.rightSide {
  width: 50%;
  display: flex;
  flex-direction: column;
  text-align: left;
  height: auto;
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
}
.rightSide h3 {
  margin-bottom: 100px;
  font-size: 32px;
  text-align: center;
  margin-top: 70px;
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
  margin-bottom: 24px;
}
.btn-submit {
  display: table;
  background-color: #083535;
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
  outline-width: 0;
  background-color: #eef3f3;
  font-weight: 400;
}
::placeholder {
  font-size: 20px;
  margin-left: 20px;
  padding-left: 28px;
}
::placeholder:focus {
  color: #000;
}
</style>
