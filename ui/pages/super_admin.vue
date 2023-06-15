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

