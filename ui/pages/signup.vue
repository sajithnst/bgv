<template>
    <v-app app>
    <v-app-bar app>
    <v-btn icon><v-icon size="32">mdi-home</v-icon></v-btn>
    <v-spacer> </v-spacer>
    <v-btn icon><v-icon size="32">mdi-arrow-left-bold</v-icon></v-btn>
    </v-app-bar>
    <v-main>
        <v-container class="signupform">
            <br/><br/>
            <h1 class="text-center">User Signup </h1>
            <br/><br/>
            <v-form>
            <v-alert dismissible type="success" v-model="success"> User creates successfully</v-alert>
            <v-alert dismissible type="error" v-model="fail"> User already exit </v-alert>
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
                        <v-text-field v-model="user.empid" label="Current Employee ID" :rules="[rules.required]"></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-text-field v-model="user.password" label="Password" type="password" :rules="[rules.required,rules.min]"></v-text-field>
                    </v-col>
                </v-row>
            </v-col>
            <v-btn large block color="teal" elevation="4" @click="signup()"> Signup</v-btn>
            </v-form>
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
            empid :'',
            firstlogin :true,
            status: 'pending'
        },
        success:false,
        fail:false,
        rules:{
            required: (v) => !!v || "Required",
            min : (v) =>  v.length > 8 || "Minimun 8 Characters is required",
            email : (v) => v.match(/\S+@\S+\.\S+/) || "Email format is wrong",
            name: (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters in Name"
        }
    }),
    methods:{
        async signup(){
    
            let res = await this.$axios.post('http://127.0.0.1:8000/user',this.user)
            if (res.data == true){

                this.success = true
            }else{
                this.fail = true
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