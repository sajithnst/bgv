<template>
    <v-app>
        <v-app-bar app color="indigo darken-3"> 
           <v-btn icon @click="home()" ><v-icon color="white">mdi-home</v-icon></v-btn>
           <v-spacer></v-spacer>
        </v-app-bar>
        <v-main>
            <Nuxt/>
        </v-main>
        <v-footer dark padless>
            <v-card class="flex" flat tile>
                <v-card-subtitle class="indigo darken-1">
                Copyright @ Securekloud Technologies Ltd {{ new Date().getFullYear() }}<br/> Author - Sajith Surendran
                </v-card-subtitle>
            </v-card>
        </v-footer>
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