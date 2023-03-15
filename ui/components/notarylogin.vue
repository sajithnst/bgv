<template>
    <v-container class="hrsignin"> 
        <br/><br/>
        <v-form>    
            <h1 class="text-center"> Notary Signin </h1>
            <v-alert border="top" color="red lighten-1" dismissible  v-if="fail"> Data insertion failed</v-alert>
            <v-text-field label="Email" v-model="email" :rules="[rules.required,rules.email]"></v-text-field>
            <v-text-field label="Password" v-model="password" type="password" :rules="[rules.required,rules.min]"></v-text-field>
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
            let url = "http://127.0.0.1:8000/notarylogin"
            let nlogin = {
                email: this.email,
                password: this.password
            }
            let res = await this.$axios.post(url,nlogin);
            if(res.data == true){
                this.$storage.setUniversal('notaryemail',this.email)
                this.$router.push("/notary");
            }else{
                this.fail= true
            }
        
        }
    }
}
</script>