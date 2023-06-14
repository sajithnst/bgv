<template>
    <container>
    <admin/>
    </container>
    </template>
    <script>
    export default{
    name: "admin login",
    layout:'signinlayout',
    async mounted(){
    this.$vuetify.theme.dark=false;
    },
    data: () => ({
    
    }),
    }
    </script>
    <style>
    .signin{
    width: 30%;
    margin: 0% auto;
    text-align: center;
    }
    </style>