<template>
    <v-app app>
    <v-app-bar app>
    <v-btn icon @click="home()"><v-icon size="32">mdi-home</v-icon></v-btn>
    </v-app-bar>
    <v-main>
        <v-container class="signupform">
            <br/><br/>
            <h1 class="text-center">User Signup </h1>
            <br/><br/>
            <v-form>
            <v-alert dismissible type="error" v-model="fail"> Duplicate User Email </v-alert>
            <v-col>
                <v-row>
                    <v-col>
                        <v-text-field v-model="user.name" label="Full Name" :rules="[rules.required, rules.name]"></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-text-field v-model="user.email" label="Personal Email" :rules="[rules.required,rules.email]"></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-text-field v-model="user.password" label="Password" type="password" :rules="[rules.required,rules.min]"></v-text-field>
                    </v-col>
                </v-row>
            </v-col>
            <v-btn large block color="teal" elevation="4" @click="submit()"> Submit</v-btn>
            </v-form>
            <br/><br/>
            <v-container v-if="sendotp">
                <v-form>
                    <v-alert v-model="error" type="error"  dismissible>OTP verification failed</v-alert>
                    <v-col>
                        <v-row>
                            <caption> An OTP is send to your provided email. Please enter the OTP below for verification</caption>
                        </v-row>
                        <v-row>
                            <v-text-field label ="Enter OTP Here" v-model="utop"></v-text-field>
                        </v-row>
                        <v-row>
                            <v-btn large block color="teal" @click="signup()">signup</v-btn>
                        </v-row>
                    </v-col>
                
                </v-form>
            </v-container>
        </v-container>
    </v-main>
</v-app>
</template>
<script>

export default{
    name:'signuppage',
    data:() => ({
        user :{
            name :'',
            email :'',
            password :'',
            firstlogin :true,
            status: 'pending'
        },
        success:false,
        fail:false,
        otp:'',
        utop:'',
        error:false,
        sendotp:null,
        rules:{
            required: (v) => !!v || "Required",
            min : (v) =>  v.length > 8 || "Minimun 8 Characters is required",
            email : (v) => v.match(/\S+@\S+\.\S+/) || "Email format is wrong",
            name: (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters in Name"
        }
    }),
    methods:{
        async home(){
            this.$router.push('/')
        },
        async submit(){
            let url = "http://127.0.0.1:8000/otp"
            let mdata = { params :{email : this.user.email}}
            await this.$axios.get(url,mdata).then(res => {
                this.otp = res.data
                this.sendotp = true
            }).catch(err => { console.log(err)});
        },
        async signup(){
            if (this.utop == this.otp){
                let url = "http://127.0.0.1:8000/user"
                await this.$axios.post(url,this.user).then(res => {
                    if (res.data == true){
                        this.success = true
                        this.$router.push('/signin')
                    }
                    else{
                        this.fail = true
                    }
                });
            }
            else {
                this.error = true
            }
        }
    }
}
</script>
<style>
.signupform{
    width: 30%;
    margin: 0% auto;
}
</style>