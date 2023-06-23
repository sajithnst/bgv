<template>

            <v-container justify="center" class="signinform">
              <br><br><br>
                <v-form>
                  <h1 class="text-center"> User Login </h1>

                    <v-alert v-model="error" type="error" dismissible> Login Failed</v-alert>

                    <v-container class="text-center">
                </v-container>
                    <br/>
                    <v-col>
                        <v-row>
                            <v-text-field v-model="signindata.email"  :rules="[rules.email,rules.required]" label=" Personal Email "></v-text-field>
                        </v-row>
                        <v-row>
                            <v-text-field v-model="signindata.password"  type="password" :rules="[rules.required,rules.min]" label="Password"></v-text-field>
                        </v-row>
                        <br>
                        <v-row>
                            <v-container class="text-center">
                                <v-btn text  color="indigo lighten-1" @click="signin()"> Sign In</v-btn>
                            </v-container>
                        </v-row>
                    </v-col>
                </v-form>
                <br/><br/><br/><br/><br/><br/>
            </v-container>
</template>
<script>
export default{
    name : 'signinpage',
    layout : 'signinlayout',
    async mounted(){
        this.$vuetify.theme.dark=false;
    },
    data: () =>({
      return:{
        email:'',
        password:'',
      },
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
                let url= 'http://127.0.0.1:8000/login'
                let res = await this.$axios.get(url, {params:{'email':this.signindata.email, 'password': this.signindata.password}})
                if (res.data == true){

                        this.email = this.$storage.setUniversal('Email',this.signindata.email)
                        this.gmail = this.$storage.setUniversal('login_mail', this.signindata.email)
                        console.log(this.email)
                        this.$router.push('/user')

                }else{
                    this.error = true;
                }
            }

        },
    }

</script>
<style>
.v-btn{
 width: 250px;
}
.signinform{
    width: 30%;
    margin: 0% auto;
}
</style>
