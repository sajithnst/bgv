<template>
    <v-app onbord>
        <v-app-bar app color="indigo darken-3"> 
           <v-btn icon @click="home()" ><v-icon color="white">mdi-home</v-icon></v-btn>
           <v-spacer></v-spacer>
        </v-app-bar>
    <v-main>
        <v-container  v-if="personal" >
            <personal/>
        </v-container>
        <v-container  v-if="sslc">
            <sslc/>
        </v-container>
        <v-container class="form" v-if="hse">
            hse
        </v-container>
        <v-container class="form" v-if="ug">
        ug
        </v-container>
        <v-container class="form" v-if="pg">
            pg
        </v-container>
        <v-container class="form" v-if="exp">
            Experience
        </v-container>

    </v-main>
    </v-app>
</template>
<script>
export default {
    name: 'onbord',
    data: () => ({
        personal:true,
        sslc:null,
        hse:null,
        ug:null,
        pg:null,
        exp:null,
    }),
    methods:{
       
        async home(){
            this.$router.push('/')
        }

    }
}
</script>
<style>
.form{
    width: 55% ;

}
</style>