<template>
  <v-container class="adminsignin">
  <br/><br/>
  <v-form>
    <h1 class="text-center"> Admin Signin </h1>
    <br><br>
    <v-alert border="top" color="red lighten-1" dismissible v-if="fail"> Data insertion failed</v-alert>
    <v-row>
      <div class="text-subtitle-1 text-medium-emphasis "> Email ID</div>
    </v-row>
    <v-row>
      <v-text-field label="Enter the email" v-model="admin_email" :rules="[rules.required,rules.email]"></v-text-field>
    </v-row>
    <v-row>
      <div class="text-subtitle-1 text-medium-emphasis ">Password</div>
    </v-row>
    <v-row>
      <v-text-field label="Enter the password" v-model="password" type="password" :rules="[rules.required,rules.min]"></v-text-field>
    </v-row>
    <br>
    <v-container class="text-center">
      <v-btn text @click="login()" color="indigo darken-2" width="200px">Signin</v-btn>
    </v-container>
  </v-form>
  </v-container>
</template>
<script>
export default{
name :"admin",
data : () => ({
admin_email: "",
password: "",
fail: null,
rules : {
required: (v) => !!v || "Required",
min : (v) => v.match(/^(?=.*[A-Z])(?=.*[@])(?=.*[a-z])(?=.*\d).{8,}$/)|| "Enter Password with One Cap letter ,@,small letter and with the number is required",
email : (v) => v.match(/\S+@\S+\.\S+/) || "Email format is wrong",
}
}),
methods:{
async login(){
let url = "http://127.0.0.1:8000/adminlogin";
let login = {
admin_email : this.admin_email,
password : this.password,
}
let result = await this.$axios.post(url, login);
console.log(login)
if (result.data === true) {
this.$storage.setUniversal('admin_mail',this.admin_email)
this.$router.push('/SuperAdminRequests');
}else{
this.fail = true;
}
}
}
}
</script>
