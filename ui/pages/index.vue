<template>
<v-container >


          <v-row>
            <v-col>
              <h1 class="text-h1 text" style="color: black;margin-left:20%; padding-top:28%"> VERIFI EDGE</h1>
              <br><br>
              <h1 class="text-h6" style="color: black;margin-left:38%;">A Web 3.0 Application</h1>
              <br><br>
              <h1 class="text-h4" style="color: black;margin-left:24%"> Effortless Background Checks </h1>

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
