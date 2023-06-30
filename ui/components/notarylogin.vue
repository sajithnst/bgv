<template>
    <v-container class="hrsignin">
        <br/><br/>
        <v-form>
            <h1 class="text-center"> Admin Signin </h1>
            <br><br>
            <v-alert border="top" color="red lighten-1" dismissible  v-if="fail"> Data insertion failed</v-alert>
            <v-row>
              <v-text-field v-model="email" :rules="[rules.required,rules.email]" label ="Admin Email "></v-text-field>
            </v-row>
            <v-row>
              <v-text-field  v-model="password" type="password" :rules="[rules.required,rules.min]" label="Password"></v-text-field>
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
    name :"notarylogin",
    data : () => ({
        email: "",
        password: "",
        fail: null,
        rules : {
            required: (v) => !!v || "Required",
            min : (v) =>  v.length > 8 || "Minimun 8 Characters is required",
            email : (v) => v.match(/\S+@\S+\.\S+/) || "Email format is wrong",
        }
    }),
    methods: {
        async login(){
            let url = "http://127.0.0.1:8000/notary/login"
            let nlogin = {
                email: this.email,
                password: this.password
            }
            let res = await this.$axios.get(url,{params:{'email': this.email, 'password': this.password}});
            if(res.data == true){
                this.$storage.setUniversal('notaryemail',this.email)
                this.$router.push("/notary");
            }else{
                this.fail= true
            }
            let nurl = "http://127.0.0.1:8000/notary/logindate"
            let nres =  await this.$axios.post(nurl, nlogin)

        }
    }
}
</script>
