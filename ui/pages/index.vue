<template>
<v-container >
      <v-sheet elevation="4"  color="indigo darken-4"  height="400px">
        <v-container fluid fill-height class="text-center">
          <h1 class="text-h2" style="color: white;margin-left:35%;"> VERIFI EDGE</h1>
          <h1 class="text-h6" style="color: white;margin-left:40%;">A Web 3.0 Application</h1>
          <h1 class="text-h4" style="color: white;margin-left:30%"> Effortless Background Checks </h1>
        </v-container>
      </v-sheet>
      <intro/>
      <whoneedsus/>
      <howitworks/>
      <partners/>
</v-container>
</template>

<script>

export default {
    name: "IndexPage",
    async mounted(){
        this.$vuetify.theme.dark=false
    },
    data: () => ({}),

}
</script>
<style>
.button{
  font-family:  Helvetica, Arial, sans-serif;
}

</style>