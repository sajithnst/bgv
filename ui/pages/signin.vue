<template>
    <v-app signin>
        <v-app-bar app>
            <v-btn icon @click="home()"><v-icon size="32">mdi-home</v-icon></v-btn>
        </v-app-bar>
        <v-main>
            <v-container class="signinform">
                <v-form>
                    <v-alert v-model="error" type="error" dismissible> Login Failed</v-alert>
                    <br/><br/>
                    <h1 class="text-center"> User Login </h1>
                    <br/><br/>
                    <v-col>
                        <v-row>
                            <v-text-field v-model="signindata.email" label="Email ID" :rules="[rules.email,rules.required]"></v-text-field>
                        </v-row>
                        <v-row>
                            <v-text-field v-model="signindata.password" label="Password" type="password" :rules="[rules.required,rules.min]"></v-text-field>
                        </v-row>
                        <v-row>
                            <v-btn large block color="teal" @click="signin()"> Sign In</v-btn> 
                        </v-row>
                    </v-col>
                </v-form>
            </v-container>
        </v-main>
    </v-app>
</template>
<script>
export default{
    name : 'signinpage',
    data: () =>({
        signindata : {
            email : '',
            password :'',
            firstlogin : null, 

        },
        error : false,
        rules : {
            required: (v) => !!v || "Required",
            min : (v) =>  v.length > 8 || "Minimun 8 Characters is required",
            email : (v) => v.match(/\S+@\S+\.\S+/) || "Email format is wrong",
        }
    }),
    methods :{
        async signin(){
            let userurl ='http://52.27.5.60:8000/user'
            await this.$axios.get(userurl,{params:{email : this.signindata.email}}).then(result =>{
                 this.firstlogin = result.data.firstlogin;
            }).catch(error =>{ console.log(error)});
            if (this.firstlogin == true){
                this.$router.push('/data')
            }else{
                let url= 'http://52.27.5.60:8000/login'
                await this.$axios.post(url, this.signindata).then(res => {
                if (res.data.status == true){
                    if (res.data.user == 'user'){
                        this.$storage.setUniversal('Email',this.signindata.email)
                        this.$router.push('/user')
                    }
                }else{
                    this.error = true;
                }
            }).catch(err => this.error=true);
            }
            
        },
        async home(){
            this.$router.push('/')
        },
    },
}
</script>
<style>
.signinform{
    width: 30%;
    margin: 0% auto;
}
</style>