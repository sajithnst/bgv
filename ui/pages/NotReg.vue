<template>
    <v-container >
        <Nreg/>
    </v-container>
</template>
<script>
export default {
name: 'NotReg',
layout:'datacollection',
async mounted(){
    this.$vuetify.theme.dark=false;
},
data: () => ({
}),
methods:{
   
    async home(){
    }

}
}
</script>
<style>
.form{
width: 55% ;

}
</style>