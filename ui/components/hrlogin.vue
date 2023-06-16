<template>
    <v-container class="hrsignin">
        <br/><br/>
        <v-form>
            <h1 class="text-center"> HR Signin </h1>
            <br><br>
            <v-alert border="top" color="red lighten-1" dismissible  v-if="fail"> Data insertion failed</v-alert>
            <v-row>
              <div class="text-subtitle-1 text-medium-emphasis ">HR Email ID</div>

            </v-row>
            <v-row>
              <v-text-field  v-model="company_mail" :rules="[rules.required,rules.email]"></v-text-field>
            </v-row>
            <v-row>
              <div class="text-subtitle-1 text-medium-emphasis ">Password</div>

            </v-row>
            <v-row>
              <v-text-field v-model="password" type="password" :rules="[rules.required,rules.min]"></v-text-field>
            </v-row>
            <br>


            <v-container class="text-center">
                <v-btn text @click="hrlogin()" color="indigo darken-2" width="200px">Signin</v-btn>
            </v-container>
        </v-form>
    </v-container>
</template>
<script>
export default{
    name : "hrlogin",
    data : () =>({
        company_mail : "",
        password : "",
        fail: null,
        rules : {
            required: (v) => !!v || "Required",
            min : (v) =>  v.length > 8 || "Minimun 8 Characters is required",
            email : (v) => v.match(/\S+@\S+\.\S+/) || "Email format is wrong",
        }
    }),
    methods:{
        async hrlogin(){
            let url = "http://127.0.0.1:8000/hrlogin";
            let hlogin = {
                company_mail : this.company_mail,
                password : this.password,
            }
            let result = await this.$axios.post(url, hlogin);
            if (result.data === true) {
                this.$storage.setUniversal('hrmail',this.company_mail)
                this.$router.push('/hrpage');
            }else{
                this.fail = true;
            }
        }
    }
}
</script>
<style>
.hrsignin {
    text-align: center;
    margin: 5% auto;
}
</style>
