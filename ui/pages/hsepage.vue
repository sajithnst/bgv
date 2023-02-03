<template>
    <v-app>
        <v-app-bar app color="indigo darken-3"> 
           <v-btn icon @click="home()" ><v-icon color="white">mdi-home</v-icon></v-btn>
           <v-spacer></v-spacer>
        </v-app-bar>
        <v-main>
            <v-container>
                <hse/>
            </v-container>
        </v-main>
    </v-app>
</template>
<script>
export default{
    name : "hsepage",
    async mounted(){
        this.$vuetify.theme.dark=false;
    },
    data : () =>({

    }),
    methods:{
        async home(){
            this.$router.push('/')
        }
    }
}
</script>