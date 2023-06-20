<template>
    <v-container >
        <Creg/>
    </v-container>
</template>
<script>
export default {
name: 'CompanyReg',
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