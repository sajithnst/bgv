<template>
    <v-app>
        <v-app-bar app color="indigo darken-3"> 
           <v-btn icon @click="home()" ><v-icon color="white">mdi-home</v-icon></v-btn>
           <v-spacer></v-spacer>
           <h3 class="white--text">{{ name }}</h3>
           <v-spacer></v-spacer>
           <v-btn icon @click="logout()" ><v-icon color="white">mdi-logout</v-icon></v-btn>
        </v-app-bar>
        <v-main>
            <v-row dense>
                <v-col>
                    <v-container fluid style="width:80%">
                        <mailstat/>
                    </v-container>
                    <v-container fluid style="width:80%">
                        <h3 class="indigo--text text-center"> Incoming requests</h3>
                        <incomingmail/>
                    </v-container>
                </v-col>
                <v-col>
                    <v-container fluid style="width:80%">
                        <h3 class="indigo--text text-center"> Outgoing requests</h3>
                       <outgoing/>
                    </v-container>
                </v-col>
            </v-row>
        </v-main>
    </v-app>
</template>
<script>
export default{
    name: 'hrpage',
    async mounted(){
        this.company_mail = await this.$storage.getUniversal('hrmail');
        let url = "http://127.0.0.1:8000/hrprofile";
        let hr={
            'company_mail': this.company_mail,
        }
        let result= await this.$axios.post(url,hr);
        this.name = result.data.name;
    },
    data: ()=>({
        company_mail:"",
        name :"",
    }),
    methods:{
        async home(){
            this.$router.push('/');
        },
        async logout(){
            this.$router.push('/hrsignin')
        },
    }
}
</script>