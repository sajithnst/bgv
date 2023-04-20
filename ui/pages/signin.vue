<template>

            <v-container justify="center" class="signinform">
              <br><br><br>
                <v-form>
                    <v-alert v-model="error" type="error" dismissible> Login Failed</v-alert>
                    <br/><br/>
                    <v-container class="text-center">
                    <img class="mr-3" :src="require('../assets/blockedge-logo.svg')" height="40"/>
                </v-container>
                    <br/>
                    <v-col>
                      <v-row>
                        <div class="text-subtitle-1 text-medium-emphasis ">Email ID</div>

                      </v-row>

                        <v-row>
                            <v-text-field v-model="signindata.email" label="Enter the email" :rules="[rules.email,rules.required]"></v-text-field>
                        </v-row>
                        <v-row>
                          <div class="text-subtitle-1 text-medium-emphasis ">Password</div>

                        </v-row>
                        <v-row>
                            <v-text-field v-model="signindata.password" label="Enter the Password" type="password" :rules="[rules.required,rules.min]"></v-text-field>
                        </v-row>
                        <br>
                        <v-row>
                            <v-container class="text-center">
                                <v-btn text  color="indigo lighten-1" @click="signin()"> Sign In</v-btn>
                            </v-container>
                        </v-row>
                    </v-col>
                </v-form>
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
            let userurl ='http://127.0.0.1:8000/user'
            await this.$axios.get(userurl,{params:{email : this.signindata.email}}).then(result =>{
                 this.firstlogin = result.data.firstlogin;
            }).catch(error =>{ console.log(error)});
            if (this.firstlogin == true){
                this.email = this.$storage.setUniversal('Email',this.signindata.email)

                this.$router.push('/onboard')
            }else{
                let url= 'http://127.0.0.1:8000/login'
                await this.$axios.post(url, this.signindata).then(res => {
                if (res.data.status == true){
                    if (res.data.user == 'user'){
                        this.email = this.$storage.setUniversal('Email',this.signindata.email)
                        console.log(this.email)
                        this.$router.push('/user')
                    }
                }else{
                    this.error = true;
                }
            }).catch(err => this.error=true);
            }

        },
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
