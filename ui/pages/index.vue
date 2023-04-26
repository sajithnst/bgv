<template>
<v-container >
    <v-row>
        <v-col>
            <h1 class="text-h2 text" style="color: black; margin-top: 30% ;"> VERIFI EDGE</h1><br/><br/>
            <h1 class="text-h6" style="color: black;">A Web 3.0 Application</h1><br/><br/>
            <h1 class="text-h4" style="color: black;"> Effortless Background Checks </h1>
        </v-col>
            &ensp; &ensp; &ensp; &ensp;
            <v-col>
              <v-img height="700px" width="700px" src="https://studentidentify.com/img/illustration-1.png"/>
            </v-col>
          </v-row>


      <intro/>
      <whoneedsus/>
      <br><br>
      <howitworks/>
      <br>
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
