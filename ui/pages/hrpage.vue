<template>
    <v-app>
        <v-app-bar app color="indigo darken-3"> 
           <v-btn icon @click="home()" ><v-icon color="white">mdi-home</v-icon></v-btn>
           <v-spacer></v-spacer>
        </v-app-bar>
        <v-main>
            <v-row dense>
                <v-col>
                    <v-container>
                        <inbox/>
                    </v-container>
                </v-col>
                <v-col>
                    <v-container>
                        <h1 class="text-center">Outgoing Requests</h1>
                    </v-container>
                </v-col>
            </v-row>
        </v-main>
    </v-app>
</template>
<script>
export default{
    name: 'hrpage',
    data: ()=>({

    }),
    methods:{
        async home(){
            this.$router.push('/');
        },
    }
}
</script>