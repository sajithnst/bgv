<template>
    <v-container class="hrsignin">
        <br/><br/>
        <v-form>
            <h1 class="text-center"> Company Signin </h1>
            <br><br>
            <v-alert border="top" color="red lighten-1" dismissible  v-if="fail"> Data insertion failed</v-alert>
            <v-row>
            </v-row>
            <v-row>
              <v-text-field  v-model="company_mail" :rules="[rules.required,rules.email]" label ="Company Email"></v-text-field>
            </v-row>
            <v-row>
            </v-row>
            <v-row>
              <v-text-field v-model="password" type="password" :rules="[rules.required,rules.min]" label="Password"></v-text-field>
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
            

            let url = "http://127.0.0.1:8000/hr/login";
            let nlogin = {
                company_mail: this.company_mail,
                password: this.password
            }
            let result = await this.$axios.get(url, {params:{'company_mail': this.company_mail, 'password': this.password}});
            if (result.data === true) {
                this.$storage.setUniversal('hrmail',this.company_mail)
                this.$router.push('/hrpage');
            }else{
                this.fail = true;
            }
            let nurl = "http://127.0.0.1:8000/hr/login_date"
       
            let nres =  await this.$axios.post(nurl, nlogin)
            
            
            
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
